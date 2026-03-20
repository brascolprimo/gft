#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob
import re

# ===== НАСТРОЙКИ =====
ARTICLES_DIR = "."                 # текущая папка (docs/gifts)
OUTPUT_FILE = "index.md"           # создаётся здесь же
IMAGE_PATH = "../assets/images/"   # путь к картинкам из папки gifts
IMAGE_EXT = ".webp"                # расширение изображений
PAGE_TITLE = "Все подарки Telegram"
PAGE_SUBTITLE = "Коллекционные подарки в одном месте"
# Для ссылок на статьи: из папки gifts относительный путь к статье — просто её slug
URL_PREFIX = ""                    # пустой, т.к. статьи лежат в той же папке
# ==================================================

def slug_to_name(slug):
    """plush-pepe -> Plush Pepe"""
    return slug.replace('-', ' ').title()

def slug_to_image_name(slug):
    """plush-pepe -> plushpepe"""
    return slug.replace('-', '')

def extract_upgraded(content):
    """
    Ищет в тексте статьи строку вида:
    <strong>Улучшено:</strong> 187 400 шт.
    Возвращает найденное число (как строку) или None.
    """
    pattern = r'Улучшено:</strong>\s*([\d\s\u202F]+?)(?:\s*(?:шт\.|\(|%|<\/)|$)'
    match = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
    if match:
        raw_number = match.group(1).strip()
        raw_number = re.sub(r'[\s\u202F]+', '', raw_number)
        return raw_number
    return None

def format_upgraded(num_str):
    """
    Принимает строку с числом и форматирует в тысячи.
    """
    if not num_str:
        return ""
    try:
        num = int(num_str)
    except ValueError:
        try:
            num = float(num_str)
        except ValueError:
            return ""
    if num >= 10000:
        thousands = round(num / 1000)
        return f"{thousands}k items"
    else:
        thousands = num / 1000
        rounded = round(thousands, 1)
        return f"{rounded:.1f}k items".replace('.', ',')

def generate_card_html(slug, upgraded):
    name = slug_to_name(slug)
    img_name = slug_to_image_name(slug)
    img_src = f"{IMAGE_PATH}{img_name}{IMAGE_EXT}"
    href = f"{URL_PREFIX}{slug}/"

    subtitle = format_upgraded(upgraded) if upgraded else "&nbsp;"

    return f'''        <!-- {name} -->
        <a href="{href}" class="nft-card grid">
            <div class="nft-image">
                <img src="{img_src}" alt="{name}">
            </div>
            <div class="nft-title">{name}</div>
            <div class="nft-subtitle">{subtitle}</div>
        </a>
'''

def main():
    # Собираем все .md файлы в текущей папке (docs/gifts)
    md_files = glob.glob(os.path.join(ARTICLES_DIR, "*.md"))
    # Исключаем сам index.md, если он уже есть
    md_files = [f for f in md_files if os.path.basename(f) != "index.md"]

    if not md_files:
        print("❌ Нет .md файлов (кроме index.md) в текущей папке.")
        return

    md_files.sort()

    # Создаём output файл в той же папке
    output_path = os.path.join(ARTICLES_DIR, OUTPUT_FILE)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# {PAGE_TITLE}\n\n")
        f.write(f"<div class=\"catalog-subtitle\">{PAGE_SUBTITLE}</div>\n\n")
        f.write("<div class=\"gift-grid\">\n")

        for md_file in md_files:
            slug = os.path.splitext(os.path.basename(md_file))[0]
            with open(md_file, 'r', encoding='utf-8') as article:
                content = article.read()
                upgraded = extract_upgraded(content)
            f.write(generate_card_html(slug, upgraded))

        f.write("</div>\n")

    print(f"✅ Готово! Сгенерировано {len(md_files)} карточек в {output_path}")

if __name__ == "__main__":
    main()
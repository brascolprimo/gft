#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob
import re

# ===== НАСТРОЙКИ =====
ARTICLES_DIR = "."
OUTPUT_FILE = "index.md"
IMAGE_PATH = "/assets/images/"
IMAGE_EXT = ".webp"
PAGE_TITLE = "Все подарки Telegram"
PAGE_SUBTITLE = "Коллекционные подарки в одном месте"
URL_PREFIX = "./"
# =====================

def slug_to_name(slug):
    """plush-pepe -> Plush Pepe"""
    return slug.replace('-', ' ').title()

def slug_to_image_name(slug):
    """plush-pepe -> plushpepe (удаляем дефисы)"""
    return slug.replace('-', '')

def extract_upgraded(content):
    """
    Ищет в тексте статьи строку вида:
    <strong>Улучшено:</strong> 187 400 шт.
    Возвращает найденное число (как строку) или None.
    """
    # Регулярное выражение: ищем "Улучшено:</strong>" + пробелы, затем группа цифр,
    # которая может содержать неразрывный пробел \u202F (или обычный пробел)
    # Допускаем также, что после числа может быть что угодно (до следующего тега или конца строки)
    pattern = r'Улучшено:</strong>\s*([\d\s\u202F]+?)(?:\s*(?:шт\.|\(|%|<\/)|$)'
    match = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
    if match:
        raw_number = match.group(1).strip()
        # Заменяем все виды пробелов на обычный пробел (для единообразия)
        raw_number = re.sub(r'[\s\u202F]+', '', raw_number)  # Удаляем все пробелы
        return raw_number
    return None

def format_upgraded(num_str):
    """
    Принимает строку с числом (например, "187400") и форматирует в тысячи.
    - Если число >= 10000: округляет до целых тысяч (187k)
    - Если число < 10000: округляет до 1 знака после запятой (5.6k)
    Возвращает строку вида "187k items" или "5.6k items".
    Если число не распознано, возвращает пустую строку.
    """
    if not num_str:
        return ""
    try:
        num = int(num_str)
    except ValueError:
        # Если вдруг попалось что-то с десятичной точкой, пробуем float
        try:
            num = float(num_str)
        except ValueError:
            return ""

    if num >= 10000:
        thousands = round(num / 1000)
        return f"{thousands}k items"
    else:
        thousands = num / 1000
        # Округляем до 1 знака после запятой
        rounded = round(thousands, 1)
        # Форматируем с одной цифрой после запятой, даже если это .0
        return f"{rounded:.1f}k items".replace('.', ',')  # если нужна запятая, раскомментируйте replace

def generate_card_html(slug, upgraded):
    name = slug_to_name(slug)
    img_name = slug_to_image_name(slug)
    img_src = f"{IMAGE_PATH}{img_name}{IMAGE_EXT}"
    href = f"{URL_PREFIX}{slug}/"

    # Форматируем подзаголовок
    subtitle = format_upgraded(upgraded) if upgraded else "&nbsp;"  # или пустая строка

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
    md_files = glob.glob(os.path.join(ARTICLES_DIR, "*.md"))
    md_files = [f for f in md_files if os.path.basename(f) != "index.md"]

    if not md_files:
        print("❌ Нет .md файлов (кроме index.md) в текущей папке.")
        return

    md_files.sort()

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
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

    print(f"✅ Готово! Сгенерировано {len(md_files)} карточек в {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
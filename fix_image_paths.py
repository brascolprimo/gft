#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

def fix_paths_in_file(filepath, docs_root='docs'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Определяем глубину вложенности файла относительно docs/
    rel_path = os.path.relpath(filepath, docs_root)
    parts = rel_path.split(os.sep)
    # Если файл называется index.md, он не создаёт дополнительную папку при сборке
    if parts[-1] == 'index.md':
        depth = len(parts) - 1
    else:
        depth = len(parts)

    prefix = '../' * depth  # например, '../' для depth=1, '' для depth=0

    # Заменяем src="/assets/images/... на src="<prefix>assets/images/...
    # Используем регулярку, чтобы не задеть случайные вхождения
    pattern = r'src="/assets/images/'
    replacement = f'src="{prefix}assets/images/'
    new_content = re.sub(pattern, replacement, content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'[✓] Исправлен: {filepath} (глубина {depth})')
    else:
        print(f'[–] Без изменений: {filepath}')

def main():
    docs_dir = 'docs'
    if not os.path.isdir(docs_dir):
        print(f'Ошибка: папка {docs_dir} не найдена.')
        return

    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                fix_paths_in_file(full_path, docs_dir)

    print('\nГотово! Проверь изменения и сделай коммит.')

if __name__ == '__main__':
    main()
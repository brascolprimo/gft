import os
from PIL import Image

# Настройки
MAX_SIZE = 400          # максимальная ширина или высота превью (пропорции сохраняются)
INPUT_FILES = [
    'stars.jpg',
    'stars-interface-placeholder.jpg'
]

def create_thumbnail(filepath, max_size):
    try:
        img = Image.open(filepath)
        # Изменяем размер с сохранением пропорций
        img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
        # Формируем имя для превью (добавляем _thumb)
        base, ext = os.path.splitext(filepath)
        thumb_path = f"{base}_thumb{ext}"
        # Сохраняем с хорошим качеством
        img.save(thumb_path, quality=90)
        print(f"✅ Создано: {thumb_path} ({img.width}x{img.height})")
    except Exception as e:
        print(f"❌ Ошибка при обработке {filepath}: {e}")

def main():
    print("🔧 Начинаю ресайз изображений...")
    for f in INPUT_FILES:
        if not os.path.exists(f):
            print(f"⚠️ Файл {f} не найден, пропускаю.")
            continue
        create_thumbnail(f, MAX_SIZE)
    print("🎉 Готово!")

if __name__ == "__main__":
    main()
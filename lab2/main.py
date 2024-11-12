import argparse

from annotation import create_csv_file_annotation
from iterator import Iterator
from download_image import download_images


def parsing() -> argparse.Namespace:
    """
    Парсинг аргументов командной строки
    :return: введённые аргументы
    """
    parser = argparse.ArgumentParser(description='Download images and create annotation.')
    parser.add_argument('keyword', type=str, help='Keyword for image search')
    parser.add_argument('save_dir', type=str, help='Directory to save images')
    parser.add_argument('annotation', type=str, help='Path to the annotation CSV file')
    args = parser.parse_args()
    return args


def main():
    args = parsing()
    try:
        download_images(args.keyword, args.save_dir)
        print("\n\nИзображения загружены успешно")
        create_csv_file_annotation(args.save_dir, args.annotation)
        print("Папка аннотации успешно создана")

        print("Проверка итератора с файлом аннотации:")
        iterator = Iterator(annotation=args.annotation)
        for image_path in iterator:
            print(image_path)

        print("\nПроверка итератора с папкой:")
        iterator = Iterator(image_dir=args.save_dir)
        for image_path in iterator:
            print(image_path)

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()
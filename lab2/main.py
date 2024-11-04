import argparse
import csv
import os

from icrawler.builtin import GoogleImageCrawler


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


def download_images(keyword: str, save_dir: str, num_images=50) -> None:
    """
    Скачивание изображений в save_dir
    :param keyword: ключевое слово
    :param save_dir: директория в которую сохраняются изображения
    :param num_images: количество изображений
    :return: None
    """
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    google_crawler = GoogleImageCrawler(storage={'root_dir': save_dir})
    google_crawler.crawl(keyword=keyword, max_num=num_images)


def create_csv_file_annotation(save_dir: str, annotation: str) -> None:
    """
    Создание аннотации к изображениям
    :param save_dir: директория с изображениями
    :param annotation: файл аннотации
    :return: None
    """
    with open(annotation, 'w', newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["absolute_path", "relative_path"])

        for filename in os.listdir(save_dir):
            if filename.endswith(('jpg', 'jpeg', 'png')):
                abs_path = os.path.abspath(os.path.join(save_dir, filename))
                rel_path = os.path.relpath(abs_path, save_dir)
                writer.writerow([abs_path, rel_path])


class Iterator:
    """
    Класс Итератора для изображений
    """
    def __init__(self, annotation: str=None, image_dir: str=None)->None:
        """
        Конструктор, инициализирующий массив строчек в зависимости от передаваемых аргументов
        файла аннотации или папки с изображениями
        :param annotation: файл аннотации
        :param image_dir: директория с изображениями
        """
        self.images = []
        if annotation:
            with open(annotation, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.images.append(row['absolute_path'])
        elif image_dir:
            for root, _, files in os.walk(image_dir):
                for filename in files:
                    if filename.endswith(('jpg', 'jpeg', 'png')):
                        self.images.append(os.path.join(root, filename))
        else:
            raise ValueError("Нужно указать файл аннотации или папку с изображениями")
        self.index = 0


    def __iter__(self) -> 'Iterator':
        """
        :return: возврат текущего объекта класса
        """
        return self


    def __next__(self) -> str:
        """
        Метод прохода по всем элементам массива класса через индекс и вывода их на экран
        :return: путь к текущему изображению
        """
        if self.index < len(self.images):
            image_path = self.images[self.index]
            self.index += 1
            return image_path
        else:
            raise StopIteration


def main():
    args = parsing()
    try:
        download_images(args.keyword, args.save_dir)
        print("\n\nИзображения загружены успешно загружены успешно")
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
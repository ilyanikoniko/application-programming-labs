import os

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

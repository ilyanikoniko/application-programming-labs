import cv2

from numpy import ndarray


def read_image(name_im: str) -> ndarray:
    """
    Чтение изображения
    :param name_im:путь к изображению
    :return:изображение в виде матрицы пикселей
    """
    return cv2.imread(name_im)


def show_image(img: ndarray) -> None:
    """
    Вывод изображения на экран
    :param img:изображение в виде матрицы пикселей
    :return:None
    """
    cv2.imshow('image', img)
    cv2.waitKey(0)


def size(img: ndarray) -> (int,int):
    """
    Вывод размера изображения
    :param img:изображение в виде матрицы пикселей
    :return:кортеж с параметрами
    """
    height, width, val = img.shape
    return height, width
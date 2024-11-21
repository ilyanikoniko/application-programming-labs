import cv2

from numpy import ndarray


def rotate_image(image: ndarray, angle: int) -> ndarray:
    """
    Вращение изображения на заданный угол
    :param image:изображение в виде матрицы пикселей
    :param angle:угол на который нужно повернуть изображение в градусах
    :return:повёрнутое изображение на указанный угол
    """
    height, width = image.shape[0], image.shape[1]
    center = (width / 2, height / 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1)
    rotated_im = cv2.warpAffine(image, matrix, (width, height))
    return rotated_im
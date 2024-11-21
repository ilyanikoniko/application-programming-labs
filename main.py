import argparse

from im_read import read_image, show_image, size
from histogram import create_histogram, show_histograms_of_channels
from rotate_img import rotate_image


def parse() -> argparse.Namespace:
    """
    Парсинг аргументов командной строки
    :return:введённые аргументы
    """
    parser = argparse.ArgumentParser(description='Process an image with optional rotation.')
    parser.add_argument('name_file', type=str, help='Name of the image file.')
    parser.add_argument('angle', type=int, help='Rotation angle in degrees.')
    args = parser.parse_args()
    return args


def main():
    args = parse()
    try:
        img = read_image(args.name_file)
        show_image(img)
        size_img = size(img)
        print(f"Image size: {size_img}")
        histogram_of_channels = create_histogram(img)
        show_histograms_of_channels(histogram_of_channels)
        rotated_im = rotate_image(img, args.angle)
        show_image(rotated_im)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
import os

from icrawler.builtin import GoogleImageCrawler


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
import csv
import os

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
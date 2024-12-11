import os
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from iterator import Iterator


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self) -> None:
        """
        Создание окна, компановок и виджетов
        """
        super().__init__()
        self.setWindowTitle("Средство просмотра изображений")
        self.setGeometry(500, 500, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        self.text = QLabel("Изображение", self)
        self.text.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.text)

        self.image_label = QLabel(self)
        self.image_label.setFixedSize(650, 500)  # задаем размер изображения
        self.image_label.setScaledContents(True)  # масштабирование изображения
        main_layout.addWidget(self.image_label)

        main_layout.addStretch()#гибкий промежуток

        button_layout = QHBoxLayout()
        self.btn_open = QPushButton("Выбрать папку с изображениями", self)
        self.btn_open.clicked.connect(self.open_folder_dialog)
        button_layout.addWidget(self.btn_open)

        self.btn_next = QPushButton("След. изображение", self)
        self.btn_next.clicked.connect(self.show_next_image)
        button_layout.addWidget(self.btn_next)
        self.btn_next.setEnabled(False)

        main_layout.addLayout(button_layout)

        self.err_text = QLabel("", self)
        self.err_text.setAlignment(Qt.AlignCenter)  # выравнивание текста по центру
        self.err_text.hide()
        main_layout.addWidget(self.err_text)

        self.image_iterator = None
        self.current_image = None

    def open_folder_dialog(self) -> None:
        """
        Открытие папки в диалоговом окне
        :return: None
        """
        folder_path = QFileDialog.getExistingDirectory(self, "Выберете папку с изображениями")

        if folder_path:
            image_files = [file for file in os.listdir(folder_path) if
            file.endswith(('.png', '.jpg', '.jpeg'))]

            if not image_files:
                self.err_text.setText("В папке нет изображений")
                self.err_text.show()
                self.image_label.hide()
                self.btn_next.setEnabled(False)
                return

            self.image_label.show()
            self.btn_next.setEnabled(True)
            self.image_iterator = Iterator(folder_path)
            try:
                self.current_image = next(self.image_iterator)
                self.display_image(self.current_image)
                self.err_text.hide()
            except StopIteration:
                self.err_text.setText("Больше нет изображений")
                self.err_text.show()


    def display_image(self, image_path) -> None:
        """
        Отображение изображения
        :param image_path: путь к изображению
        :return: None
        """
        pixmap = QPixmap(image_path)#загрузка изображения из директории
        if pixmap.isNull():
            self.err_text.setText(f"Изображение не загрузилось: {image_path}")
            self.err_text.show()
            return
        scaled_pixmap = pixmap.scaled(self.image_label.size(), aspectRatioMode=1)#масштабирование изображения
        self.image_label.setPixmap(scaled_pixmap)#вывод изображения


    def show_next_image(self) -> None:
        """
        Отображение следующего изображения
        :return: None
        """
        if self.image_iterator:
            try:
                self.current_image = next(self.image_iterator)
                self.display_image(self.current_image)
            except StopIteration:
                self.err_text.setText("Больше нет изображений")
                self.err_text.show()


def main():
    try:
        app = QtWidgets.QApplication(sys.argv)  # создание объекта QApplication
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(f'Ошибка: {e}')


if __name__ == "__main__":
    main()
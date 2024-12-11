import cv2
import matplotlib.pyplot as plt
import pandas as pd


def create_df(name_file: str)-> pd.DataFrame:
    """
    Создание DataFrame и добавление названий столбцов
    :param name_file:путь к CSV файлу
    :return:DataFrame
    """
    df = pd.read_csv(name_file, header=None)
    df.columns = ['Absolute_Path', 'Relative_Path']
    return df


def add_columns(df: pd.DataFrame) -> None:
    """
    Добавление трёх столбцов
    :param df:DataFrame
    :return:None
    """
    for i, path in enumerate(df["Absolute_Path"]):
        my_img = cv2.imread(path)
        height, width, depth = my_img.shape
        df.at[i, "Height"] = height
        df.at[i, "Width"] = width
        df.at[i, "Depth"] = depth


def statistic_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Статистическая информация о трёх добавленных столбцах
    :param df:DataFrame
    :return:DataFrame
    """
    return (df[['Height', 'Width', 'Depth']].describe())


def filter_df_by_h_w(max_height: int, max_width: int, df: pd.DataFrame) -> pd.DataFrame:
    """
    Фильтрация DataFrame по заданным значениям
    :param max_height:Максимальное значение высоты
    :param max_width:Максимальное значение ширины
    :param df:DataFrame
    :return:DataFrame
    """
    if max_width and max_height is not None:
        return df[(df['Height'] <= max_height) and (df['Width'] <= max_width)]
    elif max_width is None and max_height is not None:
        return df[(df['Height'] <= max_height)]
    elif max_height is None and max_width is not None:
        return df[(df['Width'] <= max_width)]
    return df


def add_column_area(df: pd.DataFrame) -> pd.DataFrame:
    """
    Добавление столбца с площадью
    :param df:DataFrame
    :return:DataFrame
    """
    df['Area'] = df['Height'] * df['Width']
    return df


def sort_by_area(df: pd.DataFrame) -> pd.DataFrame:
    """
    Сортировка DataFrame по площади
    :param df:DataFrame
    :return:DataFrame
    """
    return df.sort_values(by='Area', ascending=True)


def plot_area_histogram(column: pd.Series, title: str, count: str) -> None:
    """
    Построение гистограммы на основе площадей изображений
    :param column:колонка из DataFrame
    :return:None
    """
    plt.figure()
    column.hist(bins=50, edgecolor='black')
    plt.title(title)
    plt.xlabel(count)
    plt.ylabel('Count')
    plt.grid(True)
    plt.show()
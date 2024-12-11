import argparse

from work_with_DataFrame import create_df, add_columns, statistic_data, filter_df_by_h_w, add_column_area, sort_by_area, plot_area_histogram


def parsing() -> argparse.Namespace:
    """
    Парсинг аргументов командной строки
    :return:введённые аргументы
    """
    parser = argparse.ArgumentParser(description='Working with images of a certain height and width')
    parser.add_argument('name_file', type=str, help='Directory to save images')
    parser.add_argument('max_height', type=int, help='Maximum height for sorting')
    parser.add_argument('max_width', type=int, help='Maximum width for sorting')
    args = parser.parse_args()
    return args


def main():
    args = parsing()
    try:
        df = create_df(args.name_file)
        print(f'\nDataFrame\n{df.head()}')
        add_columns(df)
        print(f'\nИзменённый DataFrame\n{df.head()}')
        stat_inf = statistic_data(df)
        print(f'\nСтатистическая информация\n{stat_inf}')
        filtered_df = filter_df_by_h_w(args.max_width, args.max_height, df)
        print(f'\nФильтрация DataFrame\n{filtered_df}')
        add_column_area(df)
        print(f'\nDataFrame с площадью \n{df}')
        sort_df = sort_by_area(df)
        print(f'\nСортированный DataFrame\n{sort_df}')
        plot_area_histogram(df['Area'],"Histogram of areas", "Area(10^7)")
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
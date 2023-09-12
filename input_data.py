import os

from dotenv import load_dotenv

load_dotenv()

FILE_CSV_DIR_NAME = os.getenv('FILE_CSV_DIR_NAME')


def read_dir():
    """Получим имя директории и проверим ее существование."""
    print('Введите имя директории с текстовым файлом'
          + ' в формате D:\\Work\\1720'
          )
    # Надоело руками набирать)))
    file_dir_name = input()
    # file_dir_name = FILE_CSV_DIR_NAME
    # Проверим существование директории
    isExist = os.path.exists(file_dir_name)
    if isExist is True:
        # file_name_source = read_file_name_source()
        # file_dir_way = f'{file_dir_name}\\{file_name_source}'
        return file_dir_name
    else:
        # Если ее нет, то программа сломается. Обработчик ошибки дописать
        print('Такой директории не существует!!!')


def read_file_name_source():
    # Запросим у пользователя имя файла
    print('Введите имя файла исходника в формате CS009_2.txt')
    file_name_source = input()
    # Необходимо написать проверку существования файла
    # file_name_source = '07092023'
    return file_name_source


def read_file_name_receiver():
    # Запросим у пользователя имя файла
    print('Введите имя файла результата поиска данных в формате CS009_21.txt')
    # Файл будет создан или перезаписан, проверка не требуется
    file_name_receiver = input()
    # file_name_receiver = 'CS0081_21.txt'
    return file_name_receiver


def put_date_time_run():
    # Запросим у пользователя время начала для файла
    print('Введите дату/время начала в формате ДД.ММ.ГГ чч:мм:сс'
          ' (06.09.2023 10:00:00)')
    date_time_run = input()
    # date_time_run = '06.09.2023 10:00:00'
    return date_time_run


def put_date_time_end():
    # Запросим у пользователя время конца для файла
    print('Введите дату/время конца файла в формате ДД.ММ.ГГ чч:мм:сс'
          ' (06.09.2023 16:35:33)')
    date_time_end = input()
    # date_time_end = '06.09.2023 16:35:33'
    return date_time_end


def put_kks():
    # Запросим KKS датчика оборотов
    print('Введите KKS ДОС из файла НИКИЭТ в формате F_10JEB10CS008')
    kks = input()
    # kks = "F_10JEB10CS008"
    return kks

# -*- coding: utf-8 -*
import random
from multi_dl import *


def menu():
    i = input('Введите кол-во картинок: ')
    m = [str(random.randint(1, 100)) for x in range(int(i))]
    print(m)


if __name__ == '__main__':
    # menu()
    print('Загрузка в один поток началась...')
    main(download_many)
    print('Многопоточная загузка началась...')
    multi_main(multi_download_many)

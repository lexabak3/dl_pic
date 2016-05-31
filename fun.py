import os
import time
import sys
import requests

POP020_CC = ('1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20').split()

BASE_URL = 'http://savepic.ru/'

DEST_DIR = 'downloads/'


def save_img(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


def get_flag(cc):
    url = '{}/{cc}/{cc}.jpg'.format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    return resp.content


def show(text):
    print(text, end=' ')
    sys.stdout.flush()


def download_many(cc_list):
    for cc in sorted(cc_list):
        image = get_flag(cc)
        show(cc)
        save_img(image, cc.lower() + '.jpg')
    return len(cc_list)


def main(download_many):
    t0 = time.time()
    count = download_many(POP020_CC)
    elapsed = time.time() - t0
    msg = '\n{} pic downloaded in {:.2f}s'
    print(msg.format(count, elapsed))


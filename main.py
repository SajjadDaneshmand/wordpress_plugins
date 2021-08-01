from datetime import datetime
from zipfile import ZipFile
import settings
import shutil
import sys
import os


def not_zip_files(path):
    zips = []
    for i in os.listdir(path):
        if not i.endswith('.zip'):
            zips.append(i)
    return zips


def logger(text):
    with open(os.path.join(settings.BASE_DIR, 'plugin.log'), 'a') as f:
        f.write(text)


def check_files(src, file_name):
    files = os.listdir(src)
    for item in files:
        if file_name == item:
            return False
    return True


def main(path, zip_path=None):
    zip_path = zip_path or settings.PLUGIN_DIR

    if os.path.exists(path):
        for zip in os.listdir(zip_path):
            full_zip_path = os.path.join(zip_path, zip)
            ZipFile(full_zip_path).extractall(zip_path)
        extracted = not_zip_files(zip_path)

        for site in os.listdir(path):
            for folder in extracted:
                des = os.path.join(path, site, settings.wordpress_plugin_path, folder)
                checker = os.path.join(path, site, settings.wordpress_plugin_path)
                src = os.path.join(zip_path, folder)
                if os.path.isdir(checker):
                    if not check_files(checker, folder):
                        log = f'folder {folder} was exist in {src}!'
                        print(log)
                        logger(f'in time: {str(datetime.now())} => {log}\n')
                        continue
                    shutil.copytree(src, des)

                else:
                    log = f'site: {site} does not have wp-content/plugin'
                    print(log)
                    logger(f'in time: {str(datetime.now())} => {log}\n')
                    continue

        for exf in not_zip_files(zip_path):
            full_path = os.path.join(zip_path, exf)
            shutil.rmtree(full_path)
    else:
        log = 'your path of the websites does not exist!'
        print(log)
        logger(f'in time: {str(datetime.now())} => {log}\n')
        sys.exit()


if __name__ == '__main__':
    path = input('please enter the path: ')
    zip_path = input('please enter the zip path: ')
    main(path, zip_path)

            


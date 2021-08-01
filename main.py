from zipfile import ZipFile
import shutil
import os
import sys

def zip_files(path):
    zips = []
    for i in os.listdir(path):
        if i.endswith('.zip'):
            zips.append(i)
    return zips


path = input('please enter the path: ')
zip_path = input('please enter the zip path: ')


if len(zip_path) == 0:
    zip_path = '/home/sajjad/Project/wordpress_plugins/Plugin'



try:
    os.chdir(path)
except FileNotFoundError:
    print('your path does not exist!')
    sys.exit()

cwd = os.getcwd()

ls = os.listdir()

for dir in ls:
    os.chdir(f'{dir}/wp-content/plugins/')
    for zip in zip_files(zip_path):
        shutil.copyfile(f'{zip_path}/{zip}',f'{os.getcwd()}/{zip}')
        ZipFile(zip).extractall()
        os.remove(zip)
    os.chdir(cwd)



import os
import platform


def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')


def create_directory():
    if not os.path.exists('clients/'):
        os.makedirs('clients/')

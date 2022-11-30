"""
    Check our files
"""
import time
from os import listdir
from os.path import getsize

import colorama


def print_dirr(dirr: str) -> list:
    """
        Do a print of thh actual dir situation
    """
    return [f for f in listdir(dirr) if f.endswith(".csv")]


def compar(old_dirr: list, new_dirr: list) -> list:
    """
        Compar two list of files
    """
    return [x for x in new_dirr if x not in old_dirr]


def watcher(dirr: str, timer: int) -> str:
    """
        Look for us\n
        Timer: seconds
    """
    while True:
        if 'watching' not in locals():
            old_files_list = print_dirr(dirr)
            watching = 1
        time.sleep(timer)
        new_files_list = print_dirr(dirr)
        diff = compar(old_files_list, new_files_list)
        old_files_list = new_files_list
        if len(diff) == 0:
            print(colorama.Fore.BLUE + "Not new" + colorama.Style.RESET_ALL)
            continue
        if getsize(dirr + '/' + diff[0]) == 0:     
            print(colorama.Fore.BLUE + "Empty file" + colorama.Style.RESET_ALL)
            continue
        return diff[0]

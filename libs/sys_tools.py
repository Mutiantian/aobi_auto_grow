import os.path

from config import logger
from config import root_file
import shutil
import datetime

def get_date():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d")

def get_time():
    # 获得当前时间
    now = datetime.datetime.now()
    # 转换为指定的格式:
    otherStyleTime = now.strftime("%Y-%m-%d__%H-%M-%S")
    return otherStyleTime

def move_file_todebug(file_name_list):
    debug_path = os.path.join(root_file, "debug")
    if type(file_name_list) is not list:
        file_name_list = [file_name_list]

    for i in file_name_list:
        if os.path.exists(i) is False:
            logger.error("待转存的文件不存在")
            return False

    if os.path.exists(debug_path) is False:
        os.mkdir(debug_path)
    c = 0
    for i in file_name_list:
        shutil.move(i, os.path.join(debug_path, f"{c}{get_time()}{os.path.split(i)[1]}"))
        logger.debug(f"move {i} to debug path success!")
        c += 1

if __name__ == '__main__':
    move_file_todebug(os.path.join(root_file, "resources", "images", "battle.png"))

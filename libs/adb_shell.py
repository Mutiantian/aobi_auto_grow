import os.path
import time
from config import logger
from config import root_file
from libs.image_recognition import IMAGEMETHOD
import subprocess

# adb的一些操作
class ADBMETHODS:
    def __init__(self, devices):
        self.devices = devices

    def query_status(self):
        return subprocess.getoutput("adb devices")

    def connect(self):
        # 127.0.0.1:7555
        subprocess.getoutput("adb connect {}".format(self.devices))
        if self.devices in self.query_status():
            logger.info("devices conected success!")
            return True
        else:
            logger.error("devices conected FAILED!")
            return False

    def disconnect(self):
        # 127.0.0.1:7555
        subprocess.getoutput("adb disconnect {}".format(self.devices))
        if self.devices not in self.query_status():
            logger.info("devices disconected success!")
            return True
        else:
            logger.error("devices disconected FAILED!")
            return False

    def click(self, x, y):
        time.sleep(0.5)
        os.system("adb -s {} shell input tap {} {}".format(self.devices, x, y))
        logger.debug("has tap {},{}".format(x,y))

    def drag(self, x, y, has_crod=None, speed=500):
        time.sleep(0.5)
        if has_crod is None:
            os.system("adb -s {} shell input swipe {} {} {} {} {}".format(self.devices, x, y, x+300, y+300, speed))
        else:
            os.system("adb -s {} shell input swipe {} {} {} {} {}".format(self.devices, x, y, has_crod[0], has_crod[1], speed))
        logger.debug("has drag {},{}".format(x,y))

    def click_image(self, image_path, only_recognition=False, get_coord=False, confidence=0.7):

        if os.path.isfile(image_path) is False:
            image_path = os.path.join(root_file, "resources", "images", image_path)
        click_tmp_file = "auto_all_png_click.png"
        src_file = "/sdcard/{}".format(click_tmp_file)
        dst_file = os.path.join(root_file, "tmp", click_tmp_file)
        self.make_screenshot(src_file)
        self.download_file(src_file, dst_file)
        get_coo = IMAGEMETHOD.get_coordinate(image_path, dst_file, confidence=confidence)
        if get_coo is False:
            logger.error("识别图片出错")
            # 识别图片出错后把图片转存，用来排查问题
            # sys_tools.move_file_todebug([dst_file])
            return False
        else:
            logger.info("success to recognition image")
        if get_coord is True:
            os.remove(dst_file)
            self.rm_file("/data/auto_all_png.png")
            return get_coo
        elif only_recognition is False:
            self.click(get_coo[0], get_coo[1])

        # 点击后把下载下来的图片删除
        os.remove(dst_file)
        self.rm_file("/data/auto_all_png.png")
        return True

    def drag_image(self, image_path, only_recognition=False, get_coord=False, has_crod=None, confidence=0.7, speed=500):
        if os.path.isfile(image_path) is False:
            image_path = os.path.join(root_file, "resources", "images", image_path)
        click_tmp_file = "auto_all_png_click.png"
        src_file = "/sdcard/{}".format(click_tmp_file)
        dst_file = os.path.join(root_file, "tmp", click_tmp_file)
        self.make_screenshot(src_file)
        self.download_file(src_file, dst_file)
        get_coo = IMAGEMETHOD.get_coordinate(image_path, dst_file, confidence=confidence)
        if get_coo is False:
            logger.error("识别图片出错")
            # 识别图片出错后把图片转存，用来排查问题
            # sys_tools.move_file_todebug([dst_file])
            return False
        else:
            logger.info("success to recognition image")
        if get_coord is True:
            return get_coo
        elif only_recognition is False:
            self.drag(get_coo[0], get_coo[1], has_crod=has_crod, speed=speed)

        # 点击后把下载下来的图片删除
        os.remove(dst_file)
        self.rm_file("/sdcard/auto_all_png.png")
        return True

    def rm_file(self, file_name):
        os.system("adb -s {} shell rm -f {}".format(self.devices, file_name))
        logger.debug("rm_file {}".format(file_name))

    def input(self, msg):
        os.system("adb -s {} shell input text {}".format(self.devices, msg))
        logger.debug("has input {}".format(msg))

    def del_text(self, times):
        for i in range(times):
            os.system("adb shell input keyevent 67")

    def download_file(self, src_path, dst_path):
        if os.path.exists(dst_path):
            os.remove(dst_path)
        logger.debug(f"now download [{src_path}] to [{dst_path}]")
        os.system('adb -s {} pull "{}" "{}" > nul'.format(self.devices, src_path, dst_path))
        time.sleep(1)
        if os.path.exists(dst_path):
            logger.info("下载图片成功")
            return True
        else:
            logger.error("下载图片失败")
            return False

    def make_screenshot(self, file_name: str):
        # 默认存放到/data目录下,如果file_name没有auto开头，自动加上标识，方便后续清理空间

        file_name = f"/sdcard/{file_name}" if file_name.startswith("/sdcard") is False else file_name
        logger.debug(f"now make screencap: [{file_name}]")
        os.system("adb -s {} shell screencap {} > nul".format(self.devices, file_name))

if __name__ == "__main__":
    pass
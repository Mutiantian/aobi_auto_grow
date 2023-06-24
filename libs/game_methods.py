from config import *
from libs.adb_shell import ADBMETHODS

class GAMESFLOW:
    def __init__(self):
        self.device = ADBMETHODS("127.0.0.1:5555")
        self.device.connect()

    def wait(self, image:str, access=True, retry=5, time_out=5):
        if os.path.isabs(image) is False:
            image = os.path.join(root_file, "resources", "images", image)
        time.sleep(3)
        for i in range(retry):
            if self.device.click_image(image, only_recognition=True) is access:
                logger.info("wait image as except:{}".format(access))
                return True
            else:
                logger.warning("image not access as except:{}".format(access))
                time.sleep(time_out)
        logger.error("image not access as except:{},FAILED!".format(access))
        return False

    def click_until(self, target_img, click_img=None, Coord=None, retry=4, timewait=2):
        time.sleep(3)
        if os.path.isabs(target_img) is False:
            target_img = os.path.join(root_file, "resources", "images", target_img)
        if click_img is not None:
            Coord = self.device.click_image(click_img, get_coord=True)
            if Coord is False:
                logger.error("get click_img coord [{}] FAILED!".format(click_img))
                return False
        for i in range(retry):
            self.device.click(*Coord)
            if self.device.click_image(target_img, only_recognition=True):
                logger.info("点击：【{}】后成功识别到目标图片:[{}]！".format(click_img if click_img is not None else Coord, target_img))
                return True
            elif i == retry -1:
                logger.error("click until方法捕获图片【{}】执行重试后依旧失败！".format(target_img))
                return False
            else:
                logger.warning("click until方法捕获图片【{}】执行失败！".format(target_img))
                time.sleep(timewait)


    def sleep(self, sec):
        time.sleep(sec)
        return self

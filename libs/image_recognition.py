import os.path

from config import logger
import pyautogui as pag


class IMAGEMETHOD:
    def __init__(self):
        pass

    @staticmethod
    def get_coordinate(small_image, big_image, confidence=0.7):
        file_not_exist = 0
        if os.path.exists(small_image) is False:
            logger.error(f"small_image: [{small_image}] is not exists")
            file_not_exist += 1
        if os.path.exists(big_image) is False:
            logger.error(f"big_image: [{big_image}] is not exists")
            file_not_exist += 1
        if file_not_exist != 0:
            logger.error("待匹配的图片不存在，请排查:small_image:[{}]; big_image:[{}]".format(small_image, big_image))
            return False
        imgCoordinate = pag.locate(small_image, big_image, confidence=confidence)
        if imgCoordinate is None:
            logger.error(f"未从大图:[{big_image}]中匹配到小图[{small_image}]")
            return False
        return pag.center(imgCoordinate)

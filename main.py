import os.path
import sys
import time
from config import logger
from libs.game_methods import GAMESFLOW

interval = {
    "limai": 15,
    "lanmei": 30,
    "xionggua": 60,
    "yama": 60,
    "shengnvguo": 60,
}


def work_flow(zuowu):
    logger.info("检查作物是否成熟")
    while True:
        if g.device.click_image(os.path.join(zuowu, "chengshu.png")) is False:
            break
        time.sleep(1)
        g.device.drag_image("shou.png")
    logger.info("所有作物都收获完毕，接下来种植作物")
    while True:
        if g.device.click_image("tudi.png", confidence=0.9) is False:
            break
        time.sleep(1)
        tudi_crod = g.device.click_image("tudi.png", get_coord=True, confidence=0.9)
        g.device.drag_image(os.path.join(zuowu, "zhongzi.png"), has_crod=[tudi_crod[0], tudi_crod[1] - 200], speed=1200)
    logger.info("所有作物都种植完毕")

if __name__ == '__main__':
    zuowu = sys.argv[1:]
    if len(zuowu) == 0 or zuowu[0].strip() not in interval.keys():
        usage_detail = '\r\n\t\t'.join(interval.keys())
        logger.info(f"参数:{zuowu}错误!\r\n使用方法:\r\n\tpython main.py {{作物类型}}\r\n\t作物类型参数支持:\r\n\t\t{usage_detail}")
        sys.exit(1)

    logger.info(f"你将种植作物：{zuowu[0]}")
    g = GAMESFLOW()
    while True:
        work_flow(zuowu[0])
        logger.info(f"已完成一轮收获和种植，等待{interval[zuowu[0]]}秒后继续检查作物是否成熟")
        time.sleep(interval[zuowu[0]])

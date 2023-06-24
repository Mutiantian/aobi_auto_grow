import logging
import time
import os
from loguru import logger

class PropogateHandler(logging.Handler):
    def emit(self, record):
        logging.getLogger(record.name).handle(record)


logger.add(PropogateHandler(), format="{time:YYYY-MM-DD at HH:mm:ss} | {message}", level="INFO")

# 日志格式定义
format_str = '<green>{time: YYYY-MM-DD at HH:mm:ss.SSS}</green> ' \
             '| <cyan>{file: ^15}:{line: >3}</cyan> ' \
             '| <level>{level: <8} - {message}</level>'
RUN_TIME = time.strftime('%Y-%m-%d::%H_%M_%S', time.localtime(time.time()))

# 根目录，方便拼接路径
root_file = os.path.join(os.path.split(os.path.realpath(__file__))[0], "..")

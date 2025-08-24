from loguru import logger
from telegram import Telegram

if __name__ == '__main__':
    logger.info('Start notifying')

    with Telegram() as tele:
        text = "🔥 Thông tin overview đã được tổng hợp tại: https://github.com/AnhTuPhi/stock-market-analysis/tree/master/src/data/stock"
        tele.send_message(text, parse_mode=None)

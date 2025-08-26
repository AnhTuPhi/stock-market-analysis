from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict
from vnstock.botbuilder.noti import Messenger


class TelegramSettings(BaseSettings):
    bot_token: str
    chat_id: str

    model_config = SettingsConfigDict(
        extra='ignore',
        env_prefix='TELEGRAM_',
        env_file='.env',
        env_file_encoding='utf-8',
    )


if __name__ == '__main__':
    logger.info('Notifying overview weekly')

    settings = TelegramSettings()
    noti = Messenger(
        platform='telegram',
        channel=settings.chat_id,
        token_key=settings.bot_token
    )

    try:
        noti.send_message(
            message="🔥 Thông tin tổng quan mỗi tuần đã được tổng hợp tại: https://github.com/AnhTuPhi/stock-market-analysis/tree/master/data/stock")
    except Exception as e:
        logger.error("Notifying overview error: {}", e)

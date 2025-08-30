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
        with open("../templates/TEMP_OVERVIEW_WEEKLY.j2", "r", encoding="utf-8") as stream:
            content = stream.read()
        noti.send_message(message=content)
        logger.info("Already sent notification")
    except Exception as e:
        logger.error("Notifying overview error: {}", e)

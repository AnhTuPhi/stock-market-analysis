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


def send_message(message: str) -> None:
    settings = TelegramSettings()
    noti = Messenger(
        platform='telegram',
        channel=settings.chat_id,
        token_key=settings.bot_token
    )
    noti.send_message(message=message)


def send_photo(message: str, title: str, file_path: str) -> None:
    settings = TelegramSettings()
    noti = Messenger(
        platform='telegram',
        channel=settings.chat_id,
        token_key=settings.bot_token
    )
    noti.send_message(message=message, title=title, file_path=file_path)

__author__ = 'Phi Anh Tu'
__github__ = 'https://github.com/AnhTuPhi'
__email__ = 'phianhtu2211@gmail.com'
__url__ = 'https://github.com/AnhTuPhi/clean-architecture-python-boilerplate/blob/main/src/settings/telegram.py'

from pydantic_settings import BaseSettings, SettingsConfigDict


class TelegramSettings(BaseSettings):
    bot_token: str
    chat_id: str

    model_config = SettingsConfigDict(
        extra='ignore',
        env_prefix='TELEGRAM_',
        env_file='.env',
        env_file_encoding='utf-8',
    )

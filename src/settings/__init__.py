__author__ = 'Phi Anh Tu'
__github__ = 'https://github.com/AnhTuPhi'
__email__ = 'phianhtu2211@gmail.com'
__url__ = 'https://github.com/AnhTuPhi/clean-architecture-python-boilerplate/blob/main/src/settings/__init__.py'

__all__ = [
    'MariadbSettings',
    'RabbitmqSettings',
    'RedisSettings',
    'TelegramSettings',
]


from .mariadb import MariadbSettings
from .rabbitmq import RabbitmqSettings
from .redis import RedisSettings
from .telegram import TelegramSettings

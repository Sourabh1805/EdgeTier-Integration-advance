import logging

from config import settings
from logging_config import configure_logging

print(settings.OUR_API)
print(settings.ENV)
print(settings.SQLALCHEMY_DATABASE_URI)


logger = logging.getLogger(__name__)
configure_logging()
logger.info("Hello World")
print(settings.SQLALCHEMY_DATABASE_URI)

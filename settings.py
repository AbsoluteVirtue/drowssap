import os.path
import yaml
import logging
from yaml import FullLoader


async def close_session(app):
    app['http'].close()


def get_config(path):
    config_file = os.path.abspath(path)
    with open(config_file) as f:
        config = yaml.load(f, Loader=FullLoader)

    return config


def get_logger():
    logger = logging.getLogger(name='aiohttp.server')
    logger.setLevel(logging.INFO)

    return logger

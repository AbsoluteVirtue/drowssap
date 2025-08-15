import argparse
import os.path
import yaml
import logging
from yaml import FullLoader


async def close_session(app):
    app['http'].close()


def get_config():
    parser = argparse.ArgumentParser(description='Process arguments.')
    parser.add_argument(
        '--config_file', dest='config_file', default='./config/local.yaml', help='config file path')

    _path = parser.parse_args().config_file

    config_file = os.path.abspath(_path)
    with open(config_file) as f:
        _config = yaml.load(f, Loader=FullLoader)

    return _config, _path


def get_logger():
    _logger = logging.getLogger(name='aiohttp.access')
    _logger.setLevel(log_level)
    _logger.addHandler(logging.StreamHandler())

    return _logger


config, path = get_config()

log_level = logging.DEBUG if config['debug'] else logging.INFO

logging.getLogger('aiohttp.server').setLevel(log_level)
logging.getLogger('aiohttp.web').setLevel(log_level)

logger = get_logger()

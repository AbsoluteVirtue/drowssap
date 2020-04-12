import aiohttp_jinja2
import asyncio
import os.path
import jinja2
import logging
from aiohttp import web

from routes import setup_routes
from settings import config, logger, path
from utils import init_mongo


async def setup_mongo(app, loop):
    mgo = await init_mongo(loop)

    async def close_mongo():
        mgo.client.close()

    app.on_cleanup.append(close_mongo)
    return mgo


async def make_app():
    loop = asyncio.get_event_loop()
    app = web.Application(loop=loop)

    app['config'] = config
    app['logger'] = logger
    app['db'] = await setup_mongo(app, loop)

    setup_routes(app)

    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(os.path.abspath('templates')))

    return app


if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    logging.info('Web server started on port %s' % config['port'])
    logging.info('Config file: %s' % path)

    web.run_app(make_app(), host=config['host'], port=config['port'],
                access_log_format='%t "%r" %s %Tf ms -ip:"%a" -ref:"%{Referer}i"')

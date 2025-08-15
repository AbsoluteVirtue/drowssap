import motor.motor_asyncio as aiomotor

from settings import config


async def init_mongo(loop):
    return aiomotor.AsyncIOMotorClient(io_loop=loop, **config['mongo']['kwargs'])[config['mongo']['db']]

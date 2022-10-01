import asyncio
from utils import init_mongo
import utils.store_mongo as store


def launch_db():
    import subprocess
    import sys

    p = subprocess.Popen(["powershell.exe",
                          "mongod --dbpath D:\\mgo\\drow"], stdout=sys.stdout)
    p.communicate()


async def main():
    loop = asyncio.get_running_loop()
    loop.run_in_executor(None, launch_db)

    await asyncio.sleep(10.)

    mgo = await init_mongo(loop)

    data = await store.get_list(mgo)

    mgo.client.close()


if __name__ == '__main__':
    asyncio.run(main())

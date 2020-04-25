import datetime
import uuid

from utils import gen_cryptography as generator


async def get_pword(db, _id):
    data = await db.entries.find_one({'_id': _id})
    return generator.decrypt(data['key'], data['token'])


async def get_list(db, fields=None):
    res = await db.entries.find({'_valid_': True}, projection=fields).to_list(length=None)
    return res


async def hide(db, _id):
    res = await db.entries.find_and_modify({'_id': _id}, {'$set': {
        '_valid_': False,
        'ts_updated': datetime.datetime.now().timestamp(),
    }})
    return res


async def insert(db, **kwargs):
    key, token = generator.generate_hashed_pword()
    data = {
        '_id': uuid.uuid4().hex,
        '_valid_': True,
        'ts_inserted': datetime.datetime.now().timestamp(),
        'token': token,
        'key': key,
    }
    data.update(kwargs)
    res = await db.entries.insert_one(data)
    return res


async def update(db, _id, data):
    pass


async def change_pword(db, _id):
    pass

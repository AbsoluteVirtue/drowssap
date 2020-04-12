import aiohttp.web
import aiohttp_jinja2
import json

from . import base


class List(base.Base):

    async def get(self):
        data = {'data': [{'_id': '1', 'name': 'test.com'}]}
        response = aiohttp_jinja2.render_template('home.html', self.request, context=data)
        return response


class Generator(base.Base):

    async def get(self):
        data = {'_id': '1', 'name': 'test.com', 'payload': '1s2o3l4o'}
        return aiohttp.web.Response(body=json.dumps(data))

    async def post(self):
        pass

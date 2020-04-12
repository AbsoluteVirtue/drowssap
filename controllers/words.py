import aiohttp.web
import aiohttp_jinja2
import json

from . import base
import utils.clip_win as clip


class List(base.Base):

    async def get(self):
        data = {'data': [{'_id': '1', 'name': 'a', 'url': 'test.com', 'email': 'a@test.com'}]}
        response = aiohttp_jinja2.render_template('home.html', self.request, context=data)

        return response


class Generator(base.Base):

    async def get(self):
        data = {'_id': '1', 'name': 'test.com', 'payload': '1s2o3l4o'}

        pword = data['payload']

        clip.paste(pword)

        location = self.request.app.router['home'].url_for()

        raise aiohttp.web.HTTPFound(location=location)

    async def post(self):
        pass

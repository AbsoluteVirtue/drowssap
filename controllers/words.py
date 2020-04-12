import aiohttp.web
import aiohttp_jinja2

from . import base
import utils.clip_win as clip
import utils.store_mongo as store


class List(base.Base):

    async def get(self):
        data = await store.get_list(self.request.app['db'])
        response = aiohttp_jinja2.render_template('home.html', self.request,
                                                  context={'data': data})
        return response


class Generator(base.Base):

    async def get(self):
        _id = self.request.match_info['id']

        pword = await store.get_pword(self.request.app['db'], _id)

        clip.paste(pword)

        location = self.request.app.router['home'].url_for()
        raise aiohttp.web.HTTPFound(location=location)

    async def post(self):
        payload = {'name': 'a', 'url': 'test.com', 'email': 'a@test.com'}

        await store.insert(self.request.app['db'], **payload)

        location = self.request.app.router['home'].url_for()
        raise aiohttp.web.HTTPFound(location=location)

    async def patch(self):
        _id = self.request.match_info['id']

        payload = {}

        await store.update(self.request.app['db'], _id, payload)

        location = self.request.app.router['home'].url_for()
        raise aiohttp.web.HTTPFound(location=location)

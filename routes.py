from controllers import words


def setup_routes(app):
    app.router.add_view(r'/', handler=words.List, name='home')
    app.router.add_view(r'/gen/{id:[0-9a-f]{32}\Z}', handler=words.Generator, name='gen')
    app.router.add_view(r'/gen', handler=words.Generator, name='gen_create')

from controllers import words


def setup_routes(app):
    app.router.add_view(r'/', handler=words.List)
    app.router.add_view(r'/gen', handler=words.Generator)

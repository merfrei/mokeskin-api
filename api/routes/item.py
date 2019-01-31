from api.handlers.item import get_handler
from api.handlers.item import post_handler
from api.handlers.item import put_handler
from api.handlers.item import delete_handler
from api.handlers.item import ttl_handler


def init_item_routes(app):
    app.router.add_route('GET', '/items/{key:.+}', get_handler)
    app.router.add_route('POST', '/items', post_handler)
    app.router.add_route('PUT', '/items', put_handler)
    app.router.add_route('DELETE', '/items/{key:.+}', delete_handler)
    app.router.add_route('GET', '/ttl/{key:.+}', ttl_handler)

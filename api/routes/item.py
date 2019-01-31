from api.handlers.item import get_handler
from api.handlers.item import post_handler
from api.handlers.item import put_handler
from api.handlers.item import delete_handler
from api.handlers.item import ttl_handler


def init_brand_routes(app):
    app.router.add_route('GET', '/items/{key:\d+}', get_handler)
    app.router.add_route('POST', '/items', post_handler)
    app.router.add_route('PUT', '/items', put_handler)
    app.router.add_route('DELETE', '/items/{key:\d+}', delete_handler)
    app.router.add_route('GET', '/items/ttl/{key:\d+}', ttl_handler)


# TODO: Add tag list keys API
#    - For each new tag will create a new set with key tag_<tag_name>_keys
#    - When a new key is added then we add this to the list
#    - When a key is removed then we remove this one for the set too
#    - When a key is expired or doesn't exist then we remove it from the set too
#    - Create task or cronjob to remove expired keys from sets

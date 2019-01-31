from api.handlers.base import get_base_get
from api.handlers.base import get_base_post
from api.handlers.base import get_base_put
from api.handlers.base import get_base_delete
from api.handlers.base import get_base_ttl
from api.handlers.base import get_404_response
from api.model.item import ItemDB


def get_400_response(msg='Bad Request'):
    return web.json_response({'message': msg,
                              'data': {},
                              'status': 'unknown'}, status=400)


async def get_tag_response_handler(request, handler):
    obj_tag = request.query.get('tag', None)
    if obj_tag is None:
        return get_400_response('No tag name')
    return await handler(ItemDB, tag_name=obj_tag)(request)


async def get_handler(request):
    return await get_tag_response_handler(request, get_base_get)


async def post_handler(request):
    return await get_tag_response_handler(request, get_base_post)


async def put_handler(request):
    return await get_tag_response_handler(request, get_base_put)


async def delete_handler(request):
    return await get_tag_response_handler(request, get_base_delete)


async def ttl_handler(request):
    return await get_tag_response_handler(request, get_base_ttl)

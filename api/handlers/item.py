from api.handlers.base import get_base_get
from api.handlers.base import get_base_post
from api.handlers.base import get_base_put
from api.handlers.base import get_base_delete
from api.handlers.base import get_404_response
from api.model.item import ItemDB


async def get_handler(request):
    return await get_base_get(ItemDB)(request)


async def post_handler(request):
    return await get_base_post(ItemDB)(request)


async def put_handler(request):
    return await get_base_put(ItemDB)(request)


async def delete_handler(request):
    return await get_base_delete(ItemDB)(request)


async def ttl_handler(request):
    obj_key = request.match_info.get('key')
    if obj_key is not None:
        model_db = DBModel(request.app)
        ttl = await model_db.ttl(obj_key)
        return web.json_response({'message': 'All OK',
                                  'data': {'ttl': ttl},
                                  'status': 'success'}, status=200)
    return get_404_response()

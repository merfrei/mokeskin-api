from aiohttp import web


def get_404_response():
    return web.json_response({'message': 'Not found',
                              'data': {},
                              'status': 'unknown'}, status=404)


def get_base_get(DBModel, *args, **kwargs):
    async def get_handler(request):
        obj_key = request.match_info.get('key', None)
        model_db = DBModel(request.app, *args, **kwargs)
        obj_db = await model_db.get(obj_key)
        if obj_db is None:
            return get_404_response()
        return web.json_response({'message': 'All OK',
                                  'data': obj_db,
                                  'status': 'success'}, status=200)
    return get_handler


def get_base_post(DBModel, *args, **kwargs):
    async def post_handler(request):
        model_db = DBModel(request.app, *args, **kwargs)
        params = await request.json()
        if params:
            obj_key = params['key']
            obj_data = params['data']
            obj_exp = params.get('exp', None)
            db_key = await model_db.insert(obj_key, obj_data, obj_exp)
            return web.json_response({'message': 'All OK',
                                      'data': {'key': db_key},
                                      'status': 'success'}, status=201)
        return get_404_response()
    return post_handler


def get_base_put(DBModel, *args, **kwargs):
    async def put_handler(request):
        model_db = DBModel(request.app, *args, **kwargs)
        params = await request.json()
        if params:
            obj_key = params['key']
            obj_data = params['data']
            obj_exp = params.get('exp', None)
            obj_db = await model_db.update(obj_key, obj_data, obj_exp)
            return web.json_response({'message': 'All OK',
                                      'data': obj_db,
                                      'status': 'success'}, status=200)
        return get_404_response()
    return put_handler


def get_base_delete(DBModel, *args, **kwargs):
    async def delete_handler(request):
        obj_key = request.match_info.get('key', None)
        if obj_key is not None:
            model_db = DBModel(request.app, *args, **kwargs)
            await model_db.delete(obj_key)
            return web.json_response({'message': 'All OK',
                                      'data': {},
                                      'status': 'success'}, status=200)
        return get_404_response()
    return delete_handler


def get_base_ttl(DBModel, *args, **kwargs):
    async def ttl_handler(request):
        obj_key = request.match_info.get('key', None)
        if obj_key is not None:
            model_db = DBModel(request.app, *args, **kwargs)
            ttl = await model_db.ttl(obj_key)
            return web.json_response({'message': 'All OK',
                                      'data': {'ttl': ttl},
                                      'status': 'success'}, status=200)
        return get_404_response()
    return ttl_handler

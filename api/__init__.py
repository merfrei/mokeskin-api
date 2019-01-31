import aioredis
from aiohttp import web
from api.config import get_config
from api.routes import init_routes
from api.auth import apikey_middleware


async def init_app(loop):
    config = get_config()

    if config['TESTING']:
        app = web.Application()
    else:
        # Auth enabled
        app = web.Application(middlewares=[apikey_middleware])
        app['api_key'] = config['API_KEY']
    # Create a database connection pool
    app['pool'] = await aioredis.create_redis_pool(
        config['DATABASE_URI'],
        minsize=config['DATABASE_POOL_MIN'],
        maxsize=config['DATABASE_POOL_MAX'],
        loop=loop)

    init_routes(app)

    return app

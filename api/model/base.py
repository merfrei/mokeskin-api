"""DBModel
It's a simple model to use with Redis.
It manages any object coding the same as JSON."""


import json


class DBModelError(Exception):
    pass


class DBModel:

    exception_cls = DBModelError

    def __init__(self, app):
        self._app = app
        self.redis = app['pool']

    def _get_key(self, key):
        """
        It allows to have a custom key generator.

        @type key: string
        @param key: the main key

        @rtype: string
        @return: Returns the key used in the DB
        """
        return key

    async def exists(self, key):
        """
        Check if the key exists in DB

        @type key: string
        @param key: The key which identifies the object in DB

        @rtype: bool
        @return: Returns True or False
        """
        item_key = self._get_key(key)
        result = await self.redis.exists(item_key)
        if result == 0:
            return False
        return True

    async def get(self, key):
        """
        Get the object data by key

        @type key: string
        @param key: The key which identifies the object in DB

        @rtype: dict
        @return: Returns the object stored in the DB
        """
        item_key = self._get_key(key)
        object_json = await self.redis.get(item_key)
        if object_json is not None:
            object_item = json.loads(object_json)
            object_item['_key'] = item_key
            return object_item
        return None

    async def insert(self, key, item, exp=None):
        """
        Insert a new key -> value object

        @type key: string
        @param key: The key which identifies the object in DB

        @type item: dict
        @param item: the object to be stored in DB, it will be coded to JSON

        @type exp: int
        @param exp: expiration time (optional)

        @rtype: string
        @return: item key
        """
        item_key = self._get_key(key)
        object_json = json.dumps(item)
        if exp is not None:
            exp = int(exp)
        await self.redis.set(item_key, object_json, expire=exp)
        return item_key

    async def update(self, key, item, exp=None):
        """
        Update the data in the DB

        @type key: string
        @param key: The key which identifies the object in DB

        @type item: dict
        @param item: the object with the data to be updated in the DB

        @type exp: int
        @param exp: expiration time (optional)

        @rtype: dict
        @return: Returns the updated object stored in the DB
        """
        object_json = await self.get(key)
        if object_json is None:
            raise self.exception_cls('UPDATE ERROR: item does not exist {}'
                                     .format(self._get_key(key)))
        object_json.update(item)
        await self.insert(key, object_json, exp)
        object_json['_key'] = self._get_key(key)
        return object_json

    async def delete(self, key):
        """
        Delete the data in the DB

        @type key: string
        @param key: The key which identifies the object to be deleted in the DB
        """
        item_key = self._get_key(key)
        await self.redis.delete(item_key)

    async def ttl(self, key):
        """
        Returns the number of seconds until the object will expire

        @type key: string
        @param key: The key which identifies the object in DB

        @rtype: int
        @return: Returns the number of seconds left
        """
        item_key = self._get_key(key)
        return await self.redis.ttl(item_key)

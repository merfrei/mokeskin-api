from api.model.base import DBModel
from api.model.base import DBModelError


class ItemDBError(DBModelError):
    pass


class ItemDB(DBModel):

    exception_cls = ItemDBError

    def __init__(self, app, tag_name):
        self.tag_name = tag_name  # It identifies the item, easy to filter
        super().__init__(app)

    def _get_key(self, key):
        return '{}-{}'.format(self.tag_name, key)

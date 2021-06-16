from .database import Database
from .builder import Builder

class UpdateBuilder(Builder):
    
    def __init__(self, db_params):
        Builder.__init__(self)
        self._db = Database(db_params['host'], db_params['user'], db_params['password'], db_params['db'])


    def update(self):
        self._query += f"update"
        return self

    def set_values(self, fields):
        self._query += f' set {",".join([f"{field}=%s" for field in fields])}'
        return self    
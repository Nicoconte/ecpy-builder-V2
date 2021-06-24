from .builder import Builder
from .database import Database

class DeleteBuilder(Builder):

    def __init__(self, db_params):
        Builder.__init__(self)
        self._db = Database(db_params['host'], db_params['user'], db_params['password'], db_params['db'])
    
    def delete(self):
        self._query += f"delete from"
        return self

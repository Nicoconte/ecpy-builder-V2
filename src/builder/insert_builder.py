from .builder import Builder
from .database import Database

class InsertBuilder(Builder):
    
    def __init__(self, db_params):
        Builder.__init__(self)
        self._db = Database(db_params['host'], db_params['user'], db_params['password'], db_params['db'])
        
    def insert(self):
        self._query += f"insert into"
        return self

    def into(self, fields):
        self._query += f" values ({','.join(['%s' for i in range(len(fields))]) })"
        return self


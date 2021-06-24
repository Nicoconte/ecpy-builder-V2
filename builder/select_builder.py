from .builder import Builder
from .database import Database
from .utils import Utils

class SelectBuilder(Builder):
    
    def __init__(self, db_params):
        Builder.__init__(self)
        self._db = Database(db_params['host'], db_params['user'], db_params['password'], db_params['db'])

    def select(self):
        self._query += f"select"
        return self

    def fields_from(self, fields):
        self._table_fields = fields
        self._query += f" {','.join(fields)} from"
        return self

    def all(self):
        self._query += " * from" 
        return self
    
    def inner_join(self, another_table):
        self._query += f" inner join {another_table}"
        return self

    def on(self, relation):
        self._query += f" on {relation}"
        return self

    def count(self, field):
        self._query += f" count({field}) from"
        return self

    def avg(self, field):
        self._query += f" avg({field}) from"
        return self

    def sum(self, field):
        self._query += f" sum({field}) from"
        return self

    def like(self, field, pattern):
        self._query += f" {field} like '{pattern}'"
        return self

    def to_list(self):
        return list(self._response) 

    def to_dict(self):
        try:
            return [Utils.get_dict(self._table_fields, res) for res in self._response]
        except:
            return Utils.get_dict(self._table_fields, self._response)

    def first(self):
        return list(self._response)[0]

    def first_dict(self):
        return [Utils.get_dict(self._table_fields, res) for res in self._response][0]
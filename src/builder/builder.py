import mysql.connector
import logging 

class Builder:

    def __init__(self):
        self._query = ""
        self._values = None
        self._table_fields = None
        self._response = None

        self._connector = None
        self._cursor = None
        self._db = None

    def table(self, table: str):
        self._query += f" {table}"
        return self

    def where(self, condition: str =""):
        self._query += f" where {condition}"
        return self

    def bind(self, values):
        self._values = tuple(values)
        return self

    def and_also(self, and_condition=""):
        self._query += f" and {and_condition}"
        return self    

    def or_also(self, or_condition=""):
        self._query += f" or {or_condition}"
        return self

    def order_by(self, field, order_type):
        self._query += f" order by {field} {order_type}"
        return self

    def is_null(self):
        self._query += " is null"
        return self
    
    def is_not_null(self):
        self._query += " is not null"
        return self

    def debug(self):
        print(self._query)
        return self
    
    def reset(self):
        self._query = ""
        return self

    def exec(self):
        try:
            self._connector = self._db.set_connection()
            self._cursor    = self._connector.cursor(prepared=True)

            self._cursor.execute(
                self._query, self._values
            )

            self._connector.commit()

            return self._cursor.rowcount > 0

        except mysql.connector.Error as error:
            logging.error(f"{ error }")

        finally:
            self.reset()
            self._db.close_connection(self._cursor, self._connector)

        return False

    def get(self):
        try:
            self._connector = self._db.set_connection()
            self._cursor    = self._connector.cursor(buffered=True)

            self._cursor.execute(self._query, self._values)

            self._connector.commit()

            if self._cursor.rowcount == 1:
                self._response = self._cursor.fetchone()

            else:
                self._response = self._cursor.fetchall()

            if self._response == None:
                raise Exception('There no result')
            
            return self
            
        except mysql.connector.Error as error:
            logging.error(f"{ error }")
        
        finally:
            self.reset()
            self._db.close_connection(self._cursor, self._connector)

        return self
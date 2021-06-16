import mysql.connector

class Database:
    def __init__(self, host, user, password, db):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__db = db
        
        self.__connection = None
    
    def set_connection(self):
        self.__connection = mysql.connector.connect(
            host=self.__host,
            user=self.__user,
            password=self.__password,
            database=self.__db
        )

        return self.__connection

    def close_connection(self, cursor, connector):
        if cursor == None and connector == None:
            return 
            
        if connector.is_connected():
            connector.close()
            cursor.close()
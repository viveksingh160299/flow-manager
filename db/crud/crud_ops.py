from db.connection import postgresConnection
from psycopg2 import sql, Error

class crudOps(postgresConnection):

    def __init__(self):
        super().__init__()
        crudOps.getPgConnObj(self.cursor, self.conn)


    @classmethod
    def getPgConnObj(cls, cursor, conn):  
        cls.cursor = cursor
        cls.conn = conn

    
    @classmethod
    def fetch(cls, query, table, parameters):
        try:
            cls.cursor.execute(sql.SQL(query).format(table=sql.Identifier(table)), parameters)
            
            results = cls.cursor.fetchall()

            if(len(results) != 0):
                return results[0][0]
            else:
                raise Exception

        except Exception as err:
            print("Fetch failed due to some error")  
            cls.conn.rollback()

    
    @classmethod
    def update(cls, query, table, parameters):
        try:
            cls.cursor.execute(sql.SQL(query).format(table=sql.Identifier(table)), parameters)
            cls.conn.commit()

        except Exception as err:
            print("Update failed due to some error")  
            cls.conn.rollback()
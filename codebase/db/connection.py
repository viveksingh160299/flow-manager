import psycopg2
# import config
import os

database = os.environ.get("DATABASE") 
user = os.environ.get("USER")
password = os.environ.get("PASSWORD")
host = os.environ.get("HOST")
port = os.environ.get("PORT")

class postgresConnection:

    def __init__(self):
        self.conn = None
        self.cursor = None
        self.connection()
    
    def connection(self):
        try:
            self.conn = psycopg2.connect(
                    dbname=database,
                    user=user,
                    password=password,
                    host=host,
                    port=port                
            )

            self.cursor = self.conn.cursor()
        
        except (Exception, psycopg2.DatabaseError) as error:
            print("Failed to connect DB. Run in debug mode to know the exact issue!")


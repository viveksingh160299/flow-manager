import psycopg2
import config

class postgresConnection:

    def __init__(self):
        self.conn = None
        self.cursor = None
        self.connection()
    
    def connection(self):
        try:
            self.conn = psycopg2.connect(
                    dbname=config.database,
                    user=config.user,
                    password=config.password,
                    host=config.host,
                    port=config.port                
            )

            self.cursor = self.conn.cursor()
        
        except (Exception, psycopg2.DatabaseError) as error:
            print("Failed to connect DB. Run in debug mode to know the exact issue!")


import psycopg2

# Database connection parameters

host = "localhost"
database= "flow_manager_db"
user="postgres"
password="postgres"
port= "5432" 



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


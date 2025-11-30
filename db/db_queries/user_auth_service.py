from db.crud.crud_ops import crudOps
from exception import dbException

class userAuthService:

    def __init__(self):
        self.table_name = "user_auth"

    def getUserAndPasswordHash(self, email):
        query = '''SELECT user_id, password_hash FROM {table} WHERE email=%s'''

        results  = crudOps.fetch(query, self.table_name, (email,))

        if(len(results) == 0):
            raise dbException("User does not exist! Please Sign In.")

        return results[0][0], results[0][1]

from werkzeug.security import check_password_hash
import jwt
from db.db_queries.user_auth_service import userAuthService
import config
from datetime import datetime, timezone, timedelta
from exception import authException

class generateAuthToken:

    def __init__(self):
        self.user_id = None


    def getUserPasswordHash(self, email):
        self.user_id, password_hash = userAuthService().getUserAndPasswordHash(email)

        return password_hash


    def validateUserAndGenerateToken(self, email, password):
        password_hash = self.getUserPasswordHash(email)

        if(not check_password_hash(password_hash, password)):
            raise authException("Incorrect email or password! Please use correct credentials.")

        auth_token = jwt.encode({'user_id': self.user_id, 
                                 'exp': datetime.now(timezone.utc) + timedelta(minutes=30)},
                                 config.auth_secret,
                                 algorithm="HS256") 
                  
        return auth_token

import jwt
import config
from exception import authException
from functools import wraps
from flask import request, Response



def token_required(func):
    @wraps(func)
    def decorated():
        try: 
            headers = request.headers
            bearer = headers.get('Authorization')

            if(bearer is None):
                raise authException("bearer is missing in header!")
            
            if(not (bearer.startswith('Bearer '))):
                raise authException("bearer format is incorrect!")

            auth_token = bearer.split()[1]

            if(len(auth_token) == 0):
                raise authException("Auth token is missing! Please login again.")

            data = jwt.decode(auth_token, config.auth_secret, algorithms=["HS256"])

            return func(data['user_id'])

        except authException as err:
            # traceback.print_exc()
            # print(err)
            
            return Response(response=str(err.message), status=401, mimetype='application/json')
        
        except Exception as err:
            # traceback.print_exc()
            # print(err)
            
            return Response(response="Invalid token!", status=401, mimetype='application/json')
    

    return decorated
        
        
        

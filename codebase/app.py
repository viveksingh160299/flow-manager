from db.crud import crud_ops
from flask import Flask, request, Response
from flow_manager.flow_manager import flowManager
import traceback
from exception import dbException, flowManagerException, authException
from jwt_auth.authenticate import generateAuthToken
from jwt_auth.token_validation import token_required


# Create flask instance
app = Flask(__name__)

# Establish DB connection
crud_ops.crudOps()




@app.route('/flow-manager', methods=['POST'])
@token_required
def flowOperation(user_id):
    try:
        input = request.get_json()
        
        flow_manager_instance = flowManager(input)
        flow_manager_instance.startSequentialTaskProcessing(user_id)

        return Response(response='Task completed successfully!', status=200, mimetype='application/json')

    except (dbException, flowManagerException) as err:
        # traceback.print_exc()
        # print(err)

        return Response(response=str(err.message), status=400, mimetype='application/json')
    
    except Exception as err:
        # traceback.print_exc()
        # print(err)
        
        return Response(response='Internal Server Error!', status=500, mimetype='application/json')





@app.route('/login', methods=['POST'])
def loginUser():
    try:
        input = request.get_json()

        auth_token = generateAuthToken().validateUserAndGenerateToken(input['email'], input['password'])

        return Response(response=auth_token, status=200, mimetype='application/json')

    except authException as err:
        # traceback.print_exc()
        # print(err)

        return Response(response=str(err.message), status=400, mimetype='application/json')
    
    except Exception as err:
        # traceback.print_exc()
        # print(err)
        
        return Response(response='Internal Server Error!', status=500, mimetype='application/json')







if __name__ == "__main__":

    app.run(host='0.0.0.0', port=8080, debug=True)
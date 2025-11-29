from db.crud import crud_ops
from flask import Flask, request, Response
from flow_manager.flow_manager import flowManager
import traceback
from exception import dbException, flowManagerException


# Create flask instance
app = Flask(__name__)

@app.route('/flow-manager', methods=['POST'])
def flowOperation():
    try:
        input = request.get_json()

        flow_manager_instance = flowManager(input)
        flow_manager_instance.startSequentialTaskProcessing("user_1256")

        return Response(response='Task completed successfully!', status=200, mimetype='application/json')

    except (dbException, flowManagerException) as err:
        # traceback.print_exc()
        # print(err)

        return Response(response=str(err.message), status=400, mimetype='application/json')
    
    except Exception as err:
        # traceback.print_exc()
        # print(err)
        
        return Response(response='Internal Server Error!', status=500, mimetype='application/json')




if __name__ == "__main__":

    # Establish DB connection
    crud_ops.crudOps()

    app.run(host='0.0.0.0', port=8080, debug=True)
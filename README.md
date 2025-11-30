### Flow Manager API :-
The flow manager Api is designed to run tasks in sequential fashion. This is controlled by the flow manager handler. 


### Key Highlights about the Api:
1: The Flow Manager Api is developed using python, flask and postgreSQL.
2: There are 2 api endpoints: /login endpoint is needed to log user in. /flow-manager is the main endpoint which excutes the task.
3: The /flow-manager api endpoint is protected by JWT authentication.
4: The task class is separate from flow manager classes. The task class implements a abstract class(interface) to ensure generic design. 
5: The generic design of the task classes allows developer to add more tasks and chain them in the api.
6: To prevent sql injection attack, all the queries are parametrized using psycopg2.
7: Extensive use of try except to capture failure scenarios and update the api caller about it by only passing what is required. No internal error stack messeges are returned as Response to api caller to ensure security.
8: A gunicorn web server is added to allow users to make multiple api calls simultaneously.
9: A very simple logging is implemented by guicorn.
10: Everything is Dockerized using Podman. Podman is exactly similar to Docker. It has free usage license. 
11: There are 2 Podman images. One is DB image and other is Flow Manager API image.


### SETUP :- Flow Manager DB container  
Step 1: Navigate inside the root dir of the PostgreSQL DB folder.  
Step 2: Create a DB image by running below commands:  
&emsp;&emsp;> podman build -t flow_manager_db .  
Step 3: Create DB container from the Podman image.  
&emsp;&emsp;> podman run -d -p 7777:5432 <db_image_id>  
Step 4: Ensure DB container is active. Run below command and container should show up in the list.  
&emsp;&emsp;> podman ps  
  
  
### SETUP :- Flow Manager Api container  
Step 1: Do a git clone of the repository. Use the main branch.  
Step 2: In the root directory(root dir has Dockerfile, codebase and requirements.txt) execute below commands to create a Podman Image.  
&emsp;&emsp;> podman build -t flow_manager_api .  
Step 3: Create API container from the Podman image.  
&emsp;&emsp;> podman run -it -p 8080:8080 --tz=local <api_image_id> /bin/bash  
Step 4: You will be inside container. Before starting the api ensure that DB container is up and running.  
Step 5: Now start Gunicorn web server to start the flow manager application.  
&emsp;&emsp;$ cd codebase/  
&emsp;&emsp;$ gunicorn -c gconfig.py wsgi:app &  
&emsp;&emsp;$ tail -100f ./error.log  
Step 6: inside error.log file you'll see 2 gunicorn workers up and running.  
Step 7: Now test the API from Postman.  
  
  
### Testing :- Postman  
Step 1: The Api is protected using Jwt.  
Step 2: Generate token by calling 'http://127.0.0.1:8080/login'. Dummy user is added in the DB. So you'll need email and password.  
Step 3: Add dummy email as "user3784mail@gmail.com" and dummy password as "aFtg&89M" in the Body of the Postman api caller.  
Step 4: input Json for login should look like:  
&emsp;&emsp;{  
&emsp;&emsp;&ensp;"email": "user3784mail@gmail.com",  
&emsp;&emsp;&ensp;"password": "aFtg&89M"  
&emsp;&emsp;}  
Step 5: Copy the token.  
Step 6: Using the above token now you can make api call to the protected endpoint 'http://127.0.0.1:8080/flow-manager'.  
Step 7: add token to Authorization section. Set type to Bearer Token and then paste the token in the Token section.  
Step 8: make the api call using the input json for the flow manager api.  
        

from app import app
import uuid

#use 127.0.0.1:5000/host_id to check
@app.route('/host_id') 
def index(): 
    print(uuid.uuid4())
    return str(uuid.uuid4())
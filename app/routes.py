from app import app
import uuid

@app.route('/host_id') 
def index(): 
    print(uuid.uuid4())
    return str(uuid.uuid4())
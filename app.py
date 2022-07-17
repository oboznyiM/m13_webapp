from flask import Flask, render_template, Response

app = Flask(__name__)
import uuid

#use 127.0.0.1:5000/host_id to check 
@app.route('/host_id') 
def index(): 
    return str(uuid.uuid4())

@app.route('/health')
def health():
    return Response(status=200)
if __name__ == '__main__':
    app.run(host='0.0.0.0')
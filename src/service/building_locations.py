import flask
import os
from flask import abort, request, jsonify, Flask
from flask_cors import CORS

DATA_DIR = os.environ.get('DATA_DIR')
TEST_JSON = 'seattle.json'

app = Flask(__name__)
CORS(app)

@app.route('/buildings', methods=['GET'])
def get_buildings():
    with open(f'{DATA_DIR}{os.sep}{TEST_JSON}','r') as geo_db:
        return geo_db.readline()

if __name__ == '__main__':
    app.run()

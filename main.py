from flask import Flask, jsonify, request
import os
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

db_params = {
    'host': ${{Postgres.PGHOST}},
    'database': ${{Postgres.PGDATABASE}},
    'user': ${{Postgres.PGUSER}}',
    'password': '${{Postgres.PGPASSWORD}}'
}

@app.route('/')
def index():
   return db_params


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))

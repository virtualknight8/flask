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
    # Establish a connection to the database
    conn = psycopg2.connect(**db_params)

    # Create a cursor object to interact with the database
    cur = conn.cursor()

    # Execute the SQL query to retrieve inventory items with category and supplier information
    cur.execute("""SELECT * FROM inventory""")

    # Fetch all rows of the result
    inventory_items = cur.fetchall()

    # Close the cursor and the connection
    cur.close()
    conn.close()

    # Convert the data to a suitable format (e.g., list of dictionaries)
    inventory_data = []
    for item in inventory_items:
        item_data = {
            'id': item[0],
            'item': item[1],
            'price': float(item[2]),
            'quantity': item[3]
        }
        inventory_data.append(item_data)

    # Return the inventory data as JSON response
    return jsonify(inventory_data)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))

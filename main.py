from flask import Flask, jsonify, request
import os


app = Flask(__name__)
print('kuch bhi')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))

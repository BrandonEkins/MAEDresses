#/bin/python
from flask import Flask, jsonify
import MySQLdb
def queryDB(nQuery):
    db = MySQLdb.connect(host="localhost",
                        user="root",
                        passwd="",
                        db="MAEDresses")
    cur = db.cursor()
    cur.execute(nQuery)
    result = cur.fetchall()
    db.close()
    return result
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/address', methods=['GET'])
def get_address():
    return jsonify(queryDB("SELECT * FROM Address"))

@app.route('/api/cart', methods=['GET'])
def get_cart():
    return "cart"

if __name__ == '__main__':
    app.run(debug=True)

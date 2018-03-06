#/bin/python
from flask import Flask, jsonify, request, abort, render_template,send_from_directory
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
    return render_template('index.html')
task_id = ''

@app.route('/static/<path:path>')
def controller(path):
    return send_from_directory('js', path)

@app.route('/static/<path:path>')
def style(path):
    return send_from_directory('css', path)
##REST for Address table

@app.route('/api/address', methods=['GET'])
def get_address():
    return jsonify(queryDB("SELECT * FROM Address;"))

@app.route('/api/address', methods=['POST'])
def post_address():
    if not request.json or not 'title' in request.json:
        abort(400)
    result = queryDB("INSERT INTO address (`AddressID`, `Street`, `City`, `aState`, `Zip`) VALUES ("+ request.json[0]+', '+ request.json[1]+', '+ request.json[2]+', '+ request.json[3]+');')
    return jsonify(result), 201

@app.route('/api/address/<int:task_id>', methods=['PUT'])
def put_address():
    result = queryDB("UPDATE address SET Street="+request.json[0]+", City="+request.json[1]+", aState="+request.json[2]+", zip="+request.json[3]+" WHERE AddressID = "+task_id+";")
    return jsonify(result), 201

@app.route('/api/address/<int:task_id>', methods=['DELETE'])
def delete_task():
    result = queryDB('DELETE FROM Address WHERE AddressID = '+ task_id +';')
    return jsonify(result), 201



if __name__ == '__main__':
    app.run(debug=True)

#/bin/python
from flask import Flask, jsonify, Response, request, abort, render_template,send_from_directory
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

@app.route('/api/address', methods=['GET', 'POST'])
def api():
    if request.method == 'GET':
        return jsonify(queryDB("SELECT * FROM Address;"))
    elif request.method == 'POST':
        data = request.get_json(force=True)
        print data
        query = "INSERT INTO address (`AddressID`,`Street`, `City`, `aState`, `Zip`) VALUES ("+str(data['id'])+",'"+ data['Street']+"', '"+ data['City']+"', '"+ data['aState']+"', "+ data['Zip']+");"
        print query
        result = queryDB(query)
        return jsonify(result), 201

@app.route('/api/address', methods=[ 'PUT', 'DELETE'])
def addressput():
    if request.method == 'PUT':
        result = queryDB("UPDATE address SET Street="+request.json[0]+", City="+request.json[1]+", aState="+request.json[2]+", zip="+request.json[3]+" WHERE AddressID = "+task_id+";")
        return jsonify(result.json), 201
    elif request.method == 'DELETE':
        result = queryDB('DELETE FROM Address WHERE AddressID = '+ task_id +';')
        return jsonify(result), 201

if __name__ == '__main__':
    app.run(debug=True)

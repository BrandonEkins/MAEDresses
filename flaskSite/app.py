#/bin/python
from flask import Flask, jsonify, Response, request, abort, render_template, send_from_directory
import MySQLdb
def queryDB(nQuery):
    db = MySQLdb.connect(host="localhost",
                        user="root",
                        passwd="",
                        db="MAEDresses")
    cur = db.cursor()
    print nQuery
    cur.execute(nQuery)
    db.commit()
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

#region AddressApi
@app.route('/api/address', methods=['GET', 'POST'])
def addressget():
    if request.method == 'GET':
        return jsonify(queryDB("SELECT * FROM Address;"))
    elif request.method == 'POST':
        data = request.get_json(force=True)
        query = "INSERT INTO address (`AddressID`,`Street`, `City`, `aState`, `Zip`) VALUES ("+str(data['id'])+",'"+ data['Street']+"', '"+ data['City']+"', '"+ data['aState']+"', "+ data['Zip']+");"
        result = queryDB(query)
        return jsonify(result), 201

@app.route('/api/address/<int:task_id>', methods=[ 'PUT', 'DELETE'])
def addressput(task_id):
    if request.method == 'PUT':
        data = request.get_json(force=True)
        result = queryDB("UPDATE address SET Street='"+data['Street']+"', City='"+data['City']+"', aState='"+data['aState']+"', Zip='"+data['Zip']+"' WHERE AddressID= "+str(task_id)+";")
        return jsonify(result), 201

    elif request.method == 'DELETE':
        result = queryDB("DELETE FROM Address WHERE AddressID = '"+ str(task_id) +"';")
        return jsonify(result), 201
#endregion
#region BillingApi
@app.route('/api/billinginformation', methods=['GET', 'POST'])
def billingget():
    if request.method == 'GET':
        return jsonify(queryDB("SELECT * FROM billinginformation;"))
    elif request.method == 'POST':
        data = request.get_json(force=True)
        query = "INSERT INTO billinginformation (`BillingInformationID`,`CreditCardNumber`, `ExpirationDate`, `AddressID`) VALUES ("+str(data['id'])+",'"+ data['CreditCardNumber']+"', '"+ data['ExpirationDate']+"', '"+ data['AddressID']+"');"
        result = queryDB(query)
        return jsonify(result), 201

@app.route('/api/billinginformation/<int:task_id>', methods=[ 'PUT', 'DELETE'])
def billingput(task_id):
    if request.method == 'PUT':
        data = request.get_json(force=True)
        result = queryDB("UPDATE billinginformation SET CreditCardNumber='"+data['CreditCardNumber']+"', ExpirationDate='"+data['ExpirationDate']+"', AddressID='"+data['AddressID']+"' WHERE BillingInformationID= '"+str(task_id)+"';")
        return jsonify(result), 201

    elif request.method == 'DELETE':
        result = queryDB("DELETE FROM billinginformation WHERE BillingInformationID = '"+ str(task_id) +"';")
        return jsonify(result), 201
#endregion
#region CartApi
@app.route('/api/cart', methods=['GET', 'POST'])
def cartget():
    if request.method == 'GET':
        return jsonify(queryDB("SELECT * FROM Cart;"))
    elif request.method == 'POST':
        data = request.get_json(force=True)
        query = "INSERT INTO Cart (`CartID`,`NumberOfItems`, `TotalCost`, `ShippingCost`, `CustomerID`) VALUES ("+str(data['id'])+",'"+ data['NumberOfItems']+"','"+ data['TotalCost']+"', '"+ data['ShippingCost']+"','"+ data['CustomerID']+"');"
        result = queryDB(query)
        return jsonify(result), 201

@app.route('/api/cart/<int:task_id>', methods=[ 'PUT', 'DELETE'])
def cartput(task_id):
    if request.method == 'PUT':
        data = request.get_json(force=True)
        result = queryDB("UPDATE Cart SET NumberOfItems='"+data['NumberOfItems']+"', TotalCost='"+data['TotalCost']+"', ShippingCost='"+data['ShippingCost']+"', CustomerID='"+data['CustomerID']+"' WHERE CartID= '"+str(task_id)+"';")
        return jsonify(result), 201

    elif request.method == 'DELETE':
        result = queryDB("DELETE FROM Cart WHERE CartID = '"+ str(task_id) +"';")
        return jsonify(result), 201
#endregion
#region CartedProductApi
@app.route('/api/cartedproduct', methods=['GET', 'POST'])
def CartedProductget():
    if request.method == 'GET':
        return jsonify(queryDB("SELECT * FROM cartedproduct;"))
    elif request.method == 'POST':
        data = request.get_json(force=True)
        query = "INSERT INTO cartedproduct (`cartedproductID`,`ProductID`, `CartID`) VALUES ("+str(data['id'])+",'"+ data['ProductID']+"', '"+ data['CartID']+"');"
        result = queryDB(query)
        return jsonify(result), 201

@app.route('/api/cartedproduct/<int:task_id>', methods=[ 'PUT', 'DELETE'])
def CartedProductput(task_id):
    if request.method == 'PUT':
        data = request.get_json(force=True)
        result = queryDB("UPDATE cartedproduct SET ProductID='"+data['ProductID']+"', CartID='"+data['CartID']+"' WHERE cartedProductID = '"+str(task_id)+"';")
        return jsonify(result), 201

    elif request.method == 'DELETE':
        result = queryDB("DELETE FROM cartedproduct WHERE cartedproductID = '"+ str(task_id) +"';")
        return jsonify(result), 201
#endregion
#region customerApi
@app.route('/api/customer', methods=['GET', 'POST'])
def customerget():
    if request.method == 'GET':
        return jsonify(queryDB("SELECT * FROM customer;"))
    elif request.method == 'POST':
        data = request.get_json(force=True)
        query = "INSERT INTO customer (`customerID`,`Email`, `cName`, `Pass`,`AddressID`,`BillingInformationID`) VALUES ("+str(data['id'])+",'"+ data['Email']+"','"+ data['cName']+"','"+ data['Pass']+"', '"+ data['AddressID']+"', '"+ data['BillingInformationID']+"');"
        result = queryDB(query)
        return jsonify(result), 201

@app.route('/api/customer/<int:task_id>', methods=[ 'PUT', 'DELETE'])
def customerput(task_id):
    if request.method == 'PUT':
        data = request.get_json(force=True)
        result = queryDB("UPDATE customer SET Email='"+data['Email']+"', cName='"+data['cName']+"', AddressID='"+data['AddressID']+"', BillingInformationID='"+data['BillingInformationID']+"' WHERE customerID= '"+str(task_id)+"';")
        return jsonify(result), 201

    elif request.method == 'DELETE':
        result = queryDB("DELETE FROM customer WHERE customerID = '"+ str(task_id) +"';")
        return jsonify(result), 201
#endregion

if __name__ == '__main__':
    app.run(debug=True)

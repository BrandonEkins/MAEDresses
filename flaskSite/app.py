#/bin/python
from flask import Flask, jsonify, Response, request, abort, render_template, send_from_directory
import MySQLdb
import auth
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
@auth.requires_auth
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
        return jsonify(queryDB("SELECT * FROM BillingInformation;"))
    elif request.method == 'POST':
        data = request.get_json(force=True)
        query = "INSERT INTO BillingInformation (`BillingInformationID`,`CreditCardNumber`, `ExpirationDate`, `AddressID`) VALUES ("+str(data['id'])+",'"+ data['CreditCardNumber']+"', '"+ data['ExpirationDate']+"', '"+ data['AddressID']+"');"
        result = queryDB(query)
        return jsonify(result), 201

@app.route('/api/billinginformation/<int:task_id>', methods=[ 'PUT', 'DELETE'])
def billingput(task_id):
    if request.method == 'PUT':
        data = request.get_json(force=True)
        result = queryDB("UPDATE BillingInformation SET CreditCardNumber='"+data['CreditCardNumber']+"', ExpirationDate='"+data['ExpirationDate']+"', AddressID='"+data['AddressID']+"' WHERE BillingInformationID= '"+str(task_id)+"';")
        return jsonify(result), 201

    elif request.method == 'DELETE':
        result = queryDB("DELETE FROM BillingInformation WHERE BillingInformationID = '"+ str(task_id) +"';")
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
        return jsonify(queryDB("SELECT * FROM Customer;"))
    elif request.method == 'POST':
        data = request.get_json(force=True)
        query = "INSERT INTO Customer (`customerID`,`Email`, `cName`, `Pass`,`AddressID`,`BillingInformationID`) VALUES ("+str(data['id'])+",'"+ data['Email']+"','"+ data['cName']+"','"+ data['Pass']+"', '"+ data['AddressID']+"', '"+ data['BillingInformationID']+"');"
        result = queryDB(query)
        return jsonify(result), 201

@app.route('/api/customer/<int:task_id>', methods=[ 'PUT', 'DELETE'])
def customerput(task_id):
    if request.method == 'PUT':
        data = request.get_json(force=True)
        result = queryDB("UPDATE Customer SET Email='"+data['Email']+"', cName='"+data['cName']+"', AddressID='"+data['AddressID']+"', BillingInformationID='"+data['BillingInformationID']+"' WHERE customerID= '"+str(task_id)+"';")
        return jsonify(result), 201

    elif request.method == 'DELETE':
        result = queryDB("DELETE FROM Customer WHERE customerID = '"+ str(task_id) +"';")
        return jsonify(result), 201
#endregion
#region neworderApi
@app.route('/api/neworder', methods=['GET', 'POST'])
def neworderget():
    if request.method == 'GET':
        return jsonify(queryDB("SELECT * FROM neworder;"))
    elif request.method == 'POST':
        data = request.get_json(force=True)
        query = "INSERT INTO neworder (`neworderID`,`CartID`, `StaffID`, `OrderDate`) VALUES ("+str(data['id'])+",'"+ data['CartID']+"','"+ data['StaffID']+"','"+ data['OrderDate']+"');"
        result = queryDB(query)
        return jsonify(result), 201

@app.route('/api/neworder/<int:task_id>', methods=[ 'PUT', 'DELETE'])
def neworderput(task_id):
    if request.method == 'PUT':
        data = request.get_json(force=True)
        result = queryDB("UPDATE neworder SET CartID='"+data['CartID']+"', StaffID='"+data['StaffID']+"', OrderDate='"+data['OrderDate']+"' WHERE neworderID= '"+str(task_id)+"';")
        return jsonify(result), 201

    elif request.method == 'DELETE':
        result = queryDB("DELETE FROM neworder WHERE neworderID = '"+ str(task_id) +"';")
        return jsonify(result), 201
#endregion
#region productApi
@app.route('/api/product', methods=['GET', 'POST'])
def productget():
    if request.method == 'GET':
        return jsonify(queryDB("SELECT * FROM Product;"))
    elif request.method == 'POST':
        data = request.get_json(force=True)
        query = "INSERT INTO Product (`productID`,`ShippingCost`, `ProductName`, `Color`,`Price`,`WholesalerID`) VALUES ("+str(data['id'])+",'"+ data['ShippingCost']+"','"+ data['Color']+"','"+ data['ProductName']+"', '"+ data['Price']+"', '"+ data['WholesalerID']+"');"
        result = queryDB(query)
        return jsonify(result), 201

@app.route('/api/product/<int:task_id>', methods=[ 'PUT', 'DELETE'])
def productput(task_id):
    if request.method == 'PUT':
        data = request.get_json(force=True)
        result = queryDB("UPDATE Product SET ShippingCost='"+data['ShippingCost']+"', ProductName='"+data['ProductName']+"', Color='"+data['Color']+"', Price='"+data['Price']+"', WholesalerID='"+data['WholesalerID']+"' WHERE productID= '"+str(task_id)+"';")
        return jsonify(result), 201

    elif request.method == 'DELETE':
        result = queryDB("DELETE FROM Product WHERE productID = '"+ str(task_id) +"';")
        return jsonify(result), 201
#endregion
#region staffApi
@app.route('/api/staff', methods=['GET', 'POST'])
def staffget():
    if request.method == 'GET':
        return jsonify(queryDB("SELECT * FROM staff;"))
    elif request.method == 'POST':
        data = request.get_json(force=True)
        query = "INSERT INTO staff (`staffID`,`StaffName`, `Email`, `Wage`, `sPassword`) VALUES ("+str(data['id'])+",'"+ data['StaffName']+"', '"+ data['Email']+"', '"+ data['Wage']+"', '"+ data['sPassword']+"');"
        result = queryDB(query)
        return jsonify(result), 201

@app.route('/api/staff/<int:task_id>', methods=[ 'PUT', 'DELETE'])
def staffput(task_id):
    if request.method == 'PUT':
        data = request.get_json(force=True)
        result = queryDB("UPDATE staff SET StaffName='"+data['StaffName']+"', Email='"+data['Email']+"', Wage='"+data['Wage']+"', sPassword='"+data['sPassword']+"' WHERE staffID= "+str(task_id)+";")
        return jsonify(result), 201

    elif request.method == 'DELETE':
        result = queryDB("DELETE FROM staff WHERE staffID = '"+ str(task_id) +"';")
        return jsonify(result), 201
#endregion
#region wholesalerApi
@app.route('/api/wholesaler', methods=['GET', 'POST'])
def wholesalerget():
    if request.method == 'GET':
        return jsonify(queryDB("SELECT * FROM Wholesaler;"))
    elif request.method == 'POST':
        data = request.get_json(force=True)
        query = "INSERT INTO Wholesaler (`wholesalerID`,`Website`, `WholesalerName`, `WholesalerPhone`, `WholesalerLocation`) VALUES ("+str(data['id'])+",'"+ data['Website']+"', '"+ data['WholesalerName']+"', '"+ data['WholesalerPhone']+"', '"+ data['WholesalerLocation']+"');"
        result = queryDB(query)
        return jsonify(result), 201

@app.route('/api/wholesaler/<int:task_id>', methods=[ 'PUT', 'DELETE'])
def wholesalerput(task_id):
    if request.method == 'PUT':
        data = request.get_json(force=True)
        result = queryDB("UPDATE Wholesaler SET Website='"+data['Website']+"', WholesalerName='"+data['WholesalerName']+"', WholesalerPhone='"+data['WholesalerPhone']+"', WholesalerLocation='"+data['WholesalerLocation']+"' WHERE wholesalerID= "+str(task_id)+";")
        return jsonify(result), 201

    elif request.method == 'DELETE':
        result = queryDB("DELETE FROM Wholesaler WHERE WholesalerID = '"+ str(task_id) +"';")
        return jsonify(result), 201
#endregion
if __name__ == '__main__':
    app.run(debug=True)

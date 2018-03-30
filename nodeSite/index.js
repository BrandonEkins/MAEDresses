var express = require('express');
var app = express();
var cookieParser = require('cookie-parser')
var bodyParser = require('body-parser')
var database = require('./database')
app.use(cookieParser());
app.use(bodyParser.urlencoded({
    extended: false
}));
app.use(bodyParser.json());
//mysqldatabase
var mysql = require('mysql');
var connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'MAEDresses'
});
connection.connect(function (err) {
    if (!err) {
        console.log("Database is connected ... \n\n");
    } else {
        console.log("Error connecting database ... \n\n");
    }
});

// connection.query('UPDATE users SET foo = ?, bar = ?, baz = ? WHERE id = ?', ['a', 'b', 'c', userId], function (error, results, fields) {
//     if (error) throw error;
//     // ...
// });
//create create check for cookie function that returns the userID
checkCookieDB = function (req) {

}
app.get('/', function (req, res) {
    res.sendFile(__dirname + "/public/" + "index.html");
});
app.get('/todo.js', function (req, res) {
    global.id = 0;
    //res.send("Hello World")
    res.sendFile(__dirname + "/public/" + "todo.js");
});
app.get('/api/getUser', function (req, res) {
    database.mongoCheck(req.cookies.loginToken).then(function (items) {
        if (items != null) {
            userID = items.CustomerID;
            connection.query('SELECT * FROM Customer WHERE CustomerID = ?', [userID], function (error, results, fields) {
                if (error) throw error;
                res.send(JSON.stringify(results));
                // ...
            });
        }
    });
});
app.get('/api/getCart', function (req, res) {
    database.mongoCheck(req.cookies.loginToken).then(function (items) {
        if (items != null) {
            userID = items.CustomerID;
            //create cartView
            //create trigger for cart size
            //select & return cartView
            connection.query('SELECT * FROM CartView WHERE CustomerID = ?', [userID], function (error, results, fields) {
                res.send(JSON.stringify(results));
            });
        }
    });
});
app.post('/api/addCart', function (req, res) {//get list of ID's of products to add
    database.mongoCheck(req.cookies.loginToken).then(function (items) {
        if (items.CustomerID != null) {
            userID = items.CustomerID;
            //use product ID & cartid to add a cartitem
            connection.query('SELECT CartID FROM Cart where CustomerID = ?', [userID], function (error, results, fields) {
                cartID = results[0].CartID;
                connection.query('SELECT * FROM CartedProduct ORDER BY CartedProductID DESC LIMIT 1', function (error, results, fields) {
                    if (error) throw error;
                    if (results.length = 0){
                        cpID = results[0].CartedProductID + 1;
                    }
                    else{
                        cpID = 0;
                    }
                    connection.query('INSERT INTO CartedProduct (CartedProductID, ProductID, CartID) VALUES (?,?,?)', [cpID, req.body.ProductID, cartID], function (error, results, fields) {
                        if (error) throw error;
                        // ...
                    });
                });
                // ...
            });

        }
    });
});
app.post('/api/removeCart', function (req, res) {//get list of ID's of products to add
    database.mongoCheck(req.cookies.loginToken).then(function (items) {
        if (items.CustomerID != null) {
            userID = items.CustomerID;
            //use product ID & cartid to add a cartitem  
            connection.query('DELETE FROM CartedProduct WHERE CartedProductID = ?', [req.body.CartedProductID], function (error, results, fields) {
                if (error) throw error;
                cartID = results;

                // ...
            });
        }
    });
});
// app.get('/api/getBillingInfo', function (req, res) {
//     database.mongoCheck(req.cookies.loginToken).then(function (items) {
//         if (items != null) {
//             userID = items.CustomerID;
//             connection.query('SELECT * FROM BillingInformation WHERE CustomerID = ?', [userID], function (error, results, fields) {
//                 if (results.length = 0){
//                     connection.query('INSERT * FROM BillingInformation WHERE CustomerID = ?', [userID], function (error, results, fields) {
//                         if (results.length = 0){
                            
//                         }
//                         res.send(JSON.stringify(results));
//                     });
//                 }
//                 res.send(JSON.stringify(results));
//             });
//         }
//     });
// });
// app.get('/api/getBillingInfo', function (req, res) {
//     database.mongoCheck(req.cookies.loginToken).then(function (items) {
//         if (items != null) {
//             userID = items.CustomerID;
//             connection.query('UPDATE BillingInformation WHERE CustomerID = ?', [userID], function (error, results, fields) {
//                 res.send(JSON.stringify(results));
//             });
//         }
//     });
// });
app.post('/api/order', function (req, res) {
    //check for cookie
    //change cart into order...
});
app.get('/api/getProducts', function (req, res) {
    var stuff = []
    connection.query('SELECT * FROM Product', function (error, results, fields) {
        if (error) throw error;
        stuff = results;
        res.send(JSON.stringify(stuff));
    });

});
app.post('/login', function (request, res) {
    var cookie = request.cookies.cookieName;
    var randomNumber = Math.random().toString();
    randomNumber = randomNumber.substring(2, randomNumber.length);
    connection.query('SELECT * FROM Customer WHERE Pass = ? and Email = ?', [request.body.password, request.body.email], function (error, results, fields) {
        if (error) throw error;
        if (results[0].pass == request.body.pass) {
            //res.clearCookie('loginToken');
            res.cookie('loginToken', randomNumber, {
                maxAge: 900000,
                httpOnly: true
            });
            var user = { "rand": randomNumber, "CustomerID": results[0].CustomerID,"name":results[0].cName}
            database.mongoAdd(user);
            res.send(JSON.stringify(results[0].cName));
        }
    });
    console.log('logging in');

})
app.get('/logout', function (req, res) {
    var cookie = req.cookies.cookieName;
    database.mongoDelete(cookie);
    res.clearCookie('loginToken');
})
var server = app.listen(8000, function () {
    var host = server.address().address
    var port = server.address().port
    console.log("Example app listening at http://%s:%s", host, port)
})
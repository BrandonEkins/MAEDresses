var express = require('express');
var app = express();
var cookieParser = require('cookie-parser')
var bodyParser = require('body-parser')
app.use(cookieParser());
app.use(bodyParser.urlencoded({
    extended: false
}));
app.use(bodyParser.json());
//database
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
var getCookie = function(cookie) {
    //check mongo for cookie
    //return userID
    //if no cookie return -1
}
app.get('/', function (req, res) {
    res.sendFile(__dirname + "/public/" + "index.html");
});
app.get('/todo.js', function (req, res) {
    //res.send("Hello World")
    res.sendFile(__dirname + "/public/" + "todo.js");
});
app.get('/api/getUser', function (req, res) {
    //check for cookie
    //send user
    res.send(JSON.stringify({"user":'Brandon'}));
});
app.get('/api/getCart', function (req, res) {
    //check for cookie
    //send cart 
});
app.post('/api/addCart', function (req,res){
    //check for cookie
    //replace cart based on cookie (no add or edit just total replace)

});
app.post('/api/order', function (req,res){

});
app.post('api/getProducts', function (req,res){

});
app.post('/login', function (request, res) {
    var cookie = request.cookies.cookieName;
    var randomNumber = Math.random().toString();
    randomNumber = randomNumber.substring(2, randomNumber.length);
    connection.query('SELECT * FROM Customer WHERE Pass = ? and Email = ?', [request.body.password, request.body.email], function (error, results, fields) {
        if (error) throw error;
        if (results[0].password == request.body.password) {
            res.clearCookie('loginToken');
            res.cookie('loginToken', randomNumber, {
                maxAge: 900000,
                httpOnly: true
            });
        }
        // ...
    });
    //add cookie to mongodb

    //console.log('cookie created successfully');
    console.log('logging in');
    //request.redirect('/');
    res.redirect('/');
})
app.get('/logout', function (req, res) {
    var cookie = req.cookies.cookieName;
    res.clearCookie('loginToken');
    //mongo delete session
    res.redirect('/');
})
var server = app.listen(8000, function () {
    var host = server.address().address
    var port = server.address().port
    console.log("Example app listening at http://%s:%s", host, port)
})
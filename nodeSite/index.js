var express = require('express');
var app = express();
var passport = require("passport");
var session = require('express-session');
var bodyParser = require('body-parser');

//for BodyParser
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
//for passport
app.use(session({ secret: 'keyboard cat',resave: true, saveUninitialized:true})); // session secret
app.use(passport.initialize());
app.use(passport.session()); // persistent login sessions
//for database
//Models
var models = require("./app/models");
//Sync Database
models.sequelize.sync().then(function() {
    console.log('Nice! Database looks fine')
}).catch(function(err) {
    console.log(err, "Something went wrong with the Database Update!")
});




app.get('/', function (req, res) {
    //res.send("Hello World")
    res.sendFile( __dirname + "/public/" + "index.html" );
})
app.get('/login', function(req, res){
    console.log('logging in');
    req.redirect('/');
})
app.get('/logout', function(req, res){
    console.log('logging out');
    res.redirect('/');
})
var server = app.listen(8000, function () {
    var host = server.address().address
    var port = server.address().port
    
    console.log("Example app listening at http://%s:%s", host, port)
 })

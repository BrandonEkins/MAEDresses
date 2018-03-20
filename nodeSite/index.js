var express = require('express');
var app = express();

app.get('/', function (req, res) {
    res.sendFile( __dirname + "/public/" + "index.html" );
})
//app.listen(3000, () => console.log('example app listening on port 3000!'))
var server = app.listen(8081, function () {
    var host = server.address().address
    var port = server.address().port
    
    console.log("Example app listening at http://%s:%s", host, port)
 })
var mongo = require('mongodb')

var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017"

module.exports = {
    //user is defined by hash, ID, UserID
    mongoAdd: function (user) {
        MongoClient.connect(url, function (err, db) {
            dbo = db.db("mydb");
            dbo.collection("users").insertOne(user, function (err, res) {
                if (err) throw err;
                db.close();
            });
        });
    },

    mongoCheck: function (num) {
        return MongoClient.connect('mongodb://localhost:27017').then(function (db) {
            var dbo = db.db("mydb")
            var stuff = dbo.collection("users").findOne({ 'rand': num });
            db.close();
            return stuff
        }).then(function (items) {
            return items;

        });
    },

    mongoDelete: function (num) {
        MongoClient.connect(url, function (err, db) {
            dbo = db.db("mydb");
            dbo.collection("users").deleteOne({ "rand": num }, function (err, res) {
                if (err) throw err;
                db.close();
            });
        });
    }
}
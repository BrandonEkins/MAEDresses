angular.module('cartApp', ['ngMaterial', 'ngMessages','ngRoute'])
    .controller('cartController', function ($window, $mdDialog, $http, $route) {
        var cart = this;
        // Simple GET request example:
        cart.products = [];
        cart.getapi = function () {
            $http({
                method: 'GET',
                url: '/api/getProducts'
            }).then(function successCallback(response) {
                console.log(response.data);
                cart.products = JSON.parse(JSON.stringify(response.data));
            }, function errorCallback(response) {

            });
            $http({
                method: 'GET',
                url: '/api/getUser'
            }).then(function successCallback(response) {
                console.log(response.data);
                cart.user = JSON.parse(JSON.stringify(response.data));
            }, function errorCallback(response) {

            });
            $http({
                method: 'GET',
                url: '/api/getCart'
            }).then(function successCallback(response) {
                console.log(response.data);
                cart.cart = JSON.parse(JSON.stringify(response.data));
            }, function errorCallback(response) {

            });
            

        }
        cart.getapi();
        cart.showLogonDialog = function (ev) {
            $mdDialog.show({
                contentElement: '#myDialog',
                parent: angular.element(document.body),
                targetEvent: ev,
                clickOutsideToClose: true
            });
        };
        cart.closeLogonDialog = function (ev) {
            $http({
                url: '/login',
                method: "POST",
                data: cart.user
            }).then(function (response) { 
                location.reload();
                console.log("success") // assign  $scope.persons here as promise is resolved here 
            }),function (error) {
                console.log("failed")
            };
            
        }
        cart.addProduct = function(id) {
            
            $http({
                url: '/api/addCart',
                method: "POST",
                data: {"ProductID": cart.products[id].ProductID}
            }).then(function (response) { 
                console.log("success") // assign  $scope.persons here as promise is resolved here 
                $route.reload();
            }),function (error) {
                console.log("failed")
            };

        }
        cart.removeProduct = function(id) {
            $http({
                url: '/api/removeCart',
                method: "POST",
                data: {"CartedProductID":cart.cart[0].CartedProductID}
            }).then(function (response) { 
                console.log("success") // assign  $scope.persons here as promise is resolved here 
                $route.reload();
                $window.location.reload();
                location.reload();
            }),function (error) {
                console.log("failed")
            };
        }

    })
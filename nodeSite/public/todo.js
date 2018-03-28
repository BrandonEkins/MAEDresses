angular.module('cartApp', ['ngMaterial', 'ngMessages'])
    .controller('cartController', function ($mdDialog, $http) {
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
            console.log(cart.user.password);
            console.log(cart.user.email);
            $http({
                url: '/login',
                method: "POST",
                data: cart.user
            }).success(function (data, status, headers, config) {
                console.log("success") // assign  $scope.persons here as promise is resolved here 
            }).error(function (data, status, headers, config) {
                console.log("failed")
            });
            $mdDialog.hide();
        }

    })
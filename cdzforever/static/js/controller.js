angular.module('mainCtrl', []).controller('mainController', function($scope, $http, Episodio) {
    $scope.loading = true;

    Episodio.get().success(function(data) {
        $scope.series = data;
        $scope.loading = false;
    });

    $scope.show = function(id) {
        $scope.loading = true;

        Episodio.show(id).success(function(data) {
            $scope.episodios = data;
            $scope.loading = false;
        });
    };
});
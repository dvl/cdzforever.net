function controller($scope, $http) {
    $scope.loading = true;

    $http.get('/catalogo/series/').success(function(data) {
        $scope.series = data;
    });

    $http.get('/catalogo/episodios/').success(function(data) {
        $scope.episodios = data;
    });
    
    $scope.loading = false;
}

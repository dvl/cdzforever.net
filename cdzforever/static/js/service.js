angular.module('episodioService', []).factory('Episodio', function($http) {
    return {
        get : function() {
            return $http.get('/data/series.json');
        },
        show: function(id) {
            return $http.get('/data/' + id + '.json');
        },
    }
});
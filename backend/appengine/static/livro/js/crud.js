var livro_crud = angular.module('livro_crud', [])

livro_crud.directive('livroform', function () {
    return {
        restrict: 'E',
        replace: true,
        scope: {},
        templateUrl: '/static/livro/html/form.html',
        controller: ['$scope', '$http', function ($scope, $http) {
            $scope.livro = {title: '', price: ''};
            $scope.salvandoFlag = false;
            $scope.erros={};


            $scope.salvar = function () {
                if (!$scope.salvandoFlag) {
                    $scope.erros={};
                    var promessa = $http.post('/books/rest/save', $scope.livro);
                    $scope.salvandoFlag = true;

                    promessa.success(function (livroDoServidor) {
                        $scope.salvandoFlag = false;
                        $scope.livro = {};
                    });

                    promessa.error(function(erros){
                        $scope.salvandoFlag = false;
                        $scope.erros=erros;

                    });
                }
            }

        }]
    };
});
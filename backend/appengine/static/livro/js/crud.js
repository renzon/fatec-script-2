var livro_crud = angular.module('livro_crud', ['livro_rest'])

livro_crud.directive('livroform', function () {
    return {
        restrict: 'E',
        replace: true,
        scope: {livroSalvo: '&'},
        templateUrl: '/static/livro/html/form.html',
        controller: ['$scope', '$http', 'LivroAPI', function ($scope, $http, LivroAPI) {
            $scope.livro = {title: '', price: ''};
            $scope.salvandoFlag = false;
            $scope.erros = {};


            $scope.salvar = function () {
                if (!$scope.salvandoFlag) {
                    $scope.erros = {};
                    var promessa = LivroAPI.salvar($scope.livro);
                    $scope.salvandoFlag = true;

                    promessa.success(function (livroDoServidor) {
                        $scope.livroSalvo({livro: livroDoServidor});
                        $scope.salvandoFlag = false;
                        $scope.livro = {};
                    });

                    promessa.error(function (erros) {
                        $scope.salvandoFlag = false;
                        $scope.erros = erros;

                    });
                }
            }

        }]
    };
});

livro_crud.directive('livrolinha', function () {
    return {
        restrict: 'A',
        replace: true,
        scope: {livro: '=',
            livroApagado: '&'},
        templateUrl: '/static/livro/html/linha.html',
        controller: ['$scope', 'LivroAPI', function ($scope, LivroAPI) {
            $scope.status = 'MOSTRANDO';
            $scope.livroEditando = {};
            $scope.erros = {};

            function copiarPropriedade(origem, destino) {
                destino.id = origem.id;
                destino.title = origem.title;
                destino.price = origem.price;
            }

            $scope.mostrarInputsDeEdicao = function () {
                $scope.status = 'EDITANDO';
                copiarPropriedade($scope.livro, $scope.livroEditando);
            };

            $scope.cancelarEdicao = function () {
                $scope.status = 'MOSTRANDO';
            };

            $scope.salvarEdicao = function () {
                $scope.status = 'SALVANDO';
                LivroAPI.editar($scope.livroEditando).success(function () {
                    $scope.erros = {};
                    $scope.status = 'MOSTRANDO';
                    copiarPropriedade($scope.livroEditando, $scope.livro);
                }).error(function (erros) {
                    $scope.status = 'EDITANDO';
                    $scope.erros = erros;
                });

            };

            $scope.apagar = function () {
                $scope.status = 'APAGANDO';
                LivroAPI.apagar($scope.livro.id).success(function () {
                    if($scope.livroApagado!=null){
                        $scope.livroApagado({'id':$scope.livro.id})
                    }
                });
            }
        }]
    };

});
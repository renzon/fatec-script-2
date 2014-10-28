var livroRest = angular.module('livro_rest', []);

livroRest.factory('LivroAPI', ['$rootScope', function ($rootScope) {
    function criarPromessa() {
        var promessa = {};
        promessa.success = function (fcn) {
            promessa.successFcn = fcn;
            return promessa
        };
        promessa.error = function (fcn) {
            promessa.errorFcn = fcn;
            return promessa;
        };
        return promessa;
    }

    var id = 0;

    var apiObj = {
        salvar: function (livro) {
            var promessa = criarPromessa();
            id += 1;
            setTimeout(function () {
                livro.id = id;
                livro.creation = '02/09/1982 09:00:00';
                promessa.successFcn(livro);
                $rootScope.$digest();
            }, 3000);
            return promessa;
        },
        listar: function () {
            var promessa = criarPromessa();
            id += 1;
            setTimeout(function () {
                var livros = [
                    {title: 'App Engine', price: '23,00', id: '-1', creation: '02/09/1982 09:00:00'},
                    {title: 'Fluent Python', price: '23,00', id: '-2', creation: '02/09/1982 09:00:00'}
                ];
                promessa.successFcn(livros);

                $rootScope.$digest();
            }, 500);
            return promessa;
        }
    };
    return  apiObj;


}]);

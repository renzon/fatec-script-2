/**
 * Created by renzo on 10/1/14.
 */


$(document).ready(function () {
    var $formDiv = $('#form-div');
    $formDiv.hide();
    var $cursoListaDiv = $('#curso-lista-div');
    $('#novo-curso-botao').click(function () {
        $formDiv.slideToggle();
    });


    var $priceInput = $('#priceInput');
    var $titleInput = $('#titleInput');
    var $ajaxLoader = $('#ajax-loader');
    $ajaxLoader.hide();
    function exibirCurso(curso) {
        var template = '<tr id="tr' + curso.id + '" ><td></td>' +
            '<td>' + curso.id + '</td>' +
            '<td>' + curso.creation + '</td>' +
            '<td>' + curso.price + '</td>' +
            '<td>' + curso.title + '</td>' +
            '<td><button id="bt' + curso.id + '" class="btn btn-danger btn-sm"><i class="glyphicon glyphicon-trash"></i></button></td>' +

            '</tr>';
        $corpoTabela.prepend(template);
        var $linhaTabela = $('#tr' + curso.id);
        $linhaTabela.hide();
        $linhaTabela.fadeIn();
        $('#bt' + curso.id).click(function () {
            $.post('/books/rest/delete', {'book_id': curso.id}).success(function(){
                $linhaTabela.remove();
            }).error(function () {
                alert('Não foi possível apagar o curso nesse momento');
                $linhaTabela.fadeIn();
            });
            $linhaTabela.fadeOut();
        });
    }


    $.get('/books/rest').success(function (cursos) {
        cursos.forEach(exibirCurso);
    });
    var $salvarCursoBtn = $('#salvar-curso-btn');


    var $corpoTabela = $('#corpo-tabela');

    $salvarCursoBtn.click(function () {
        var data = {price: $priceInput.val(),
            title: $titleInput.val()};
        $ajaxLoader.show();
        $salvarCursoBtn.hide();
        $.post('/books/rest/save', data).success(function (curso) {
            $priceInput.val('');
            $titleInput.val('');
            exibirCurso(curso);
        }).error(function () {
            alert('Não foi possível acessar');
        }).always(function () {
            $ajaxLoader.hide();
            $salvarCursoBtn.show();
        });
    });
});
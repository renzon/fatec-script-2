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

    $('#salvar-curso-btn').click(function () {
        var data = {price: $priceInput.val(),
            title: $titleInput.val()};
        $.post('/books/rest/save', data).success(function (dadoDoServidor) {
            $priceInput.val('');
            $titleInput.val('');
            console.log(dadoDoServidor);
        }).error(function(){
            alert('Não foi possível acessar');
        });
    });

});
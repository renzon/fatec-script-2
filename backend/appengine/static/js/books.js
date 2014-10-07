/**
 * Created by renzo on 10/1/14.
 */


function aFunction(nome) {
    return'Hello ' + nome;
}

console.log(aFunction());
console.log(aFunction('Renzo'));
console.log(aFunction('Renzo', 'Nuccitelli'));

var a = aFunction;

aFunction = 1;

console.log(aFunction);

console.log(a('Vini'));

function geradoraDeFcnContadora() {
    var i = 0;

    function contar() {
        i += 1;
        return i;
    }

    return contar
}

var contar1 = geradoraDeFcnContadora();

//console.log(i);

console.log(contar1);
console.log(contar1());
console.log(contar1());
console.log(contar1());

contar2 = geradoraDeFcnContadora();

console.log(contar2);
console.log(contar2());
console.log(contar2());
console.log(contar2());

function derivar(fcn) {
    var deltaX = 0.00000000001;

    function derivada(x) {
        return (fcn(x + deltaX) - fcn(x)) / deltaX;
    }

    return derivada
}


function reta(x) {
    return x;
}

var derivaReta = derivar(reta);

console.log(derivaReta(1));
console.log(derivaReta(2));
console.log(derivaReta(3.5));
console.log(derivaReta(1));

function parabola(x) {
    return x * x;
}

var parabolaDerivada = derivar(parabola);

console.log(parabolaDerivada(1));
console.log(parabolaDerivada(2));
console.log(parabolaDerivada(3));

function mouseClick(evento) {
    console.log(evento);
}


function exemploDeIf() {
    if (0 !== []) {
        console.log('Bizarro');
    } else {
        console.log('Esperado');

    }
}

exemploDeIf();

var a = [1, 2, 'Renzo'];

a.push('Nuccitelli');
a.unshift(0);
a.splice(3, 2);

console.log(a);

for (var i = 0; i < a.length; i += 1) {
    console.log(a[i]);
}

var obj = {nome: 'Renzo', 'sobrenome': 'Nuccitelli', 1: 3,
    att: [1, 2, 3],
    f: function blah() {
        return this.nome;
    },
    'obj':{nome:'adfasfd'}};

console.log(obj.nome);
console.log(obj['sobrenome']);
console.log(obj[1]);
console.log(obj.f());
console.log(obj);


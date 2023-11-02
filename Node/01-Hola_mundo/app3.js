console.log("Inicio del programa") ;//1

setTimeout(() => {
    console.log("Primer Time out")//5
}, 3000 );// Quiere decir que solo va a estar disponoble 3``, y después desaparece

setTimeout(() => {
    console.log("Segundo del programa")//3
}, 0 );


setTimeout(() => {
    console.log("Tercero del programa")//4
}, 0 );


console.log("Fin del programa")//2

//Instruciones No Bloqueantes.

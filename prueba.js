const prompt= require('prompt-sync')();
/*
*/
//
const Suma = (a,b) => {
 let suma = (a+ b) / 2; 
 let promedio = suma;
 return promedio
}
console.log(Suma(6,4));

//
const saludo = (a) => {
let saludo = "Hola " + a;
return saludo;
}
console.log(saludo("Aldahir"));

//
const vali = (a) => {
    if (a > 18){
        return("Valido")
    } else { 
        return ("invalido")
    }
     return vali;
}
console.log(vali(20));

/*/
const consonantes = (a) => {
    let contador = 0;
    let vocales = "AEIOUaeiou";
    for(let i = 0; i < a.length; i++ ){
    if (!vocales.includes(a[i])) {
            contador++;
        }
    }
    
    return contador;
}
console.log(consonantes("COMIDA"));

/*/
const consonantes = (a) => {
    let contador = 0;
    let vocales = "AEIOUaeiou";
    for(let i = 0; i < a.length; i++ ){
    if (vocales.includes(a[i])) {
            contador++;
        }
    }
    
    return contador;
}
console.log(consonantes("hola"));

//

function pc(modelo,marca,disco) {
    this.modelo = modelo;
    this.marca = marca;
    this.disco = disco;

}
let pc1 = new pc("Hp", "pavilion", 240 );
let pc2 = new pc("Asus", "pavilion", 240 );
let pc3 = new pc("Dell", "pavilion", 240 );
let database = [pc1,pc2,pc3];
console.log(database);
let contador = 0;
for(let i = 0; i < database.length; i++){
    contador = contador + database[i].disco;
        
    }
console.log("Precio total es : " + contador);

const num = (a,b) => {
    let suma = a + b;
return suma;
}
console.log(num(4,4));







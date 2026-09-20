///1. Diseñe una función flecha que reciba 2 parámetros y devuelva el promedio.
const prompt = require("prompt-sync")();

const Promedio = (n1,n2) => {
    let promedio = (n1 + n2)/2
    return promedio
}
console.log(Promedio(8,6));





//2. Diseñe una función constructora Libro (título, año publicación) e instancie 2 objetos.,


// 1. Función constructora corregida
function Systema(Codigo, Nombre, Categoria, Precio, Stock) {
    this.Codigo = Codigo;
    this.Nombre = Nombre;
    this.Categoria = Categoria;
    this.Precio = Precio;
    this.Stock = Stock;
}

let inventario = [];



// 2. Función para agregar productos usando correctamente el constructor 'Systema'

function AgregarProducto(Codigo, Nombre, Categoria, Precio, Stock) {
    const productoNuevo = new Systema(Codigo, Nombre, Categoria, Precio, Stock);
    inventario.push(productoNuevo);
}



// 3. Función flecha corregida para calcular el valor total del inventario
const CalcularValor = (valor) => {
    return valor.reduce((total, prod) => total + (prod.Precio * prod.Stock), 0);
};

// Agregando productos
AgregarProducto("P001", "Laptop", "Electrónica", 800, 10);
AgregarProducto("P002", "Mouse", "Accesorios", 20, 3);
AgregarProducto("P003", "Teclado", "Accesorios", 45, 2);
AgregarProducto("P004", "Monitor", "Electrónica", 150, 8);



// Bucle para mostrar los productos (propiedades con la primer letra en mayúscula)
console.log("--- LISTA DE PRODUCTOS ---");
for (let i = 0; i < inventario.length; i++) {


    console.log(inventario[i].Nombre + " - Cantidad: " + inventario[i].Stock + " - Precio: $" + inventario[i].Precio);
}

// 4. Uso de función de orden superior (filter) fuera del bucle



console.log("\n--- PRODUCTOS CON STOCK BAJO (< 5) ---");
const StockBajo = inventario.filter(prod => prod.Stock < 5);
console.log(StockBajo);



// 5. Resultado del valor total del inventario
console.log("\nValor total del inventario: $" + CalcularValor(inventario));








function Productos(Nombre, Precio, Cantidad){
this.Nombre = Nombre;
this.Precio = Precio;
this.Cantidad = Cantidad;
}
let inventario = [];
 
function AgregarProducto(Nombre, Precio, Cantidad){
const producto0 = new Productos(Nombre, Precio, Cantidad)
inventario.push(producto0);   
}


const calvalor = (valores) => {
    return valores.reduce((total,p) => total + ( p.Pecio * p.Cantidad), 0)
                                     
}

// Agregando productos
AgregarProducto("P001", "Laptop", "Electrónica", 800, 10);
AgregarProducto("P002", "Mouse", "Accesorios", 20, 3);
AgregarProducto("P003", "Teclado", "Accesorios", 45, 2);
AgregarProducto("P004", "Monitor", "Electrónica", 150, 8);

for(let i = 0; i < inventario.length; i++) {
    console.log(inventario);

}

const Stockbajo = inventario.filter(p => p.Cantidad < 5)

console.log("\nValor total del inventario: $" + CalcularValor(inventario));






// 1. Función constructora con 3 propiedades
function Productos(Nombre, Precio, Cantidad) {
    this.Nombre = Nombre;
    this.Precio = Precio;
    this.Cantidad = Cantidad;
}

let inventario = [];

// 2. Función para agregar productos (ajustada para recibir Nombre, Precio y Cantidad)
function AgregarProducto(Nombre, Precio, Cantidad) {
    const producto0 = new Productos(Nombre, Precio, Cantidad);
    inventario.push(producto0);    
}

// 3. Función flecha corregida para sumar el valor total
const calvalor = (valores) => {
    return valores.reduce((total, p) => total + (p.Precio * p.Cantidad), 0);
};

// Agregando productos (Nombre, Precio, Cantidad)
AgregarProducto("Laptop", 800, 10);
AgregarProducto("Mouse", 20, 3);
AgregarProducto("Teclado", 45, 2);
AgregarProducto("Monitor", 150, 8);

// Bucle corregido para mostrar cada elemento de forma limpia
console.log("--- LISTA DE PRODUCTOS ---");
for (let i = 0; i < inventario.length; i++) {
    console.log(inventario[i].Nombre + " - Cantidad: " + inventario[i].Cantidad + " - Precio: $" + inventario[i].Precio);
}

// Filtro de stock bajo (< 5)
const Stockbajo = inventario.filter(p => p.Cantidad < 5);
console.log("\n--- PRODUCTOS CON STOCK BAJO ---");
console.log(Stockbajo);

// Llamada corregida usando 'calvalor'
console.log("\nValor total del inventario: $" + calvalor(inventario));

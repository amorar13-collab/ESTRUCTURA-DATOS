const prompt = require('prompt-sync')();

function productos(codigo, nombre, categoria, precio, cantidad){
    this.codigo = codigo;
    this.nombre = nombre;
    this.categoria = categoria;
    this.precio = precio;
    this.cantidad = cantidad;

}
let inventario = [];

function registrarProducto(codigo, nombre, categoria, precio, cantidad) {
    const nuevoProducto = new Producto(codigo, nombre, categoria, precio, cantidad);

    inventario.push(nuevoProducto);


    
    console.log("Producto " + nombre + " registrado con éxito.");
}


// Función flecha para calcular el valor total del inventario
const calcularValorTotal = (lista) => {
    return lista.reduce((total, prod) => total + (prod.precio * prod.cantidad), 0);
};

// 1. Registro de productos
registrarProducto("P001", "Laptop", "Electrónica", 800, 10);
registrarProducto("P002", "Mouse", "Accesorios", 20, 3);
registrarProducto("P003", "Teclado", "Accesorios", 45, 2);
registrarProducto("P004", "Monitor", "Electrónica", 150, 8);

console.log("--- Inventario Completo ---");
for (let i = 0; i < inventario.length; i++) {


    // Uso de concatenación con '+'
    console.log(inventario[i].nombre + " - Cantidad: " + inventario[i].cantidad + " - Precio: $" + inventario[i].precio);
}

// 3. Uso de función de orden superior (filter) para stock bajo (< 5)
const productosStockBajo = inventario.filter(producto => producto.cantidad < 5);



console.log("--- Productos con Stock Bajo (< 5) ---");
console.log(productosStockBajo);



// 4. Cálculo del valor total
const valorTotal = calcularValorTotal(inventario);




// Arreglo de estudiantes
let estudiantes = [
    { nombre: "Ana", notas: [8, 9, 7], asistencia: 90 },
    { nombre: "Luis", notas: [4, 5, 3], asistencia: 70 },
    { nombre: "Carlos", notas: [10, 9, 9], asistencia: 95 },
    { nombre: "Maria", notas: [5, 6, 4], asistencia: 80 }
];

// 1. Función flecha para calcular el promedio
const calcularPromedio = (notas) => {
    let suma = 0;
    // Recorrido usando for
    for (let i = 0; i < notas.length; i++) {
        suma += notas[i];
    }
    return suma / notas.length;
};

// 2. Uso de map() para generar un nuevo arreglo con los promedios
const promedios = estudiantes.map(est => calcularPromedio(est.notas));
console.log("Promedios calculados:", promedios);

// 3. Uso de filter() para obtener solo los aprobados (promedio >= 6)
const aprobados = estudiantes.filter(est => calcularPromedio(est.notas) >= 6);
console.log("\nEstudiantes aprobados:");
console.log(aprobados);

// 4. Clasificación de rendimiento con if...else anidados
function clasificarRendimiento(promedio) {
    if (promedio >= 9) {
        return "Excelente";
    } else {
        if (promedio >= 7) {
            return "Bueno";
        } else {
            if (promedio >= 6) {
                return "Regular";
            } else {
                return "Insuficiente";
            }
        }
    }
}

// 5. Recorrido de notas usando while
console.log("\n--- Detalle de notas usando while ---");
estudiantes.forEach(est => {
    console.log("Estudiante: " + est.nombre);
    let i = 0;
    while (i < est.notas.length) {
        console.log("Nota " + (i + 1) + ": " + est.notas[i]);
        i++;
    }
});

// Ejemplo de uso de la clasificación
console.log("\n--- Clasificación de Rendimiento ---");
estudiantes.forEach(est => {
    let prom = calcularPromedio(est.notas);
    console.log(est.nombre + " tiene un promedio de " + prom + " -> " + clasificarRendimiento(prom));
});






// Función constructora para crear objetos Vehiculo
function Vehiculo(placa, marca, anio, kilometraje) {
    this.placa = placa;
    this.marca = marca;
    this.anio = anio;
    this.kilometraje = kilometraje;
}

// Arreglo para almacenar el registro de vehículos
let parqueAutomotor = [
    new Vehiculo("GBA-123", "Toyota", 2024, 15000),
    new Vehiculo("LRC-456", "Chevrolet", 2015, 120000),
    new Vehiculo("MNO-789", "Ford", 2020, 85000),
    new Vehiculo("XYZ-999", "Nissan", 2010, 250000)
];

// 1. Encontrar el vehículo con mayor kilometraje
let vehiculoMasUsado = parqueAutomotor[0];

for (let i = 1; i < parqueAutomotor.length; i++) {
    if (parqueAutomotor[i].kilometraje > vehiculoMasUsado.kilometraje) {
        vehiculoMasUsado = parqueAutomotor[i];
    }
}

console.log("Vehículo con mayor kilometraje: " + vehiculoMasUsado.marca + " (Placa: " + vehiculoMasUsado.placa + ") con " + vehiculoMasUsado.kilometraje + " km.");

// 2. Clasificar cada vehículo según su antigüedad
// Consideramos el año actual como 2026
const anioActual = 2026;

console.log("\n--- Clasificación de Vehículos por Antigüedad ---");

for (let i = 0; i < parqueAutomotor.length; i++) {
    let vehiculo = parqueAutomotor[i];
    let antiguedad = anioActual - vehiculo.anio;
    let categoria = "";

    if (antiguedad <= 2) {
        categoria = "Nuevo";
    } else {
        if (antiguedad <= 7) {
            categoria = "Seminuevo";
        } else {
            if (antiguedad <= 15) {
                categoria = "Usado";
            } else {
                categoria = "Antiguo";
            }
        }
    }

    console.log("Vehículo " + vehiculo.marca + " (" + vehiculo.anio + "): " + categoria + " (" + antiguedad + " años)");
}
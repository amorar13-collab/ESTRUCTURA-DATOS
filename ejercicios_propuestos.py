#Ejericio 1 - Saludo personalizado 

#Entender el problema 
    #Entrada: Leer nombre(input), leer edad
    #Proceso: Concatenar "Hola" + nombre + edad
    #Salida: Mostar el saludo completo(print)

#Bosquejo a mano
    #nombre = "Carlos"
    #edad = 19
    #Salida: Hola, bienvenido Carlos. Tienes 19 años.

#Descubrir el patron 
    #El primer valor de entrada es "nombre" como es str usamos input
    #El segundo valor de entrada es "edad" como es entero usamos int

#Escribir codigo

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad. "))
print(f"Hola, bienvenido {nombre}. Tienes {edad} años.")


#Ejercicio 2 - Promedio tres notas

#Entender el problema 
    #Entrada: Leer nota_1, nota_2 y nota_3
    #Proceso: Sumar las tres notas y dividirla para 3. Ejemplo: (10+9+8)/3
    #Salida: Mostrar el promedio del estudiante

#Bosquejo a mano
    #nota_1 = 10, nota_2 = 9, nota_3 = 9
    #Paso1: Sumar     10 + 9 + 9 = 28
    #Paso 2: Dividir  28/3 = 9.33
    #Salida: Promedio: 9.33

#Descubrir el patron
    #Como los tres valores son notas pueden llegar a ser decimal, usamos float
    #Para este proceso primero se debe de sumar luego dividir y para respetar el orden colocamos parentesis

#Escribir el codigo

nota_1 = float(input("Ingrese nota 1: "))
nota_2 = float(input("Ingrese nota 2: "))
nota_3 = float(input("Ingrese nota 3: "))

promedio = (nota_1 + nota_2 + nota_3)/3

print(f"Promedio: {promedio:.2f}")

#Ejercicio 3 - Area y perimetro de un rectangulo 

#Entender el problema 
    #Entrada: Leer base, leer altura 
    #Proceso: Calcular area multiplicando base y altura
    #         Calcular perimetro sumando la base y altura para ñiegp multiplicar por 2 
    #Salida: Mostrar el area y perimetro del rectangulo 

#Boquejo a mano
    #base = 10, altura = 9
    #Paso1: Calcular area        10 * 9 = 90
    #Paso2: Calcular perimetro   2 * (10 + 9) = 38
    #Salida: Area: 90      Perimetro: 38

#Descubrir el patron
    #Los valores de entrada pueden ser decimal usamos float 

#Escribir el codigo 
base = float(input("Ingrese la base de su rectangulo: "))
altura = float(input("Ingrese la altura de su rectangulo: "))

area = base * altura
perimetro = 2 * (base + altura)
print(f"'Area': {area:.2f}")
print(f"'Perimetro': {perimetro:.2f}")
#Ejercicio 1 - Convertir grados Celsius a Fahrenheit

#Entender el problema 
    #Entrada: Leer grados Celius 
    #Proceso: Multiplicar grado Celsius por 9/2 y luego sumarle 32
    #Salida: Mostrar Fahrenheit

#Bosquejo a mano
    #celsius = 9.5
    #Paso1: multiplicar   9.5 * 9/5 = 17.1
    #Paso2: sumar  17.1 + 32 = 49.1
    #Salida: Fahrenheit: 49.1

#Descubrir el patron
    #Como los grados pueden ser decimal usamos float
    #En esta operacion primero se debe multiplicar y luego sumar

#Escribir el codigo
celsius = float(input("Ingrese Temperatura en °C: "))
fahrenheit = celsius * 9/5 + 32
print(f"Fahrenheit: {fahrenheit:.2f} °F")

#Ejercicio 2: Segundos a horas, minutos y segundos

#Entender el problema 
    #Entrada: Leer el total de segundos 
    #Proceso: Dividir en total para 3600 que son los total de segundos en una hora
    #         Calcular el residuo del total con 3600
    #         Luego de tener el residuo dividimos para los segundos que tiene un minuto que es 60
    #         Para los segundos calculamos el residuo, para el residuo que ya teniamos 
    #Salida: Total de la hora

#Bosquejo a mano 
    #total = 3725
    #Paso1:  Dividir    3725 // 3600 = 1    Se coloca dos / para que el resultado quede entero y no con decimal 
    #Paso2:  Residuo    3725 % 3600 = 125 
    #Paso3:  Dividir    125 // 60 = 2
    #Paso4:  Residuo    125 % 60 = 5
    #Salida:  1:02:05

#Descubrir el patron 
    #Los segundos que se van a ingresar deben ser enteros por eso usamos int 
    #Para calcular vamos a usar signos de operaciones como mood (%) o // que nos servira para obtener resultados enteros

#Escribir codigo

total = int(input("Ingrese el total de segundos: "))
hora = total // 3600
resto = total % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{hora}:{minutos:02d}:{segundos:02d}")

#Ejercicio 3: Intercambiar dos variables

#Entender el problema 
    #Entrada: Leer a y leer b 
    #Proceso: Igualar variables para cambiar los valores 
    #Salida: Mostrar las variables con sus nuevos valores

#Bosquejo a mano 
    #a = 10, b= 9
    #a, b = b, a
    #10, 9 = 10, 9 
    #Salida: a = 9 ; b = 10

#Descubrir el patron 
    #como se van a ingresar numeros estos deben de ser entenros (int)
    #Vamos a igualar las variables para que cambien sus valores

#Escribir codigo
a = int(input("a: "))
b = int(input("b: "))
a, b = b, a
print(f"a = {a}; b = {b}")

#Ejercicio 4: Calcular el Iva 15%

#Entender el problema 
    #Entrada: Leer el precio del producto 
    #Proceso: Multiplicar el precio por el 15% (0.15)
    #         Sumar el precio con el total que salio del iva
    #Salida: Mostrar el total de producto con iva 

#Bosquejar a mano
    #precio = 100
    #Paso 1:  100 * 0.15 = 15
    #Paso 2:  100 + 15 = 115
    #Salida: Iva: 15; Total: 115

#Descubrir el patron 
    #Como vamos a leer una cantidad y es precio tambien puede llegar a ser decimal usamos float
    #Vamos a cacular el total primero multiplicando y despues sumando la cantidad

#Escribir el codigo 
precio = float(input("Ingresa el precio sin Iva: "))
iva = precio * 0.15
total = precio + iva
print(f"Iva: {iva:.2f}")
print(f"Total: {total:.2f}")

#Ejercicio 1 - Calcular IVA 15% y precio final
#Entender el problema 
    #Entrada: Leer precio
    #Proceso: Multiplicar el precio por 0.10 para descuento
    #         Multiplicar el precio por 0.15 para el iva
    #         Sumar el precio con el iva y restar el descuento
    #Salida:   Mostrar el descuento, iva y el precio final 
#Bosquejar a mano 
    #precio = 100
    #Paso 1: 100 * 0.10 = 10
    #Paso 2: 100 * 0.15 = 15
    #Paso 3: 100 + 15 - 10 = 105
    #Salida: Descuento: 10
    #        Iva:15
    #        Precio Final: 105
#Descubrir el patron 
    #Como vamos a usar una cantidad fija ponemos IVA y DESCUENTO en mayuscula 
    #El precio que pueden ingresar puede ser decimal float
    #Usamos operaciones matematicas para calcular el precio, iva y descuento
#Escribir el codigo 
IVA = 0.15
DESCUENTO = 0.10
precio = float(input("Ingrese el precio: "))
descuento = precio * DESCUENTO
iva = precio * IVA
total = precio + iva - descuento
print(f"Descuento: ${descuento:.2f}")
print(f"Iva: ${iva:.2f}")
print(f"Precio Final: ${total:.2f}")

# Ejercicio 2 - Par o Impar y múltiplos

# Entender el problema
    # Entrada: Leer el numero
    # Proceso: Usar las condicionales
    #         Si el numero es divisible entre dos y el residuo es 0 es par
    #         Sino el numero es impar
    #         Si es divisible entre 3 y 5 es múltiplo de ambos
    #         Si es divisible entre 3 es múltiplo de 3
    #         Si es divisible entre 5 es múltiplo de 5
    # Salida: Mostrar si es par o impar y sus múltiplos

# Bosquejar a mano
    # numero = 15
    # 15 / 2 sobra 1 es impar
    # 15 / 3 sobra 0 es múltiplo de 3
    # 15 / 5 sobra 0 es múltiplo de 5
    # Salida: El numero es impar
    #         Es múltiplo de 3 y de 5

# Descubrir el patron
    # Usamos % para obtener el residuo
    # numero % 2 == 0 -> es par
    # numero % 3 == 0 -> es múltiplo de 3
    # numero % 5 == 0 -> es múltiplo de 5

# Escribir el codigo
numero = int(input("Ingrese el numero: "))
resultado = "Par" if numero % 2 == 0 else "Impar"
print(f"{numero} es {resultado}")
if numero % 3 == 0 and numero % 5 == 0:
    print(f"{numero} es múltiplo de 3 y de 5")
elif numero % 3 == 0:
    print(f"{numero} es múltiplo de 3")
elif numero % 5 == 0:
    print(f"{numero} es múltiplo de 5")
else:
    print(f"{numero} no es múltiplo de 3 ni de 5")

# Ejercicio 3 - Convertir hora a segundos

# Entender el problema
    # Entrada: Leer una hora en formato hh:mm:ss
    # Proceso: Separar las horas, minutos y segundos usando split(":")
    #         Convertir cada parte a entero
    #         Multiplicar las horas por 3600
    #         Multiplicar los minutos por 60
    #         Sumar los segundos
    # Salida: Mostrar los segundos totales

# Bosquejar a mano
    # hora = 02:30:15
    # 2 horas = 2 * 3600 = 7200 segundos
    # 30 minutos = 30 * 60 = 1800 segundos
    # 15 segundos = 15 segundos
    # Total = 7200 + 1800 + 15 = 9015 segundos
    # Salida: 9015 segundos

# Descubrir el patron
    # Usamos split(":") para separar la hora
    # "02:30:15" -> ["02", "30", "15"]
    # Convertimos cada parte a entero
    # segundos totales = horas * 3600 + minutos * 60 + segundos

# Escribir el codigo
hora = input("Ingrese la hora (hh:mm:ss): ")
partes = hora.split(":")
horas = int(partes[0])
minutos = int(partes[1])
segundos = int(partes[2])
total = horas * 3600 + minutos * 60 + segundos
print(f"Segundos totales: {total}")

# Ejercicio 4 - Descomponer un monto en monedas

# Entender el problema
    # Entrada: Leer el monto en dólares
    # Proceso: Convertir el monto a centavos
    #          Calcular cuántas monedas de $0.25, $0.10, $0.05 y $0.01 se necesitan
    # Salida: Mostrar la cantidad de cada moneda

# Bosquejar a mano
    # monto = $0.87
    # 87 centavos
    # 25 × 3 = 75 centavos    quedan 12 centavos
    # 10 × 1 = 10 centavos    quedan 2 centavos
    # 5 × 0 = 0
    # 1 × 2 = 2 centavos
    # Salida:
    # $0.25 × 3
    # $0.10 × 1
    # $0.05 × 0
    # $0.01 × 2

# Descubrir el patron
    # Convertimos los dólares a centavos multiplicando por 100
    # Usamos // para obtener la cantidad de monedas
    # Usamos % para obtener el resto

# Escribir el codigo
monto = float(input("Monto: $"))

centavos = int(round(monto * 100))
resto = centavos

m25 = resto // 25; resto = resto % 25
m10 = resto // 10; resto = resto % 10
m05 = resto // 5;  resto = resto % 5
m01 = resto // 1;  resto = resto % 1

print(f"$0.25 × {m25}")
print(f"$0.10 × {m10}")
print(f"$0.05 × {m05}")
print(f"$0.01 × {m01}")

#Ejercicio 1 - Suma de digitos de un numero de 3 cifras
#Entender el problema 
    #Entrada: Leer numero de tres cifras
    #Proceso: Sacar las centenas 
    #         Para obtener decena y unidad 
    #         Luego de separar los numeros los sumanos cada uno
    #Salida: Mostrar suma de numeros 

#Bosquejo a mano 
    #num = 435
    #Paso 1:  435 // 100 = 4
    #Paso 2:  (435 // 10) % 10 = 3
    #Paso 3: 4365 % 10 = 5
    #Paso 4:  4 + 3 + 5 
    #Salida: 12 

#Encontrar el patron 
    #El numero debe ser entero usamos int al leer 
    #Debemos separar los digitos diviendo y sacando el residuo para luego sumarlos

#Escrirbir el codigo 
num = int(input("Número de 3 cifras: "))

centenas = num // 100
decenas = (num // 10) % 10
unidades = num % 10

suma = centenas + decenas + unidades
print(f"Suma: {suma}")

#Ejercicio 2 - Convertir minutos da hora y minutos 
#Entender el problema 
    #Entrada: Leer minutos total
    #Proceso: Para obtener la hora dividimos el total con 60 y obtener solo los valores enteros 
    #         Para los minutos sacamos el residuo del total
    #Salida: Mostrar la hora y minutos 

#Bosquejar a mano 
    #total = 135
    #Paso1: 135 // 60 = 2 
    #Paso 2: 135 % 60 = 15
    #Salida: 2 horas 15 minutos 


#Encontrar el patron

#Escribir el codigo 
total = int(input("Minutos totales: "))

horas = total // 60
mins = total % 60

print(f"{horas} horas {mins} minutos")

#Ejercicio 3 - Indice de masa corporal 
#Entender el problema 
    #Entrada: Leer peso, leer estatura
    #Proceso: la estatura sobre 2 y luego el resultado de eso dividirlo para el peso
    #Salida: Mostrar el IMC
#Bosquejar a mano 
    #peso = 70, estatura = 1.75
    #Paso 1: 1.75 ** 2 = 3.062
    #Paso 2: 70 / 3.062
    #Salida: 22.86

#Encontrar el patron 
    #Para leer el peso y la estatura usamos float ya que puede ser numero decimal 
    #Usamos operadores matematicos para calcular el imc (/) y tambien (**)
#Escribir a mano 
peso = float(input("Peso (kg): "))
estatura = float(input("Estatura (m): "))

imc = peso / (estatura ** 2)
print(f"IMC: {imc:.2f}")

#Ejercicio 4 - Redondeo por cifra decimal 
#Entender el problema
    #Entrada: Leer numero, leer decimales 
    #Proceso: Redondear los numeros en los enteros que esten mas cerca
    #Salida: Mostrar numeros redondeados

#Bosquejar a mano
    #num = 3.14159 , dec = 2
    #Paso 1: Ver la cantidad de decimal que se quiere en este caso son 2
    #Paso 2: round(3.14159, 2) = 3.14
    #Salida: 3.14


#Encontrar el patron
    #Para el numero pueden ser dicimal pero para cantidad de decimal que se quiere debe ser entero 
    #Usamos round para redondear los numeros de una forma mas sencilla

#Escribir codigo
num = float(input("Número: "))
dec = int(input("Decimales: "))

resultado = round(num, dec)
print(resultado)

#Ejercicio 5 -  Descuento por cantidad
#Entender el problema 
    #Entrada: PRECIO = 12, leer cantidad
    #Proceso: Usamos condiciones para dependiendo la cantidad aplicar el descuento
    #         Luego sacamos un subtotal multiplicando el precio por la cantidad
    #         Luego calculamos el total con el descuento 
    #Salida: Mostrar el precio unitario 
    #        Mostrar el descuento
    #        Mostrar el total

#Bosquejar a mano 
    #PRECIO = 12, cantidad = 12
    #12 >= 10 decuento de 0.15
    #12 >= 5 descuento de 0.05
    #sino descuento de 0
    #Paso 1: 12 * 12 = 144
    #Paso 2: 144 * (1 - 0.15) = 122.4  es descuento es de 0.15 porque la cantidad es mayor de 10
    #Salida: Precio unitario: 12
    #        Descuento = 15%
    #        Total: 122.40

#Encontrar el patron 
    #Colocar la variable PRECIO en mayuscula ya que sera una constante el precio siempre debe ser el mismo
    #Usar condiciones para que sepueda aplicar el descuento segun la cantidad
    #Usar operaciones para obtener el descuento
#Escribir el codigo 
PRECIO = 12
cant = int(input("Cantidad: "))

if cant >= 10:
    descuento = 0.15
elif cant >= 5:
    descuento = 0.05
else:
    descuento = 0

subtotal = PRECIO * cant
total = subtotal * (1 - descuento)

print(f"Precio unitario: ${PRECIO}")
print(f"Descuento: {int(descuento*100)}%")
print(f"Total: ${total:.2f}")

#Ejercicio 1 - Contar de n a 1
#Entender el problema
    #Entrada: Leer el numero N
    #Proceso: Usar un ciclo for para contar desde N hasta 1
    #         El ciclo debe ir disminuyendo de uno en uno   9 8 7 6
    #Salida: Mostrar los números de N hasta 1 
#Bosquejar a mano
    # N = 4
    # 4
    # 3
    # 2
    # 1
    # Salida:
    # 4
    # 3
    # 2
    # 1
# Descubrir el patron
    # Usamos range() para generar los números
    # range(n, 0, -1) empieza en n y termina antes de 0
    # El -1 indica que disminuye de uno en uno
#Escribir el codigo
n = int(input("N: "))
for i in range(n, 0, -1):
    print(i)

#Ejercicio 2 - Sumar pares del 2 al 100
#Entender el problema
    # Entrada: No leemos numero
    # Proceso: Usar un ciclo for para recorrer los números pares del 2 al 100
    #         Inicializar una variable suma en 0
    #         Ir acumulando cada número par
    # Salida: Mostrar la suma de los números pares
# Bosquejar a mano
    # 2 + 4 + 6 + 8 + ... + 100
    # Salida: Suma = 2550

# Descubrir el patron
    # Usamos range(2, 101, 2)   2 es el inicio   
    # 101 es el límite, pero no se incluye
    # 2 indica que avanzamos de dos en dos
    # Usamos suma como acumulador
#Escribir el codigo
suma = 0
for i in range(2, 101, 2):
    suma = suma + i
print(f"Suma: {suma}")

#Ejercicio 3 - Factorial de N
#Entender el problema 
    #Entrada: Leer el numero 
    #Proceso: Multiplicar los numeros de 1 hasta n
    #Salida: Mostrar el factorial
#Bosquejar a mano
    #numero = 5
    #i = 1   1 * 1 = 1
    #i = 2   1 * 2 = 2
    #i = 3   2 * 3 = 6
    #i = 4   6 * 4 = 24
    #i = 5   24 * 5 = 120
    #Salida: 5! = 120
#Descubrir el patron 
    #El valor lo debemos iniciar en 1 porque sino simpre nos va a dar 0 
    #Usamos un for range(1, numero + 1) para recorrer el valor 
#Escribir el codigo 
numero = int(input("Ingrese un numero: "))
fact = 1
for i in range(1, numero + 1):
    fact = fact * i
print(f"{numero}! = {fact}")

# Ejercicio 4 - Cuántos aprobaron, reprobaron y porcentaje 

# Entender el problema
    # Entrada: Leer n estudiantes y leer sus notas
    # Proceso: Crear un contador para aprobados y otro para reprobados
    #         Si la nota es mayor o igual a 7, sumar un aprobado
    #         Si no, sumar un reprobado
    #         Calcular el porcentaje de aprobación
    # Salida: Mostrar aprobados, reprobados y porcentaje de aprobación

# Bosquejar a mano
    # n = 4
    # aprobados = 0
    # reprobados = 0
    #
    # nota = 8  -> aprobado = 1
    # nota = 6  -> reprobado = 1
    # nota = 10 -> aprobado = 2
    # nota = 9  -> aprobado = 3
    # Porcentaje de aprobación:
    # (3 / 4) * 100 = 75%
    # Salida:
    # Aprobados: 3 de 4
    # Reprobados: 1 de 4
    # Porcentaje de aprobación: 75%
# Descubrir el patron
    # Creamos una condición para comparar la nota
    # Si la nota es mayor o igual a 7, suma uno a aprobados
    # Si no, suma uno a reprobados
    # Para calcular el porcentaje:
    # aprobados / n * 100
# Escribir el codigo
n = int(input("Ingrese la cantidad de estudiantes: "))
aprobados = 0
reprobados = 0
for i in range(n):
    nota = float(input(f"Ingrese la nota del {i + 1} estudiante: "))
    if nota >= 7:
        aprobados += 1
    else:
        reprobados += 1
porcentaje = (aprobados / n) * 100
print(f"Aprobados: {aprobados} de {n}")
print(f"Reprobados: {reprobados} de {n}")
print(f"Porcentaje de aprobación: {porcentaje:.2f}%")

#Ejercicio 5 - Nota mas baja
#Entender el problema
    #Entrada: Leer n estudiantes y las notas 
    #Proceso: Comparar notas y guardar la nota mas baja y actualizar si aparece una menor
    #Salida: Mostrar la nota mas baja
#Bosquejar a mano 
    #n = 4
    #menor = 0
    #nota1 = 7   7 < menor     menor = 7
    #nota2 = 8   8 < menor     menor = 8
    #nota3 = 9   9 < menor     menor = 9
    #nota4 = 6   6 < menor     menor = 9
    #Salida: Nota maxima: 9

#Descubrir el patron
    #Guardar la nota mas baja o actualizar si aparece una menor
    #Para recorrer los n estudiantes usamos for range(n)

#Escribir el codigo 
n = int(input("Ingrese la cantidad de estudiantes: "))
menor = float("inf")
for i in range(n):
    nota = float(input(f"Ingrese nota {i + 1}: "))
    if nota < menor :
        menor = nota
print(f"Nota Menor: {menor}")

# Ejercicio 6 - ¿Es primo?
# Entender el problema
    # Entrada: No necesitamos leer un numero
    # Proceso: Recorrer los numeros desde 2 hasta 100
    #          Comprobar si cada numero es primo
    #          Si es primo, agregarlo a la lista
    # Salida: Mostrar todos los numeros primos
# Bosquejar a mano
    # Numeros primos entre 2 y 100:
    # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
    # 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    # 73, 79, 83, 89, 97
# Descubrir el patron
    # Recorremos los numeros desde 2 hasta 100
    # Para cada numero suponemos que es primo
    # Comprobamos si tiene algun divisor
    # Si encontramos un divisor, deja de ser primo
    # Si sigue siendo primo, lo agregamos a la lista
# Escribir el codigo
primos = []
for n in range(2, 101):
    es_primo = True
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(n)
print(f"{primos}")

#Ejercicio 1 - Tabla de multiplicar
#Entender el problema
    #Entrada: Leer numero 
    #Proceso: multiplicar el numero por 1,2,3... hasta 12
    #Salida: Mostrar cada respuesta de la multiplicacion
#Bosquejar a mano 
    #numero = 8
    #8 x 1 = 8
    #8 x 2 = 16
    #8 x 3 = 24
    #8 x 4 = 32
    #8 x 5 = 40
    #8 x 6 = 48
    #8 x 7 = 56
    #8 x 8 = 64
    #8 x 9 = 72
#Descubrir el patron
    #Usamos un for range para recorrer los numero 
    #multiplicamos el numero con el valor que va recorriendo 
#Escribir el codigo
numero = int(input(f"Ingrese un numero: "))
tabla = 1
for i in range(1,13):
    tabla = numero * i
    print(f"{numero} x {i} = {tabla}")

# Ejercicio 2 - Contar digitos de un numero
# Entender el problema
    # Entrada: Leer el numero
    # Proceso: Dividir el numero entre 10 para ir eliminando
    #          un digito en cada vuelta
    #          Contar cada vez que eliminamos un digito
    # Salida: Mostrar la cantidad de digitos
# Bosquejar a mano
    # numero = 12345
    # 12345 // 10 = 1234   contador = 1
    # 1234  // 10 = 123    contador = 2
    # 123   // 10 = 12     contador = 3
    # 12    // 10 = 1      contador = 4
    # 1     // 10 = 0      contador = 5
    # Salida: Cantidad de digitos: 5
# Descubrir el patron
    # Dividimos el numero entre 10 usando //
    # Cada division elimina un digito
    # Aumentamos el contador en cada vuelta
    # El ciclo termina cuando el numero llega a 0
# Escribir el codigo
numero = int(input("Ingrese el numero: "))
contador = 0
while numero > 0:
    numero = numero // 10
    contador += 1
print(f"Cantidad de digitos: {contador}")

#Ejercicio 3 - Suma de pares e impares 
#Entender el problema 
    #Entrada: Leer n numeros, leer los numeros 
    #Proceso: Divide los numeros y verifica si son pares o impares 
    #         Escoge los numeros que son pares y los suma 
    #         Escoge los numeros que son impares y los suma 
    #Salida: Mostrar la suma de pares y la suma de impares
#Bosquejar a mano
    #n = 5
    #numeros = 4 7 2 9 6      Se va leyendo cada numero luego dentro de un for  
    #4 % 2 == 0     Par = 4
    #7 % 2 == 0     Impar = 7
    #2 % 2 == 0     Par = 4 + 2 = 6
    #9 % 2 == 0     Impar = 7 + 9 = 16
    #6 % 2 == 0     Par = 6 + 6 = 12
    #Salida: Suma Pares: 12
    #        Suma Impares: 16
#Descubrir el patron 
    #Recorrer con un for la cantidad de numeros para luego ingresar uno por uno 
    #Sacar el residuo y verificar cual es impar y par para irlos sumando 
#Escribir el codigo 
n = int(input("Ingrese la cantidad de numeros: "))
Impar = 0
Par = 0
for i in range(1, n + 1):
    numero = int(input(f"Ingrese numero {i}: "))
    if numero % 2 == 0:
        Par += numero
    else:
        Impar += numero
print(f"Suma pares: {Par}")
print(f"Suma impares: {Impar}")

#Ejercicio 4 - Validar entrada(bucle centinela)
#Entender el problema 
    #Entrada: Leer la edad 
    #Proceso: validar que la edad sea mayor que 0  menor que 120
    #         Solo acepta el valor si esta en ese rango
    #Salida: Mostrar la edad valida 
#Bosquejar a mano 
    #edad = 35
    #si 35 > 0 y 35 < 120   edad valida
    #sino vuelve a pedir el dato 
#Descubrir el patron
    #Usamos while true para validar entradas 
    #Si la condicion se cumple termianmos el proceso con un break
#Escribir el codigo
edad = int(input(f"Ingrese la edad: "))
while True:
    if edad > 0 and edad <= 120:
        print(f"Edad valida: {edad}")
        break
    else:
        edad = int(input(f"Ingrese la edad: "))

#Ejercicio 5 - Adivina el numero
#Entender el problema 
    #Entrada: Leer el numero que ingresa el usuario, crear una variable secreta donde tendra random para que tengo sus propios valores al azar 
    #Proceso:Valida si el numero esta cerca y va presentandosi es mayor o menor 
    #         Tambien debe de contar cuantos intentos realizo el estudiante para adivinar
    #Salida: Mostrar que ese es el numero y las veces que lo intento
#Bosquejar a mano
    #Secreto = 45
    #Usuario = 15
    #45 == 15   no   cuenta un intento 1
    #El numero secreto es mayor
    #Usuario = 40
    #45 == 40   no   cuenta otro intento 1 + 1 = 2
    #El numero secreto es mayor
    #Usuario = 45
    #45 == 45    si 
    #Salida: Correcto, intento 2 veces
#Descubrir el patron 
    #Usamos import random para que luego en secreto le ponemos random.randing y haga numeros al azar
    #Comparamos cada uno de los valores con los que ingresa el usuario
    #Contamos las veces que va intentando el usuario
#Escribir el codigo
import random 
secreto = random.randint(1,101)
contador = 0
while True:
    usuario = int(input("Adivina el numero: "))
    contador += 1
    if secreto == usuario:
        print(f"Correcto, intentaste {contador} veces")
        break
    elif secreto > usuario:
        print(f"El numero secreto es mayor")
    else: 
        print(f"El numero secreto es menor")
    
#Ejercicio 6 - Serie Fibonacci
#Entender el problema
    #Entrada: Leer numero
    #Proceso: Suma el numero anterior con el nuevo para obtener el valor
    #Salida: Mostrar todas las suma de los valores 
#Bosquejar a mano
    #numero = 8
    #0 + 0 = 0
    #0 + 1 = 1
    #1 + 1 = 2
    #1 + 2 = 3
    #2 + 3 = 5
    #3 + 5 = 8
    #5 + 8 = 13
#Descurbir el patron
    #le damos valor a cada variable para hacer la suma a, b = b, a + b
#Escribir el codigo
numero = int(input("Ingrese un numero: "))
a, b = 0, 1
for _ in range(numero):
    print(a, end= " ")
    a, b = b, a + b

# EJERCICIO 1: Validador de notas con promedio

# Entender el problema (E · P · S):
#   - Entrada: Notas individuales o en lotes (*args).
#   - Proceso: Validar que cada nota esté entre 0 y 100, guardarlas en lista y calcular promedio.
#   - Salida: True/False, lista de válidas y promedio.
#
# Bosquejo a mano:
#   - Ingresa 85, 110. 85 pasa (0-100), 110 descartado. Promedio = suma / cantidad.

class Calificador:

    def __init__(self):
        self.notas = []

    def validar_nota(self, nota):
        if nota >= 0 and nota <= 100:
            return True
        else:
            return False

    def cargar_notas(self, *args):
        for nota in args:
            if self.validar_nota(nota):
                self.notas.append(nota)
        return self.notas

    def promedio(self):
        if len(self.notas) == 0:
            return 0.0
        acumulador = 0
        for n in self.notas:
            acumulador = acumulador + n
        return acumulador / len(self.notas)




class Calificaciones:
    def __init__(self):
        self.notas=[]
    def validar_notas(self,notas):
        if 0 <= notas <=100:
            return True
        else:
            return False
    def cargar_notas(self, *args):
        for notas in args:
            if self.validar_notas(notas):
                self.notas.append(notas)
        return self.notas

    def promedio(self):
            if not self.notas:
               return 0
            return sum(self.notas) / len(self.notas)

# EJERCICIO 2: Contador de palabras únicas
# Entender el problema
#   - Entrada: Palabras individuales o en lotes.
#   - Proceso: Guardar en set (sin duplicados) y lista (orden), contar únicas.
#   - Salida: Cantidad de palabras únicas.
#
# Bosquejo a mano:
#- "hola", "mundo", "hola". Set guarda {"hola", "mundo"}. Cantidad = 2.

class AnalizadorTexto:
    def __init__(self):
        self.palabras_lista = []
        self.palabras_conjunto = set()

    def agregar_palabra(self, palabra):
        self.palabras_lista.append(palabra)
        self.palabras_conjunto.add(palabra)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)

    def contar_palabras(self):
        # Retorna la cantidad de elementos únicos almacenados en el conjunto
        return len(self.palabras_conjunto)


class CarroCompras:

    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        total = 0
        for precio in self.articulos.values():
            total = total + precio
        return total

    def articulos_por_rango(self, precio_min, precio_max):
        filtrados = []
        for nombre, precio in self.articulos.items():
            if precio >= precio_min and precio <= precio_max:
                filtrados.append(nombre)
        return filtrados






# EJERCICIO 3: Gestor de compras con totales
# Entender el problema (E · P · S):
#   - Entrada: Nombres de artículos y precios.
#   - Proceso: Guardar en diccionario {nombre: precio}, sumar valores, filtrar por rango.
#   - Salida: Total del carrito y artículos en rango.
#
# Bosquejo a mano:
#   - "pan": 2.50, "leche": 3.00. Total = 5.50. Filtro 2.00-4.00 -> ['pan', 'leche'].
class CarroCompras:
    def __init__(self):
       
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
       
        self.articulos[nombre] = precio

    def total_carrito(self):
      
        total = 0
        for precio in self.articulos.values():
            total += precio
        return total

    def articulos_por_rango(self, precio_min, precio_max):
  
        resultado = []
        for nombre, precio in self.articulos.items():
            if precio_min <= precio <= precio_max:
                resultado.append(nombre)
        return resultado


class InversorSecuencia:

    def invertir_lista(self, lista):
        invertida = []
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida

    def invertir_multiples(self, *listas):
        resultado = {}
        for lst in listas:
            resultado[tuple(lst)] = self.invertir_lista(lst)
        return resultado


# EJERCICIO 4: Inversor de secuencias
# Entender el problema (E · P · S):
#   - Entrada: Una o varias listas.
#   - Proceso: Invertir manualmente con bucles y guardar en diccionario.
#   - Salida: Lista invertida o diccionario.
#
# Bosquejo a mano:
#   - Recorre [1, 2, 3] desde el final hacia el inicio con bucle, obtiene [3, 2, 1].
class InversorSecuencia:
    def invertir_lista(self, lista):
        invertida = []
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida

    def invertir_multiples(self, *listas):
        resultado = {}
        for lst in listas:
            resultado[tuple(lst)] = self.invertir_lista(lst)
        return resultado


class InversorSecuencia:
    def invertir_lista(self, lista):
       
        invertida = []
        
      
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
            
        return invertida

    def invertir_multiples(self, *listas):
        resultado = {}
        for lista in listas:
           
            lista_invertida = self.invertir_lista(lista)
            
            
            resultado[tuple(lista)] = lista_invertida
            
        return resultado


# EJERCICIO 5: Detector de números pares e impares
# Entender el problema (E · P · S):
#   - Entrada: Números en lote.
#   - Proceso: Clasificar pares e impares con operador % reutilizando es_par.
#   - Salida: Diccionario con listas y tupla con cantidades.
#
# Bosquejo a mano:
#   - 1,2,3,4,5 -> Pares: [2,4], Impares: [1,3,5]. Cantidades: (2, 3).
class AnalizadorNumeros:
    def __init__(self):
       
        self.pares = []
        self.impares = []

    def es_par(self, numero):
       
        return numero % 2 == 0

    def separar(self, *numeros):
      
        self.pares = []
        self.impares = []
        
      
        for num in numeros:
          
            if self.es_par(num):
                self.pares.append(num)
            else:
                self.impares.append(num)
                
       
        return {'pares': self.pares, 'impares': self.impares}

    def cantidad_pares_impares(self):
   
        cant_pares = len(self.pares)
        cant_impares = len(self.impares)
        return (cant_pares, cant_impares)



class AnalizadorNumeros:
    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        pares = []
        impares = []
        for n in numeros:
            if self.es_par(n):
                pares.append(n)
            else:
                impares.append(n)
        return {"pares": pares, "impares": impares}

    def cantidad_pares_impares(self, *numeros):
        resultado = self.separar(*numeros)
        return (len(resultado["pares"]), len(resultado["impares"]))


# EJERCICIO 6: Estadísticas de temperatura
# Entender el problema (E · P · S):
#   - Entrada: Temperaturas individuales o en lote.
#   - Proceso: Guardar en lista, calcular mín, máx y promedio con funciones built-in.
#   - Salida: Valores estadísticos.
#
# Bosquejo a mano:
#   - Registra 20, 25, 18, 30. Mín: 18, Máx: 30, Promedio: 23.25.
class GestorTemperatura:
    def __init__(self):
       
        self.temperaturas = []

    def registrar_temperatura(self, temp):
      
        self.temperaturas.append(temp)

    def registrar_multiples(self, *temps):
   
        for temp in temps:
            self.registrar_temperatura(temp)

    def minima(self):
        if not self.temperaturas:
            return 0
        return min(self.temperaturas)

    def maxima(self):
        if not self.temperaturas:
            return 0
        return max(self.temperaturas)

    def promedio(self):
        if not self.temperaturas:
            return 0
        return sum(self.temperaturas) / len(self.temperaturas)


class GestorPersonas:

    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        mayores = []
        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                mayores.append(nombre)
        return mayores

    def edad_promedio(self):
        if len(self.personas) == 0:
            return 0.0
        acumulador = 0
        for edad in self.personas.values():
            acumulador = acumulador + edad
        return acumulador / len(self.personas)


# EJERCICIO 7: Mapeador de edades
# Entender el problema (E · P · S):
#   - Entrada: Nombres y edades.
#   - Proceso: Guardar en diccionario, filtrar por edad mínima, promediar con .values().
#   - Salida: Lista filtrada y promedio.
#
# Bosquejo a mano:
#   - "Ana": 28, "Bob": 17. Mayores a 18 -> ["Ana"]. Promedio -> 22.5.
class GestorPersonas:
    def __init__(self):
        
        self.personas = {}

    def agregar_persona(self, nombre, edad):
       
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        
        resultado = []
        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                resultado.append(nombre)
        return resultado

    def edad_promedio(self):
        if not self.personas:
            return 0
       
        return sum(self.personas.values()) / len(self.personas)



class Equipos:

    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        if equipo not in self.equipos:
            self.crear_equipo(equipo)
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        if len(self.equipos) == 0:
            return None
        max_equipo = None
        max_cant = -1
        for equipo, jugadores in self.equipos.items():
            if len(jugadores) > max_cant:
                max_cant = len(jugadores)
                max_equipo = equipo
        return max_equipo



# EJERCICIO 8: Asignador de equipos
# Entender el problema (E · P · S):
#   - Entrada: Nombres de equipos y jugadores.
#   - Proceso: Crear estructura diccionario de listas, contar elementos y comparar.
#   - Salida: Equipo con mayor cantidad de integrantes.
#
# Bosquejo a mano:
#   - Equipo "A" con "Juan" y "Pedro". Compara longitudes y retorna el mayor.
class Equipos:
    def __init__(self):
        
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
     
        if equipo not in self.equipos:
            self.crear_equipo(equipo)
     
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        if not self.equipos:
            return None
        
     
        equipo_mayor = None
        max_cantidad = -1
        
   
        for equipo, jugadores in self.equipos.items():
            cantidad = len(jugadores)
            if cantidad > max_cantidad:
                max_cantidad = cantidad
                equipo_mayor = equipo
                
        return equipo_mayor



class Equipos:
    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        if equipo not in self.equipos:
            self.crear_equipo(equipo)
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        if not self.equipos:
            return None
        max_equipo = None
        max_cant = -1
        for equipo, jugadores in self.equipos.items():
            if len(jugadores) > max_cant:
                max_cant = len(jugadores)
                max_equipo = equipo
        return max_equipo



# EJERCICIO 9: Validador de caracteres
# Entender el problema (E · P · S):
#   - Entrada: Textos para analizar.
#   - Proceso: Recorrer carácter por carácter, clasificar vocales, consonantes, dígitos.
#   - Salida: Diccionario con conteos.
#
# Bosquejo a mano:
#   - "Hola123" -> Vocales: 2, Consonantes: 2, Dígitos: 3.
class AnalizadorString:
    def __init__(self):
      
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        
        letra_min = letra.lower()
        vocales = "aeiou"
        return letra_min in vocales

    def contar_por_tipo(self, texto):
        
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        cant_vocales = 0
        cant_consonantes = 0
        cant_digitos = 0

     
        for letra in texto:
            if self.solo_vocales(letra):
                cant_vocales += 1
            elif letra.isalpha():  
                cant_consonantes += 1
            elif letra.isdigit():  
                cant_digitos += 1

        
        return {
            'vocales': cant_vocales, 
            'consonantes': cant_consonantes, 
            'digitos': cant_digitos
        }



class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        return letra.lower() in "aeiouáéíóú"

    def contar_por_tipo(self, texto):
        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        vocales = 0
        consonantes = 0
        digitos = 0

        for char in texto:
            if char.isdigit():
                digitos += 1
            elif char.isalpha():
                if self.solo_vocales(char):
                    vocales += 1
                else:
                    consonantes += 1

        return {"vocales": vocales, "consonantes": consonantes, "digitos": digitos}



# EJERCICIO 10: Gestor de tareas con prioridad
# Entender el problema (E · P · S):
#   - Entrada: Descripciones y prioridades.
#   - Proceso: Guardar tuplas en lista, filtrar por prioridad, eliminar por coincidencia.
#   - Salida: Tareas filtradas.
#
# Bosquejo a mano:
#   - Agrega ("Estudiar", "alta"), ("Leer", "baja"). Filtra prioritarias -> [("Estudiar", "alta")].
class Tareas:
    def __init__(self):
    
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad):
    
        self.tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
     
        resultado = []
        for tarea in self.tareas:
           
            if tarea[1] == "alta":
                resultado.append(tarea)
        return resultado

    def eliminar_completada(self, descripcion):
        
        for tarea in self.tareas:
            if tarea[0] == descripcion:
                self.tareas.remove(tarea)
                break  


class Tareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion, prioridad):
        self.tareas.append((descripcion, prioridad))

    def tareas_prioritarias(self):
        resultado = []
        for desc, prio in self.tareas:
            if prio == "alta":
                resultado.append((desc, prio))
        return resultado

    def eliminar_completada(self, descripcion):
        for desc, prio in self.tareas:
            if desc == descripcion:
                self.tareas.remove((desc, prio))
                break


# EJERCICIO 11: Contador de frecuencia
# Entender el problema (E · P · S):
#   - Entrada: Elementos individuales o en lote.
#   - Proceso: Guardar en diccionario contando repeticiones, encontrar máximo.
#   - Salida: Elemento más frecuente y su conteo.
#
# Bosquejo a mano:
#   - Agrega "a", "b", "a". Conteo: {'a': 2, 'b': 1}. Máximo: "a".
class ContadorFrecuencia:
    def __init__(self):
        self.conteo = {}

    def agregar_elemento(self, elemento):
        self.conteo[elemento] = self.conteo.get(elemento, 0) + 1

    def frecuencia_elemento(self, elemento):
        return self.conteo.get(elemento, 0)

    def elemento_mas_frecuente(self):
        if not self.conteo:
            return None
        return max(self.conteo, key=self.conteo.get)



class ContadorFrecuencia:
    def __init__(self):
    
        self.frecuencias = {}

    def agregar_elemento(self, elemento):
       
        if elemento in self.frecuencias:
            self.frecuencias[elemento] += 1
        else:
            self.frecuencias[elemento] = 1

    def frecuencia_elemento(self, elemento):
       
        if elemento in self.frecuencias:
            return self.frecuencias[elemento]
        return 0

    def elemento_mas_frecuente(self):
        if not self.frecuencias:
            return None
        
        elemento_max = None
        max_freq = -1
     
        for elemento, freq in self.frecuencias.items():
            if freq > max_freq:
                max_freq = freq
                elemento_max = elemento
                
        return elemento_max


# EJERCICIO 12: Selector de rango con tuplas
# Entender el problema (E · P · S):
#   - Entrada: Pares (inicio, fin) para varios rangos.
#   - Proceso: Crear rangos como tuplas, unir sin duplicados usando conjuntos.
#   - Salida: Lista de elementos únicos.
#
# Bosquejo a mano:
#   - Rangos (1,3) y (2,4). Conjunto une elementos y elimina duplicados -> [1, 2, 3, 4].
class SelectorRango:
    def crear_rango(self, inicio, fin):
       
        numeros = []
        for i in range(inicio, fin + 1):
            numeros.append(i)
       
        return tuple(numeros)

    def elementos_en_multiples_rangos(self, *rangos):
       
        elementos_unicos = set()
        
    
        for par in rangos:
            inicio = par[0]
            fin = par[1]
            
           
            rango_actual = self.crear_rango(inicio, fin)
            
            
            for numero in rango_actual:
                elementos_unicos.add(numero)
                
        return list(elementos_unicos)


class SelectorRango:
    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def elementos_en_multiples_rangos(self, *rangos):
        unicos = set()
        for inicio, fin in rangos:
            for num in range(inicio, fin + 1):
                unicos.add(num)
        return list(unicos)



# EJERCICIO 13: Combinador de listas
# Entender el problema (E · P · S):
#   - Entrada: Dos o más listas.
#   - Proceso: Alternar elementos de ambas listas utilizando índices y bucles.
#   - Salida: Lista intercalada.
#
# Bosquejo a mano:
#   - Intercala [1, 2] y [3, 4] alternando índices -> [1, 3, 2, 4].
class CombinadorListas:
    def intercalar(self, lista1, lista2):
        resultado = []
        
        
        max_len = len(lista1)
        if len(lista2) > max_len:
            max_len = len(lista2)
            
      
        for i in range(max_len):
            
            if i < len(lista1):
                resultado.append(lista1[i])
          
            if i < len(lista2):
                resultado.append(lista2[i])
                
        return resultado

    def intercalar_multiples(self, *listas):
        if not listas:
            return []
            
   
        resultado_actual = list(listas[0])
        
     
        for i in range(1, len(listas)):
            resultado_actual = self.intercalar(resultado_actual, listas[i])
            
        return resultado_actual


    
class CombinadorListas:
    def intercalar(self, lista1, lista2):
        resultado = []
        max_len = max(len(lista1), len(lista2))
        for i in range(max_len):
            if i < len(lista1):
                resultado.append(lista1[i])
            if i < len(lista2):
                resultado.append(lista2[i])
        return resultado

    def intercalar_multiples(self, *listas):
        if not listas:
            return []
        resultado = list(listas[0])
        for otra_lista in listas[1:]:
            resultado = self.intercalar(resultado, otra_lista)
        return resultado



# EJERCICIO 14: Mapeo de estudiantes a notas
# Entender el problema (E · P · S):
#   - Entrada: Estudiante y nota.
#   - Proceso: Guardar en diccionario, iterar con items(), comparar valores máximos.
#   - Salida: Listas filtradas y tupla (nombre, nota).
#
# Bosquejo a mano:
#   - "Ana": 95, "Bob": 70. Mejor estudiante -> ("Ana", 95).
class RegistroNotas:
    def __init__(self):
        
        self.notas = {}

    def registrar(self, estudiante, nota):
      
        self.notas[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
       
        resultado = []
        for estudiante, nota in self.notas.items():
            if nota >= nota_minima:
                resultado.append(estudiante)
        return resultado

    def mejor_estudiante(self):
        if not self.notas:
            return None
        
        mejor_nombre = None
        mejor_nota = None
        
      
        for estudiante, nota in self.notas.items():
            if mejor_nota is None or nota > mejor_nota:
                mejor_nota = nota
                mejor_nombre = estudiante
                
      
        return (mejor_nombre, mejor_nota)


    
class RegistroNotas:
    def __init__(self):
        self.registro = {}

    def registrar(self, estudiante, nota):
        self.registro[estudiante] = nota

    def estudiantes_aprobados(self, nota_minima):
        return [est for est, nota in self.registro.items() if nota >= nota_minima]

    def mejor_estudiante(self):
        if not self.registro:
            return None
        mejor = max(self.registro, key=self.registro.get)
        return (mejor, self.registro[mejor])



# EJERCICIO 15: Divisores de un número
# Entender el problema (E · P · S):
#   - Entrada: Uno o varios números.
#   - Proceso: Encontrar divisores con bucles módulo, verificar suma de perfectos.
#   - Salida: Tuplas, booleanos, diccionarios.
#
# Bosquejo a mano:
#   - Divisores de 12 -> (1, 2, 3, 4, 6, 12).
class DivisorFinder:
    def encontrar_divisores(self, numero):
        lista_divisores = []
        
        for i in range(1, numero + 1):
            if numero % i == 0:
                lista_divisores.append(i)
      
        return tuple(lista_divisores)

    def es_perfecto(self, numero):
        if numero <= 1:
            return False
            
       
        divisores = self.encontrar_divisores(numero)
        suma = 0
        
  
        for d in divisores:
            if d < numero:
                suma += d
                
        return suma == numero

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}
       
        for num in numeros:
            resultado[num] = self.encontrar_divisores(num)
        return resultado
    


class DivisorFinder:
    def encontrar_divisores(self, numero):
        divs = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                divs.append(i)
        return tuple(divs)

    def es_perfecto(self, numero):
        divs = self.encontrar_divisores(numero)
        suma_divs = sum(d for d in divs if d != numero)
        return suma_divs == numero

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}
        for n in numeros:
            resultado[n] = self.encontrar_divisores(n)
        return resultado



# EJERCICIO 16: Codificador/Decodificador César
# Entender el problema (E · P · S):
#   - Entrada: Letra/palabra y desplazamiento (1-25).
#   - Proceso: Convertir a ASCII, desplazar con módulo %, guardar historial.
#   - Salida: Palabra codificada.
#
# Bosquejo a mano:
#   - "hola" con desplazamiento 3 -> "kroc".
class CodificadorCesar:
    def __init__(self):
        
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
       
        if 'a' <= letra <= 'z':
            base = ord('a')
            desplazado = base + (ord(letra) - base + desplazamiento) % 26
            return chr(desplazado)
  
        elif 'A' <= letra <= 'Z':
            base = ord('A')
            desplazado = base + (ord(letra) - base + desplazamiento) % 26
            return chr(desplazado)
        else:
          
            return letra

    def codificar_palabra(self, palabra, desplazamiento):
        palabra_codificada = ""
        
       
        for letra in palabra:
            palabra_codificada += self.codificar_letra(letra, desplazamiento)
            
       
        self.historial[palabra] = palabra_codificada
        
        return palabra_codificada

    

class CodificadorCesar:
    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        if not letra.isalpha():
            return letra
        base = ord('a') if letra.islower() else ord('A')
        return chr(base + (ord(letra) - base + desplazamiento) % 26)

    def codificar_palabra(self, palabra, desplazamiento):
        codificada = "".join([self.codificar_letra(c, desplazamiento) for c in palabra])
        self.historial[palabra] = codificada
        return codificada



# EJERCICIO 17: Grupo de edades
# Entender el problema (E · P · S):
#   - Entrada: Edades en lote.
#   - Proceso: Clasificar con if/elif, agrupar en diccionario anidado de listas.
#   - Salida: Diccionario agrupado y promedios.
#
# Bosquejo a mano:
#   - 5, 15, 30, 70 -> {'niño':[5], 'adolescente':[15], 'adulto':[30], 'mayor':[70]}.
class AgrupadorEdades:
    def __init__(self):
       
        self.grupos = {
            'niño': [],
            'adolescente': [],
            'adulto': [],
            'mayor': []
        }

    def clasificar_edad(self, edad):
       
        if edad < 13:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 65:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
     
        self.grupos = {
            'niño': [],
            'adolescente': [],
            'adulto': [],
            'mayor': []
        }
        
     
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            self.grupos[categoria].append(edad)
            
        return self.grupos

    def edad_promedio_categoria(self, categoria):
        if categoria not in self.grupos:
            return 0
            
        lista_edades = self.grupos[categoria]
        if not lista_edades:
            return 0
            
      
        suma = 0
        for edad in lista_edades:
            suma += edad
            
        return suma / len(lista_edades)


    
class AgrupadorEdades:
    def clasificar_edad(self, edad):
        if edad <= 12:
            return "niño"
        elif edad <= 19:
            return "adolescente"
        elif edad <= 59:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        grupos = {"niño": [], "adolescente": [], "adulto": [], "mayor": []}
        for edad in edades:
            cat = self.clasificar_edad(edad)
            grupos[cat].append(edad)
        return grupos

    def edad_promedio_categoria(self, categoria, *edades):
        grupos = self.agrupar_por_categoria(*edades)
        lista_cat = grupos.get(categoria, [])
        if not lista_cat:
            return 0.0
        return sum(lista_cat) / len(lista_cat)



# EJERCICIO 18: Matriz de distancias
# Entender el problema (E · P · S):
#   - Entrada: Tuplas (x, y) como puntos 2D.
#   - Proceso: Calcular distancia euclidiana con fórmula matemática, comparar.
#   - Salida: Distancia numérica, punto más cercano.
#
# Bosquejo a mano:
#   - Distancia entre (0,0) y (3,4) -> raíz de (3^2 + 4^2) = 5.0.

class CalculadorDistancia:
    def __init__(self):
      
        self.historial_distancias = []

    def distancia_euclidiana(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        
     
        distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        
      
        self.historial_distancias.append(distancia)
        
        return distancia

    def punto_mas_cercano(self, referencia, *puntos):
        if not puntos:
            return None
            
        punto_cercano = None
        menor_distancia = None
        
       
        for punto in puntos:
            dist = self.distancia_euclidiana(referencia, punto)
            
            
            if menor_distancia is None or dist < menor_distancia:
                menor_distancia = dist
                punto_cercano = punto
                
        return punto_cercano


    
class CalculadorDistancia:
    def __init__(self):
        self.distancias_calculadas = []

    def distancia_euclidiana(self, p1, p2):
        dist = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
        self.distancias_calculadas.append(dist)
        return dist

    def punto_mas_cercano(self, referencia, *puntos):
        if not puntos:
            return None
        mas_cercano = puntos[0]
        min_dist = self.distancia_euclidiana(referencia, mas_cercano)
        for p in puntos[1:]:
            d = self.distancia_euclidiana(referencia, p)
            if d < min_dist:
                min_dist = d
                mas_cercano = p
        return mas_cercano



# EJERCICIO 19: Inventario de productos
# Entender el problema (E · P · S):
#   - Entrada: Productos y cantidades.
#   - Proceso: Guardar/actualizar diccionario, validar restas, filtrar bajo mínimo.
#   - Salida: True/False, lista de productos.
#
# Bosquejo a mano:
#   - "pan": 50, resta 30 (queda 20). Stock menor a 15 -> [].
class Inventario:
    def __init__(self):
       
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
      
        if producto in self.stock:
            self.stock[producto] += cantidad
        else:
            self.stock[producto] = cantidad

    def restar_stock(self, producto, cantidad):
        
        if producto in self.stock and self.stock[producto] >= cantidad:
            self.stock[producto] -= cantidad
            return True
        return False

    def productos_bajo_stock(self, minimo):
        resultado = []
       
        for producto, cantidad in self.stock.items():
            if cantidad < minimo:
                resultado.append(producto)
        return resultado



class Inventario:
    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        self.stock[producto] = self.stock.get(producto, 0) + cantidad

    def restar_stock(self, producto, cantidad):
        if producto in self.stock and self.stock[producto] >= cantidad:
            self.stock[producto] -= cantidad
            return True
        return False

    def productos_bajo_stock(self, minimo):
        return [prod for prod, cant in self.stock.items() if cant < minimo]



# EJERCICIO 20: Analizador de patrones en textos
# Entender el problema (E · P · S):
#   - Entrada: Texto y patrón de búsqueda.
#   - Proceso: split(), filtrar con startswith(), agrupar por longitud, conjunto único.
#   - Salida: Listas, diccionarios, conjuntos.
#
# Bosquejo a mano:
#   - "el gato está aquí" -> {2:['el'], 4:['gato'], 5:['está','aquí']}.
class AnalizadorPatrones:
    def encontrar_palabras(self, texto, patron):
        resultado = []
        palabras = texto.split()
        

        for palabra in palabras:
            if palabra.startswith(patron):
                resultado.append(palabra)
                
        return resultado

    def agrupar_por_longitud(self, texto):
        resultado = {}
        palabras = texto.split()
        
       
        for palabra in palabras:
            lon = len(palabra)
            if lon not in resultado:
                resultado[lon] = []
            resultado[lon].append(palabra)
            
        return resultado

    def palabras_unicas(self, texto):
        unicos = set()
        palabras = texto.split()
        
       
        for palabra in palabras:
            unicos.add(palabra)
            
        return unicos


    
class AnalizadorPatrones:
    def encontrar_palabras(self, texto, patron):
        palabras = texto.split()
        return [p for p in palabras if p.startswith(patron)]

    def agrupar_por_longitud(self, texto):
        palabras = texto.split()
        grupos = {}
        for p in palabras:
            length = len(p)
            if length not in grupos:
                grupos[length] = []
            grupos[length].append(p)
        return grupos

    def palabras_unicas(self, texto):
        return set(texto.split())
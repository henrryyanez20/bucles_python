#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1
Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

# Variable global utilizada para el ejercicio de nota
notas = [70, 82, -1, 65, 55, 67, 87, 92, -1]

# Variable global utilizada para el ejercicio de temperaturas
temp_dataloger = [12.8, 18.6, 14.5, 20.8, 12.1, 21.2, 13.5, 18.6,
                  14.7, 19.6, 11.2, 18.4]


def ej1():
    print('Comenzamos a ponernos serios!')

    '''
    Realice un programa que pida por consola dos números que representen
    el principio y fin de una secuencia numérica.
    Realizar un bucle "for" que recorra esa secuencia armada con "range"
    y cuante cuantes números ingresados hay y la sumatoria de todos los números
    Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    sino que va hasta el anterior
    '''

    inicio = int(input('Ingrese el INICIO NUMERICO de la secuencia\n'))
    fin = int(input('Ingrese el FIN NUMERICO de la secuencia\n'))
    sumatoria = 0
    fin_range = fin + 1

    for x in range(inicio, fin_range):
        sumatoria += x
        cantidad_numeros = len(range(inicio, fin_range))

    print("\n[*] La suma de los Numeros ingresados es:",sumatoria)
    print("\n[*] El Total de numeros de la secuencia ingresada es:",cantidad_numeros)

    promedio = sumatoria / cantidad_numeros
    print("\n[*] El PROMEDIO de los numeros ingresados es:",promedio)
    # cantidad_numeros ....
    # sumatoria ....
    # bucle.....
    # Al terminar el bucle calcular el promedio como:
    # promedio = sumatoria / cantidad_numeros
    # Imprimir resultado en pantalla

def ej2():
    print("Mi Calculadora (^_^)")

    '''
    Tome el ejercicio de clase:
    <condicionales_python /  ejercicios_practica / ej3>,
    copielo a este ejercicio y modifíquelo, ahora se deberá ejecutar
    indefinidamente hasta que como operador se ingrese la palabra "FIN",
    en ese momento debe terminar el programa
    Se debe debe imprimir un cartel de error si el operador ingresado no es
    alguno de lo soportados o no es la palabra "FIN"
    '''
    num_1 = int(input('Ingrese el primer numero a calcular\n'))
    num_2 = int(input('Ingrese el segundo numero a calcular\n'))

    suma = num_1 + num_2
    resta = num_1 - num_2
    multiplicacion = num_1 * num_2
    division = num_1 / num_2
    potencia = num_1 ** num_2
    estado = True

    while estado:
        operador = str(input("Ingresa el simbolo del operador que desea ejecutar: "))

        if operador == "+":
            print("El resultado de la SUMA es:", suma)
        elif operador == "-":
            print("El resultado de la RESTA es:", resta)
        elif operador == "*":
            print("El resultado de la MULTPLICACION es:", multiplicacion)
        elif operador == "/":
            print("El resultado de la DIVISION es:", division)
        elif operador == "**":
            print("El resultado de la POTENCIA es:", potencia)
        elif operador == "FIN":
            print("\n[*] Saliendo de la operación")
            break
        else:
            print("\n\x1b[6;37;41m[!] ERROR, el simbolo o valor ingresado no es válido, intenta de nuevo. \x1b[0m")



def ej3():
    print("Mi organizador académico (#_#)")

    '''
    Tome el ejercicio de "calificaciones":
    <condicionales_python / ejercicios_clase / ej3>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento
    Las notas del estudinte se encuentran almacenadas en una
    lista llamada "notas" que ya hemos definido al comienzo del archivo
    Debe caluclar el promedio de todas las notas y luego transformar
    la califiación en una letra según la escala establecida en el ejercicio
    "calificaciones" <condicionales_python / ejercicios_clase / ej3>
    A medida que recorre las notas, no debe considerar como válidas aquellas
    que son negativas, en ese caso el alumno estuvo ausente
    Debe contar la cantidad de notas válidas y la cantidad de ausentes
    '''

    # Para calcular el promedio primero debe obtener la suma
    # de todas las notas, que irá almacenando en esta variable
    sumatoria = 0           # Ya le hemos inicializado en 0

    cantidad_notas = 0      # Aquí debe contar cuantas notas válidas encontró
    cantidad_ausentes = 0   # Aquí debe contar cuantos ausentes hubo
    puntaje = 0
    print("Mis notas son las siguientes:\n",notas,"\n")
    notas_validas = []
    notas_invalidas = []

    # Realice aquí el bucle para recorrer todas las notas
    # y cacular la sumatoria
    for nota in notas:
        if nota >= 0:
            cantidad_notas += nota
            notas_validas.append(nota)
        else:
            notas_invalidas.append(nota)
            #print("Valor no tomado en cuenta por estas ausente",nota)
    print("_"*66)
    print("Lista de notas VÁLIDAS:",notas_validas)
    print("Lista de notas NO VÁLIDAS:",notas_invalidas,"\n")
    print("_"*66)

    print("La cantidad de notas VÁLIDAS encontradas son:",len(notas_validas))
    print("La cantidad de AUSENCIAS son:", len(notas_invalidas))

    # Terminado el bucle calcule el promedio como
    # promedio = sumatoria / cantidad_notas
    promedio = cantidad_notas / len(notas_validas)
    print("El promedio de notas es:",promedio)
    print("_"*66)
    # Utilice la nota promedio calculada y transformela
    # a calificación con letras, imprima en pantalla el resultado
    if promedio >= 90:
        print("\x1b[6;37;42m[*]Como tu promedio es",promedio,"entonces tienes un [A] de calificación\x1b[0m")
    elif promedio >= 80 and promedio < 90:
        print("\x1b[6;37;42m[*]Como tu promedio es",promedio,"entonces tienes un [B] de calificación\x1b[0m")
    elif promedio >= 70 and promedio < 80:
        print("\x1b[7;30;43m[*]Como tu promedio es",promedio,"entonces tienes un [C] de calificación\x1b[0m")
    elif promedio >= 60 and promedio < 70:
        print("\x1b[6;37;41m[!]Como tu promedio es",promedio,"entonces tienes un [D] de calificación\x1b[0m")
    else:
        print("Tu calificación es [D]")
    # Imprima en pantalla al cantidad de ausentes
    print("_"*66)

def ej4():
    print("Mi primer pasito en data analytics")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_practica /ej5>,
    copielo a este ejercicio y modifíquelo para cumplir el
    siguiente requerimiento
    En este ejercicio se lo provee de una lista de temperatuas,
    esa lista de temperatuas corresponde a los valores de temperaturas
    tomados durante una temperorada del año en Buenos Aires.
    Ustede deberá analizar dicha lista para deducir
    en que temporada del año se realizó el muestreo de temperatura.
    La variable con la lista de temperaturas se llama "temp_dataloger"
    definida al comienzo del archivo
    Debe recorrer la lista "temp_dataloger" y obtener los siguientes
    resultados
    1 - Obtener la máxima temperatura
    2 - Obtener la mínima temperatura
    3 - Obtener el promedio de las temperatuas
    Los resultados se deberán almacenar en las siguientes variables
    que ya hemos preparado para usted
    '''

    temperatura_max = None      # Aquí debe ir almacenando la temp máxima
    temperatura_min = None      # Aquí debe ir almacenando la temp mínima
    temperatura_sumatoria = 0   # Aquí debe ir almacenando la suma de todas las temp
    temperatura_promedio = 0    # Al finalizar el loop deberá aquí alamcenar el promedio
    temperatura_len = 0         # Aquí debe almacenar cuantas temperatuas hay en la lista

    # Colocar el bucle aqui......
    for temperatura in temp_dataloger:

        if (temperatura_min is None) or (temperatura < temperatura_min):
            temperatura_min = temperatura

        elif (temperatura_max is None) or (temperatura > temperatura_max):
            temperatura_max = temperatura

        temperatura_sumatoria += temperatura
        temperatura_len = len(temp_dataloger)
        temperatura_promedio = temperatura_sumatoria / temperatura_len

    print("Temperatura MÍNIMA es:", temperatura_min)
    print("Temperatura MÍNIMA con MIN PYTHON es:",min(temp_dataloger))

    print("Temperatura MÁXIMA es:", temperatura_max)
    print("Temperatura MÁXIMA con MAX PYTHON es:",max(temp_dataloger))

    print("Sumatoria de las temperaturas: ", temperatura_sumatoria)
    print("Sumatoria de las temperaturas con SUM Python = ", sum(temp_dataloger))

    print("Cantidad de temperaturas registradas: ", temperatura_len)
    print("El promedio de las temperaturas es: ", temperatura_promedio)

    # Al finalizar el bucle compare si el valor que usted calculó para
    # temperatura_max y temperatura_min coincide con el que podría calcular
    # usando la función "max" y la función "min" de python
    # función "max" --> https://www.w3schools.com/python/ref_func_max.asp
    # función "min" --> https://www.w3schools.com/python/ref_func_min.asp

    # Al finalizar el bucle debe calcular el promedio como:
    # temperatura_promedio = temperatura_sumatoria / cantidad_temperatuas

    # Corroboren los resultados de temperatura_sumatoria
    # usando la función "sum"
    # función "sum" --> https://www.w3schools.com/python/ref_func_sum.asp

    '''
    Una vez que tengamos nuestros valores correctamente calculados debemos
    determinar en que epoca del año nos encontramos en Buenos Aires utilizando
    la estadística de años anteriores. Basados en el siguiente link realizamos
    las siguientes aproximaciones:
    verano -->      min = 19, max = 28
    otoño -->       min = 11, max = 24
    invierno -->    min = 8, max = 14
    primavera -->   min = 10, max = 24
    Referencia:
    https://es.weatherspark.com/y/28981/Clima-promedio-en-Buenos-Aires-Argentina-durante-todo-el-a%C3%B1o
    '''

    # En base a los rangos de temperatura de cada estación,
    # ¿En qué época del año nos encontramos?
    # Imprima el resultado en pantalla
    # Debe utilizar temperatura_max y temperatura_min para definirlo

    if temperatura_min and temperatura_max:
        if temperatura_min >=8 and temperatura_max <=14:
            print("Temporada de Invierno")

    if temperatura_min and temperatura_max:
        if temperatura_min >=10 and temperatura_max <=24:
            print("Temporada de Primavera")

    if temperatura_min and temperatura_max:
        if temperatura_min >=11 and temperatura_max <=24:
            print("Temporada de Otoño")

    if temperatura_min and temperatura_max:
        if temperatura_min >=19 and temperatura_max <=28:
            print("Temporada de Verano")



def ej5():
    print("Ahora sí! buena suerte :)")

    '''
    Tome el ejercicio:
    <condicionales_python / ejercicios_practica / ej4>,
    copielo a este ejercicio y modifíquelo para cumplir
    el siguiente requerimiento
    Realize un programa que corra indefinidamente en un bucle, al comienzo de la
    iteración del bucle el programa consultará al usuario con el siguiente menú:
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)
    3 - Salir del programa
    En caso de presionar "3" el programa debe terminar e informar por
    pantalla de que ha acabado,
    en caso contrario si se presionar "1" o "2" debe continuar con la siguiente tarea
    NOTA: Si se ingresa otro valor que no sea 1, 2 o 3 se debe enviar
    un mensaje de error y volver a comenzar el bucle
    (vea en el apunte "Bucles - Sentencias" para encontrar
    la sentencia que lo ayude a cumplir esa tarea)
    Si el bucle continua (se presionó "1" o "2") se debe ingresar a otro bucle
    en donde en cada iteración se pedirá una palabra. La cantidad de iteración
    (cantidad de palabras a solicitar) lo dejamos a gusto del alumno, intente que esa
    condición esté dada por una variable (ej: palabras_deseadas = 4)
    Cada palabra ingresada se debe ir almacenando en una lista de palabras, dicha
    lista la debe inicializar vacia y agregar cada nuevo valor con el método "append".
    Luego de tener las palabras deseadas almacenadas en una lista de palabras
    se debe proceder a realizar las siguientes tareas:
    Si se ingresa "1" por consola se debe obtener la palabra
    más grande por orden alfabético
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra
    más grande alfabeticamente.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?
    Si se ingresa "2" por consola se debe obtener la palabra
    con mayor cantidad de letras
    Luego de terminar de recorrer toda la lista (utilizar un bucle "for")
    se debe imprimir en pantalla cual era la palabra con
    mayor cantidad de letras.
    Recuerde que debe inicializar primero su variable
    donde irá almacenando la palabra que cumpla dicha condición.
    ¿Con qué valor debería ser inicializada dicha variable?
    NOTA: Es recomendable que se organice con lápiz y papel para
    hacer un bosquejo del sistema ya que deberá utilizar 3 bucles en total,
    1 - El bucle principal que hace que el programa corra hasta ingresar un "3"
    2 - Un bucle interno que corre hasta socilitar todas las palabras deseadas
        que se deben ir guardando en una lista
    3- Otro bucle interno que corre luego de que termine el bucle "2" que
       recorre la lista de palabras y busca la mayor según el motivo ingresado ("1" o "2")
  '''

    condicion = True
    lista_palabras = []
    total_len = 0

    while condicion:
        menu = int(input("""\nIngrese las siguientes opciones:
                            [*] 1 para orden alfabetico 
                            [*] 2 para orden segun cantidad de letras
                            [*] 3 para finalizar:\n"""))
        if (menu != 1) and (menu != 2) and (menu != 3):
            print("[!] ERROR, vuelva a intentarlo")
        
        elif menu == 3:
            print("[!] Saliendo del programa")
            break

        elif (menu == 1) or (menu == 2):

            if menu == 1:
                lista_palabras = []
                for x in range(4):
                    valor=str(input("[*] Ingresa la palabra numero [{}]/[4]: ".format(x)))
                    lista_palabras.append(valor)
                print("La lista de palabras ingresadas son:\t",lista_palabras)
                print("\x1b[6;37;42m[*] La palabra más grande alfabeticamente es:\x1b[0m {}".format(max(lista_palabras)))

            if menu == 2:
                lista_palabras = []
                for x in range(4):
                    valor=str(input("[*] Ingresa la palabra numero [{}]/[4]: ".format(x)))
                    lista_palabras.append(valor)
                    total_len = len(lista_palabras)

                print("La lista de palabras ingresadas son:\t",lista_palabras)
                print("\x1b[6;37;42m[*] La palabra con más caracteres ingresados es:\x1b[0m",max(lista_palabras, key=len))

if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()

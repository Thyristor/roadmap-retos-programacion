#/*
# * ¿Preparad@ para aprender o repasar el lenguaje de programación que tú quieras?
# * - Recuerda que todas las instrucciones de participación están en el
# *   repositorio de GitHub.
# *
# * Lo primero... ¿Ya has elegido un lenguaje?
# * - No todos son iguales, pero sus fundamentos suelen ser comunes.
# * - Este primer reto te servirá para familiarizarte con la forma de participar
# *   enviando tus propias soluciones.
# *
# * EJERCICIO:
# * - Crea un comentario en el código y coloca la URL del sitio web oficial del
# *   lenguaje de programación que has seleccionado.
# * - Representa las diferentes sintaxis que existen de crear comentarios
# *   en el lenguaje (en una línea, varias...).
# * - Crea una variable (y una constante si el lenguaje lo soporta).
# * - Crea variables representando todos los tipos de datos primitivos
# *   del lenguaje (cadenas de texto, enteros, booleanos...).
# * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
# *
# * ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
# * debemos comenzar por el principio.
# */

if __name__ == "__main__": 
    # * - Crea un comentario en el código y coloca la URL del sitio web oficial del lenguaje de programación que has seleccionado.
    # https://www.python.org/
    
    # * - Representa las diferentes sintaxis que existen de crear comentarios en el lenguaje (en una línea, varias...).
    # Este es un comentario de una linea con hashtag
    ''' 
        Este es un comentario de varias 
        lineas con comillas simples 
    '''
    """ 
        Este es un comentario de varias 
        lineas con comillas dobles 
    """

    # * - Crea una variable (y una constante si el lenguaje lo soporta).
    mi_primera_variable = "mi_primera_variable"
    PI = 3.14159265

    # * - Crea variables representando todos los tipos de datos primitivos del lenguaje (cadenas de texto, enteros, booleanos...).
    entero = 3 # int
    flotante = 3.141592 # float
    cadena = "cadena" # string
    booleano = True # bool
    lista = [1, 2, 3] # list
    tupla = (4, 5, 6) # tuple
    diccionario = {'uno': 1, 'dos': 2, 'tres': 3} # dict
    conjuntos = {1, 2, 3, 3, 4} # los conjuntos no tienen elementos duplicados 

    # * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
    nombre_lenguaje = "Python"
    print(f"¡Hola, {nombre_lenguaje}!")
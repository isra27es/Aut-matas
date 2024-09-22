#Lenguajes Automatas
#Espinosa López Israel SOFT 07-01
# Función 
def automata(word):
    # Definir transiciones del autómata como un diccionario
    transiciones = {
        'q0': {'a': 'q1', 'b': 'q2'},
        'q1': {'a': 'q1', 'b': 'q1'},
        'q2': {'a': 'q0', 'b': 'q2'}
    }

    # Estado inicial
    estado = 'q0'

    # Procesar cada símbolo de la palabra
    for simbolo in word:
        if simbolo in transiciones[estado]:
            estado = transiciones[estado][simbolo]
        else:
            return False  # Símbolo no reconocido

    # Verificar si el estado final es de aceptación
    return estado in {'q1', 'q2'}

# Lista de palabras para probar
palabras = ["ab", "ba", "aaa", "bba", "abb", "bbb", "aab"]

# Probar cada palabra
for palabra in palabras:
    if automata(palabra):
        print(f"La palabra '{palabra}' es aceptada.")
    else:
        print(f"La palabra '{palabra}' no es aceptada.")


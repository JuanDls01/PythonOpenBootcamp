# En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt,
# lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces
# al archivo creado.

archivoCreado = open('archivo.txt', 'x')
archivoEscrito = open('archivo.txt', 'a')
archivoEscrito.write('Hola, como estas?')

import pickle as manip


class Vehiculo:
    marca = ''
    valor = 0

    def __init__(self, marca, valor):
        self.marca = marca
        self.valor = valor


# Instanciamos el vehiculo:
miAuto = Vehiculo('volkswagen', 1000)

# Creamos el archivo:
archivo = open('archivoEj2.bin', 'ab')

# Guardamos (serializamos) el objeto en el archivo:
manip.dump(miAuto, archivo)

archivo.close()

# Abrimos el archivo para leer:
archivo = open('archivoEj2.bin', 'rb')

# Cargamos (deserializamos) el objeto del archivo:
autoCargado = manip.load(archivo)

archivo.close()

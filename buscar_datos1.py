import unittest

def buscar_datos(*args, **kwargs):
    # Obtener el diccionario de la base de datos de personas
    database = kwargs.get('database', {})
    
    # Crear una lista para almacenar los IDs de las personas encontradas
    personas_encontradas = []

    ##Se itera sobre cada persona en la base de datos, donde key es el ID de la persona y datos_persona son los datos asociados a esa persona
    for key, datos_persona in database.items():

        # Verificar si todos los nombres y apellidos están presentes en los datos de la persona
        if all(arg in  datos_persona.values() for arg in args):
            #agrega el ID de esa persona a la lista de personas encontradas.   
            personas_encontradas.append(key)

    return personas_encontradas #Devuelve un valor booleano


# Base de datos de personas
database = {
    "primer persona": {
        "nombre1": "Pablo",
        "nombre2": "Diego",
        "apellido1": "Ruiz",
        "apellido2": "Picasso"
    },
    "Segunda persona": {
        "nombre1": "Elio",
        "apellido1": "Anci"
    },
    "Tercer persona": {
        "nombre1": "Elias",
        "nombre2": "Marcos",
        "nombre3": "Luciano",
        "apellido1": "Marcelo",
        "apellido2": "Gonzalez"
    }
}

# Ejemplo de uso
resultado = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", database=database)
print(resultado)  # Salida esperada: ["primer persona"]

resultado = buscar_datos("Elio", "Anci", database=database)
print(resultado)  # Salida esperada: ["Segunda persona"]

resultado = buscar_datos("Elias", "Marcos","Luciano", "Marcelo", "Gonzalez", database=database)
print(resultado)  # Salida esperada: ["Tercer persona"]

# class TestDatos(unittest.TestCase):
#     def test_1(self):
#         resultado = buscar_datos("Pablo")
#         self.assertEqual(resultado, True)
    
#     def test_2(self):
#         resultado = buscar_datos("Diego")
#         self.assertEqual(resultado, True)
    
#     def test_3(self):
#         resultado = buscar_datos("Ruiz")
#         self.assertEqual(resultado, True)
    
#     def test_4(self):
#         resultado = buscar_datos("Picasso")
#         self.assertEqual(resultado, True)


# unittest.main()
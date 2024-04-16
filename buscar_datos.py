import unittest

def buscar_datos(*args, **kwargs):
    for arg in args:
        print(arg)
        
    for key, value in kwargs.items():
        print("key:", key, "value:", value)

    for persona in database.values():  # Iterate through the values of kwargs
        for dato in persona.values():  # Iterate through the values of each persona
            if dato in args:  # Check if the dato is in the args passed to buscar_datos
                print(f"'{dato}' is present in the arguments.")
            else:
                print(f"'{dato}' is not present in the arguments.")
    #lista = [str(data for data in kwargs.values())]
 

# Example usage
database = {
    "persona1": {
        "primer_nombre": "pablo",
        "segundo_nombre": "diego",
        "primer_apellido": "ruiz",
        "segundo_apellido": "Picasso",
    }
}

buscar_datos("pablo", "Diego", "Ruiz", "Picasso", **database)


database = {
    "persona1": {
        "primer_nombre": "pablo",
        "segundo_nombre": "diego",
        "primer_apellido": "ruiz",
        "segundo_apellido": "Picasso",
    }
}

buscar_datos("pablo", "Diego", "Ruiz", "Picasso", **database)

class TestDatos(unittest.TestCase):
    def test_1(self):
        resultado = buscar_datos("pablo")
        self.assertEqual(resultado, True)
    
    def test_2(self):
        resultado = buscar_datos("diego")
        self.assertEqual(resultado, True)
    
    def test_3(self):
        resultado = buscar_datos("ruiz")
        self.assertEqual(resultado, True)
    
    def test_4(self):
        resultado = buscar_datos("picasso")
        self.assertEqual(resultado, True)


unittest.main()
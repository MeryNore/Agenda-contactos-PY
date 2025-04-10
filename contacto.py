# importación de la librería re que permite trabajar con expresiones regulares
import re

class Contacto:

    # Contador de contactos que será el ID de cada contacto según se incremente
    contador_contacto = 0

    # Constructor de la clase Contacto
    def __init__(self, nombre, telefono, email):

        # Validar y asignar los atributos del contacto
        if not nombre.strip() or not telefono.strip() or not email.strip():
            raise ValueError("Ninguno de los campos (nombre, teléfono, email) puede estar vacío.")

        # Validar el NOMBRE
        pattern = r"^[\D\s]{3,45}$"
        if not re.fullmatch(pattern, nombre):
            raise ValueError("El nombre debe contener entre 3 y 45 caracteres y no puede contener números.")

        # Validar el TELEFONO
        pattern = r"^\d{9}$"
        if not re.fullmatch(pattern, telefono):
            raise ValueError("El teléfono debe contener 9 dígitos.")

        # Validar el EMAIL
        pattern = r"^[\w.+-]+@[\w-]+\.[\w.-]{2,5}$"
        if not re.fullmatch(pattern, email):
            raise ValueError("El email no es válido.")

        # Incrementar el contador de contactos y asignar el ID al nuevo contacto
        Contacto.contador_contacto += 1

        # Asignar el ID de contacto al nuevo contacto
        self.__id_contacto = Contacto.contador_contacto
        self.__nombre = nombre
        self.__telefono = telefono
        self.__email = email

    def get_id_contacto(self):
        return self.__id_contacto
    def get_nombre(self):   
        return self.__nombre
    def get_telefono(self):     
        return self.__telefono
    def get_email(self):    
        return self.__email

    # Inicializar la lista de contactos
    def __str__(self):
        return f'Contacto: id: {self.__id_contacto}, Nombre: {self.__nombre}, Telefono: {self.__telefono}, Email: {self.__email}]'
    
    # Método para escribir el contacto en un archivo, el formato de cada linea es "id_contacto,nombre,telefono,email"
    def escribir_contacto(self):
        return f'{self.__id_contacto},{self.__nombre},{self.__telefono},{self.__email}'
    
    def eliminar_contacto(self):
        Contacto.contador_contacto -= 1
        self.__id_contacto = Contacto.contador_contacto
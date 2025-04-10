# importación libría os que permite interactuar con el sistema operativo para leer el archivo txt
import os.path

# importación de la clase Contacto que contiene los atributos de un contacto
from contacto import Contacto


class AccionesContactos:

    # Definición de la constante NOMBRE_ARCHIVO que contiene el nombre del archivo donde se guardan los contactos
    NOMBRE_ARCHIVO = "contactos.txt"

    # definición del constructor de la clase AccionesContactos que inicializa la lista de contactos y verifica si el archivo existe
    def __init__(self):
        self.contactos = []

        if os.path.isfile(self.NOMBRE_ARCHIVO):
            self.contactos = self.obtener_contactos()
        else:
            self.crear_contacto_inicial()
    
    def crear_contacto_inicial(self):
        contacto_inicial = [
            Contacto('Maria', '654321961', 'maria@gmail.com')
        ]
        self.contactos.extend(contacto_inicial)
        self.guardar_contactos_archivo(contacto_inicial)
    
    # Método para agregar un nuevo contacto a la lista de contactos y guardarlo en el archivo
    def guardar_contactos_archivo(self, contactos):
        try:
            with open(self.NOMBRE_ARCHIVO, "a") as archivo:
                for contacto in contactos:
                    archivo.write(contacto.escribir_contacto() + "\n")
            print("Contacto guardado en el archivo.")
        except Exception as e:
            print(f"Error al guardar el contacto en el archivo: {e}")
    
    # Método para eliminar un contacto de la lista de contactos y guardarlo en el archivo
    def eliminar_contactos_archivo(self, contacto):
        try:
            with open(self.NOMBRE_ARCHIVO, "w") as archivo:
                archivo.write(contacto.eliminar_contacto(contacto) + "\n")
            print("Contacto eliminado del archivo.")
        except Exception as e:
            print(f"Error al eliminar el contacto en el archivo: {e}")

    def obtener_contactos(self):
        contactos = []
        try:
            with open(self.NOMBRE_ARCHIVO, "r") as archivo:
                for linea in archivo:
                    id_contacto, nombre, telefono, email = linea.strip().split(",")
                    contacto = Contacto(nombre, telefono, email)
                    contactos.append(contacto)
        except Exception as e:
            print(f"Error al obtener los contactos: {e}")
        return contactos

    def agregar_contacto(self, contacto):
        try:
            self.contactos.append(contacto)
            self.guardar_contactos_archivo([contacto])
            print("Contacto agregado correctamente.")
        except ValueError as e:
            print(f"Error al agregar el contacto: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")
    
    def mostrar_contactos(self):
        try:
            if not self.contactos:
                print("No hay contactos disponibles.")
            else:
                print("*** Lista de contactos: ***")
                for contacto in self.contactos:
                    print(contacto)
        except Exception as e:
            print(f"Error al mostrar los contactos: {e}")
    
    def buscar_contacto(self, nombre):
        try:
            if not self.contactos:
                print("No hay contactos disponibles.")
            for contacto in self.contactos:
                if contacto.nombre == nombre:
                    print(f"Contacto encontrado: {contacto}")
            if not any(contacto.nombre == nombre for contacto in self.contactos):
                print(f"Contacto {nombre} no encontrado.")
        except Exception as e:
            print(f"Error al buscar el contacto: {e}")

    def eliminar_contacto(self, nombre):
        try:
            # Si no encuentra el nombre. Realizamos primero esta acción porque despues ya estaría borrado y no lo encontraría.
            if not any(contacto.nombre == nombre for contacto in self.contactos):
                print(f"Contacto {nombre} no encontrado.")
            # Si encuentra el nombre
            for contacto in self.contactos:
                if contacto.nombre == nombre:
                    self.contactos.remove(contacto)
                    self.eliminar_contactos_archivo([contacto])
                    print(f"Contacto {contacto.nombre} eliminado.")
        except Exception as e:
            print(f"Error al eliminar el contacto: {e}")

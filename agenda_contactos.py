from acciones_contactos import AccionesContactos
from contacto import Contacto


class AgendaContactos:
    def __init__(self):
        self.acciones_contactos = AccionesContactos()

    def agenda_contactos(self):
        salir = False
        print("----- Agenda ----")
        self.acciones_contactos.mostrar_contactos()
        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f"Error inesperado: {e}")

    def mostrar_menu(self):
        while True:
            try:
                print('''Menú de opciones:
                1. Agregar contacto
                2. Mostrar contactos
                3. Buscar contacto
                4. Eliminar contacto
                5. Salir''')
                opcion = int(input("Seleccione una opción: "))
                return opcion
            except ValueError:
                print("Debe ingresar un número válido. Intente nuevamente.")
    
    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.agregar_contacto()
        if opcion == 2:
            self.acciones_contactos.mostrar_contactos()
        if opcion == 3:
            self.buscar_contacto()
        if opcion == 4:
            self.eliminar_contacto()
        if opcion == 5:
            print("Saliendo de la agenda...")
            return True
        else:
            print(f'Opción {opcion} no válida. Intente nuevamente.')
        return False
    
    def agregar_contacto(self):
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        email = input("Ingrese el email del contacto: ")
        nuevo_contacto = Contacto(nombre, telefono, email)
        self.acciones_contactos.agregar_contacto(nuevo_contacto)

    
    def buscar_contacto(self):
        try:
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            self.acciones_contactos.buscar_contacto(nombre)
        except Exception as e:
            print(f"Error al buscar el contacto: {e}")
    
    def eliminar_contacto(self):
        try:
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            self.acciones_contactos.eliminar_contacto(nombre)
        except Exception as e:
            print(f"Error al eliminar el contacto: {e}")


# Programa principal
if __name__ == '__main__':
    agenda_contactos = AgendaContactos()
    agenda_contactos.agenda_contactos()
from models.modelo import Modelo
from view.vista import Vista

class Controlador:
    def __init__(self, server, database, username, password):
        self.modelo = Modelo(server, database, username, password)
        self.vista = Vista()

    def iniciar(self):
        self.modelo.connect()
        while True:
            self.vista.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            #Agregar producto
            if opcion == '1':
                nombre, cantidad, precio = self.vista.agregar_producto()
                self.modelo.agregar_producto(nombre, cantidad, precio)
                self.vista.mostrar_mensaje("Producto agregado exitosamente.")

            # Modificar producto
            elif opcion == '2':
                id_producto, nombre, cantidad, precio = self.vista.modificar_producto()
                self.modelo.modificar_producto(id_producto ,nombre, cantidad, precio)
                self.vista.mostrar_mensaje("Producto modificado exitosamente.")
            # Eliminar producto
            elif opcion == '3':
                id_producto = self.vista.eliminar_producto()
                self.modelo.eliminar_producto(id_producto)
                self.vista.mostrar_mensaje("Producto eliminado exitosamente.")
            # Buscar producto
            elif opcion == '4':
                id_producto = self.vista.buscar_producto()
                producto = self.modelo.buscar_producto(id_producto)
                if producto:
                    self.vista.mostrar_mensaje(f"Producto encontrado: {producto}")
                else:
                    self.vista.mostrar_mensaje("Producto no encontrado.")
            # Listar productos
            elif opcion == '5':
                productos = self.modelo.listar_productos()
                if productos:
                    self.vista.listar_productos(productos)
                else:
                    self.vista.mostrar_mensaje("No hay productos para mostrar.")

            # Verificar conexión
            elif opcion == '6':
                conexion = self.modelo.connect()
                self.vista.verificar_conexion(conexion)

            # Mostrar total
            elif opcion == '7':
                total = self.modelo.total_valor()
                if total is not None:
                    self.vista.mostrar_total(total)
                else:
                    self.vista.mostrar_mensaje("No hay productos para calcular el total.")
            # Salir
            elif opcion == '8':
                self.vista.mostrar_mensaje("Saliendo del programa...")
                print("Cerrando conexión a la base de datos...")
                self.modelo.close()
                break
            else:
                print("Opción no válida. Intente de nuevo.")
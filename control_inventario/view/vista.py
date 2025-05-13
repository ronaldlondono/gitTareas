class Vista:
    @staticmethod
    def mostrar_menu():
        print("1. Agregar producto")
        print("2. Modificar producto")
        print("3. Eliminar producto")
        print("4. Buscar producto")
        print("5. Listar productos")
        print("6. verificar conexion")
        print("7. Mostrar total")
        print("8. Salir")

    @staticmethod
    def agregar_producto():
        print("Agregar producto")
        print("="*100)
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio = float(input("Ingrese el precio del producto: "))
        return nombre, cantidad, precio
    
    def modificar_producto(self):
        print("Modificar producto por ID")
        print("="*100)
        id_producto = int(input("Ingrese el ID del producto a modificar: "))
        nombre = input("Ingrese el nuevo nombre del producto: ")
        cantidad = int(input("Ingrese la nueva cantidad del producto: "))
        precio = float(input("Ingrese el nuevo precio del producto: "))
        return id_producto, nombre, cantidad, precio
    
    def eliminar_producto(self):
        print("Eliminar producto por ID")
        print("="*100)
        id_producto = int(input("Ingrese el ID del producto a eliminar: "))
        return id_producto
    
    def buscar_producto(self):
        print("Buscar producto por ID")
        print("="*100)
        id_producto = int(input("Ingrese el ID del producto a buscar: "))
        return id_producto
    
    def listar_productos(self, productos):
        print("Lista de productos")
        print("="*100)
        print(f"{'ID':<20} {'Nombre':<20} {'Cantidad':<20} {'Precio':<20}")
        print("="*100)
        for producto in productos:
            print(f"{producto[0]:<20}\t{producto[1]:<20}\t{producto[2]:<20}\t{producto[3]:<20}")

    def mostrar_total(self, total):
        print("="*100)
        print(f"El valor total de los productos es: {total}")
        print("="*100)

    def verificar_conexion(self, conexion):
        if conexion:
            print("Conexión exitosa a la base de datos.")
        else:
            print("Error al conectar a la base de datos.")

    def mostrar_mensaje(self, mensaje):
        print(mensaje)
import pyodbc

class Modelo:
    def __init__(self, server, database, username, password):
        self.connection_string = f'DRIVER={{MySQL ODBC 9.3 ANSI Driver}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        self.connection = pyodbc.connect(self.connection_string)
        self.cursor = self.connection.cursor()

    def connect(self):
        try:
            self.connection = pyodbc.connect(self.connection_string)
            return True
        except pyodbc.Error as e:
            return False
###------------------------------------------------------------------------------
    
    def agregar_producto(self, nombre, cantidad ,precio):
            try:
                query = "INSERT INTO Productos (Nombre, Cantidad, Precio) VALUES (?, ?, ?)"
                self.cursor.execute(query, (nombre, cantidad, precio))
                self.connection.commit()
            except pyodbc.Error as e:
                print(f"Error al agregar producto: {e}")

    def modificar_producto(self, id_producto, nombre, cantidad, precio):
        try:
            query = "UPDATE Productos SET Nombre = ?, Cantidad = ?, Precio = ? WHERE ID = ?"
            self.cursor.execute(query, (nombre, cantidad, precio, id_producto))
            self.connection.commit()
        except pyodbc.Error as e:
            print(f"Error al actualizar producto: {e}")        

    def buscar_producto(self, id_producto):
            try:
                query = "SELECT * FROM Productos WHERE ID = ?"
                self.cursor.execute(query, (id_producto,))
                producto = self.cursor.fetchone()
                if producto:
                    return producto
                else:
                    print("Producto no encontrado.")
                    return None
            except pyodbc.Error as e:
                print(f"Error al buscar producto: {e}")
                return None
        
    def listar_productos(self):
        try:
            query = "SELECT * FROM Productos"
            self.cursor.execute(query)
            productos = self.cursor.fetchall()
            return productos
        except pyodbc.Error as e:
            print(f"Error al obtener productos: {e}")
            return None
    
    def eliminar_producto(self, id_producto):
        try:
            query = "DELETE FROM Productos WHERE ID = ?"
            self.cursor.execute(query, (id_producto,))
            self.connection.commit()
        except pyodbc.Error as e:
            print(f"Error al eliminar producto: {e}")

    def total_valor(self):
        try:
            query = "SELECT SUM(Cantidad * Precio) FROM Productos"
            self.cursor.execute(query)
            total = self.cursor.fetchone()[0]
            return total
        except pyodbc.Error as e:
            print(f"Error al calcular el total: {e}")
            return None

    def close(self):
        if self.connection:
            self.connection.close()
            print("Conexión cerrada.")
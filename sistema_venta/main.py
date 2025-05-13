from models.model import Venta, Producto, Cliente
from views.vista_main import MainView

if __name__ == "__main__":
    # Crear la base de datos y las tablas
    Venta.create_table()
    Producto.create_table()
    Cliente.create_table()

    # Iniciar la aplicación
    app = MainView()
    app.mainloop()

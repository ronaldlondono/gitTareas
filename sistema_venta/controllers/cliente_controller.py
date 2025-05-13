from models.model import Cliente

def crear_cliente(nombre, email, telefono):
    try:
        cliente = Cliente.create(nombre=nombre, email=email, telefono=telefono)
        return cliente
    except Exception as e:
        print(f"Error al crear el cliente: {e}")

def obtener_clientes():
    try:
        # Obtener todos los clientes de la base de datos
        clientes = Cliente.select()
        return list(clientes)
        
    except Exception as e:
        print(f"Error al obtener los clientes: {e}")

def eliminar_cliente(isSelected):
    try:
        cliente = Cliente.get(Cliente.id == isSelected)
        cliente.delete_instance()
        print(f"Cliente con ID {isSelected} eliminado.")
    except Exception as e:
        print(f"Error al eliminar el cliente: {e}")
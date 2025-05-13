from models.model import Producto

def crear_producto(nombre, precio):
    try:
        producto = Producto.create(nombre=nombre, precio=precio)
        return producto
    except Exception as e:
        print(f"Error al crear el producto: {e}")
    
def obtener_productos():
    try:
        productos = Producto.select()
        return list(productos)
    except Exception as e:
        print(f"Error al obtener los productos: {e}")
    
def eliminar_producto(isSelected):
    try:
        producto = Producto.get(Producto.id == isSelected)
        producto.delete_instance()
        print(f"Producto con ID {isSelected} eliminado.")
    except Exception as e:
        print(f"Error al eliminar el producto: {e}")

def actualizar_producto(isSelected, nombre, precio):
    try:
        producto = Producto.get(Producto.id == isSelected)
        producto.nombre = nombre
        producto.precio = precio
        producto.save()
        print(f"Producto con ID {isSelected} actualizado.")
    except Exception as e:
        print(f"Error al actualizar el producto: {e}")
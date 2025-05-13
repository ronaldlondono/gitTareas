from models.model import Venta, Producto, Cliente
from datetime import datetime

def crear_venta(cliente_id, producto_id, cantidad):
    try:
        # Convertir cantidad a entero
        cantidad = int(cantidad)

        # Obtener el producto y cliente
        producto = Producto.get_or_none(Producto.id == int(producto_id))
        cliente = Cliente.get_or_none(Cliente.id == int(cliente_id))

        if not producto:
            print(f"Error: No existe el producto con ID {producto_id}")
            return
        if not cliente:
            print(f"Error: No existe el cliente con ID {cliente_id}")
            return

        # Calcular el total
        total = float(producto.precio) * cantidad

        # Crear la venta
        venta = Venta.create(fecha = datetime.now(),
                             cliente=cliente, 
                             producto=producto, 
                             cantidad=cantidad, 
                             total=total)
        return venta
    except Exception as e:
        print(f"Error al crear la venta: {e}")

def obtener_ventas():
    try:
        ventas = Venta.select()
        return list(ventas)
    except Exception as e:
        print(f"Error al obtener las ventas: {e}")

def eliminar_venta(isSelected):
    try:
        venta = Venta.get(Venta.id == isSelected)
        venta.delete_instance()
        print(f"Venta con ID {isSelected} eliminada.")
    except Exception as e:
        print(f"Error al eliminar la venta: {e}")

def actualizar_venta(isSelected, cliente_id, producto_id, cantidad):
    try:
        venta = Venta.get(Venta.id == isSelected)
        producto = Producto.get(Producto.id == producto_id)
        cliente = Cliente.get(Cliente.id == cliente_id)

        # Calcular el total
        total = producto.precio * cantidad

        # Actualizar la venta
        venta.cliente = cliente
        venta.producto = producto
        venta.cantidad = cantidad
        venta.total = total
        venta.save()
        print(f"Venta con ID {isSelected} actualizada.")
    except Exception as e:
        print(f"Error al actualizar la venta: {e}")


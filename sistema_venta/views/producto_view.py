import customtkinter as ctk
import tkinter as tk  # Importa tkinter para usar Listbox
from controllers.producto_controller import obtener_productos, crear_producto, eliminar_producto, actualizar_producto

class ProductoView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Productos")
        self.geometry("600x400")
        self.resizable(False, False)


        # Lista de productos
        self.productos_listbox = tk.Listbox(self, width=45, height=15)
        self.productos_listbox.place(x=20, y=20)
        self.actualizar_lista_productos()

        # Formulario de nuevo producto
        ctk.CTkLabel(self, text="Nombre:").place(x=340, y=30)
        self.nombre_entry = ctk.CTkEntry(self, width=200)
        self.nombre_entry.place(x=400, y=30)

        ctk.CTkLabel(self, text="Precio:").place(x=340, y=70)
        self.precio_entry = ctk.CTkEntry(self, width=200)
        self.precio_entry.place(x=400, y=70)

        self.agregar_btn = ctk.CTkButton(self, text="Agregar Producto", command=self.agregar_producto)
        self.agregar_btn.place(x=400, y=110)

        self.eliminar_btn = ctk.CTkButton(self, text="Eliminar Seleccionado", command=self.eliminar_producto)
        self.eliminar_btn.place(x=400, y=150)

        # Botón para actualizar el producto seleccionado
        self.actualizar_btn = ctk.CTkButton(self, text="Actualizar Seleccionado", command=self.actualizar_producto)
        self.actualizar_btn.place(x=400, y=190)
        self.producto_seleccionado = None

    def actualizar_producto(self):
        seleccion = self.productos_listbox.curselection()
        if seleccion:
            producto_info = self.productos_listbox.get(seleccion[0])
            producto_id = producto_info.split(" - ")[0]
            nombre = self.nombre_entry.get()
            precio = self.precio_entry.get()
            if nombre and precio:
                # Llama a la función de actualización del controlador
                actualizar_producto(producto_id, nombre, precio)
                self.actualizar_lista_productos()
                self.nombre_entry.delete(0, "end")
                self.precio_entry.delete(0, "end")
        else:
            print("Por favor, selecciona un producto para actualizar.")


    def actualizar_lista_productos(self):
        self.productos_listbox.delete(0, "end")
        productos = obtener_productos()
        for producto in productos:
            self.productos_listbox.insert("end", f"{producto.id} - {producto.nombre} - {producto.precio}")
            
    def agregar_producto(self):
        nombre = self.nombre_entry.get()
        precio = self.precio_entry.get()
        if nombre and precio:
            crear_producto(nombre, precio)
            self.actualizar_lista_productos()
            self.nombre_entry.delete(0, "end")
            self.precio_entry.delete(0, "end")

    def eliminar_producto(self):
        seleccion = self.productos_listbox.curselection()
        if seleccion:
            producto_info = self.productos_listbox.get(seleccion[0])
            producto_id = producto_info.split(" - ")[0]
            eliminar_producto(producto_id)
            self.actualizar_lista_productos()
    
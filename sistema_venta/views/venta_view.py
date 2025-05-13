import customtkinter as ctk
import tkinter as tk
from controllers.venta_controller import obtener_ventas, crear_venta, eliminar_venta, actualizar_venta

class VentaView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Ventas")
        self.geometry("600x400")
        self.resizable(False, False)

        # Lista de ventas
        self.ventas_listbox = tk.Listbox(self, width=45, height=15)
        self.ventas_listbox.place(x=20, y=20)
        self.actualizar_lista_ventas()

        # Formulario de nueva venta
        ctk.CTkLabel(self, text="Cliente ID:").place(x=340, y=30)
        self.cliente_id_entry = ctk.CTkEntry(self, width=200)
        self.cliente_id_entry.place(x=400, y=30)

        ctk.CTkLabel(self, text="Producto ID:").place(x=340, y=70)
        self.producto_id_entry = ctk.CTkEntry(self, width=200)
        self.producto_id_entry.place(x=400, y=70)

        ctk.CTkLabel(self, text="Cantidad:").place(x=340, y=110)
        self.cantidad_entry = ctk.CTkEntry(self, width=200)
        self.cantidad_entry.place(x=400, y=110)

        self.agregar_btn = ctk.CTkButton(self, text="Agregar Venta", command=self.agregar_venta)
        self.agregar_btn.place(x=400, y=150)

        self.eliminar_btn = ctk.CTkButton(self, text="Eliminar Seleccionado", command=self.eliminar_venta)
        self.eliminar_btn.place(x=400, y=200)

    def actualizar_lista_ventas(self):
        self.ventas_listbox.delete(0, "end")
        ventas = obtener_ventas()
        for venta in ventas:
            self.ventas_listbox.insert("end", f"{venta.id} - {venta.cliente.nombre} - {venta.producto.nombre} - {venta.cantidad} - {venta.total}")
   
    def agregar_venta(self):
        cliente_id = self.cliente_id_entry.get()
        producto_id = self.producto_id_entry.get()
        cantidad = self.cantidad_entry.get()
        if cliente_id and producto_id and cantidad:
            crear_venta(cliente_id, producto_id, cantidad)
            self.actualizar_lista_ventas()
            self.cliente_id_entry.delete(0, "end")
            self.producto_id_entry.delete(0, "end")
            self.cantidad_entry.delete(0, "end")

    def eliminar_venta(self):
        seleccion = self.ventas_listbox.curselection()
        if seleccion:
            venta_info = self.ventas_listbox.get(seleccion[0])
            venta_id = venta_info.split(" - ")[0]
            eliminar_venta(venta_id)
            self.actualizar_lista_ventas()

    def actualizar_venta(self):
        seleccion = self.ventas_listbox.curselection()
        if seleccion:
            venta_info = self.ventas_listbox.get(seleccion[0])
            venta_id = venta_info.split(" - ")[0]
            cliente_id = self.cliente_id_entry.get()
            producto_id = self.producto_id_entry.get()
            cantidad = self.cantidad_entry.get()
            if cliente_id and producto_id and cantidad:
                actualizar_venta(venta_id, cliente_id, producto_id, cantidad)
                self.actualizar_lista_ventas()
                self.cliente_id_entry.delete(0, "end")
                self.producto_id_entry.delete(0, "end")
                self.cantidad_entry.delete(0, "end")
        else:
            print("Por favor, selecciona una venta para actualizar.")
                
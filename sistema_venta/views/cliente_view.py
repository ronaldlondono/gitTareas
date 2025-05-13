import customtkinter as ctk
import tkinter as tk  # Importa tkinter para usar Listbox
from controllers.cliente_controller import obtener_clientes, crear_cliente, eliminar_cliente

class ClienteView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Clientes")
        self.geometry("600x400")
        self.resizable(False, False)
        ctk.set_appearance_mode("System")


        # Lista de clientes usando tk.Listbox
        self.clientes_listbox = tk.Listbox(self, width=45, height=15)
        self.clientes_listbox.place(x=20, y=20)
        self.actualizar_lista_clientes()

        # Formulario de nuevo cliente
        ctk.CTkLabel(self, text="Nombre:").place(x=340, y=30)
        self.nombre_entry = ctk.CTkEntry(self, width=200)
        self.nombre_entry.place(x=400, y=30)

        ctk.CTkLabel(self, text="Email:").place(x=340, y=70)
        self.email_entry = ctk.CTkEntry(self, width=200)
        self.email_entry.place(x=400, y=70)

        ctk.CTkLabel(self, text="Teléfono:").place(x=340, y=110)
        self.telefono_entry = ctk.CTkEntry(self, width=200)
        self.telefono_entry.place(x=400, y=110)

        self.agregar_btn = ctk.CTkButton(self, text="Agregar Cliente", command=self.agregar_cliente)
        self.agregar_btn.place(x=400, y=150)

        self.eliminar_btn = ctk.CTkButton(self, text="Eliminar Seleccionado", command=self.eliminar_cliente)
        self.eliminar_btn.place(x=400, y=200)

    def actualizar_lista_clientes(self):
        self.clientes_listbox.delete(0, "end")
        clientes = obtener_clientes()
        for cliente in clientes:
            self.clientes_listbox.insert("end", f"{cliente.id} - {cliente.nombre} - {cliente.email} - {cliente.telefono}")

    def agregar_cliente(self):
        nombre = self.nombre_entry.get()
        email = self.email_entry.get()
        telefono = self.telefono_entry.get()
        if nombre and email and telefono:
            crear_cliente(nombre, email, telefono)
            self.actualizar_lista_clientes()
            self.nombre_entry.delete(0, "end")
            self.email_entry.delete(0, "end")
            self.telefono_entry.delete(0, "end")

    def eliminar_cliente(self):
        seleccion = self.clientes_listbox.curselection()
        if seleccion:
            cliente_info = self.clientes_listbox.get(seleccion[0])
            cliente_id = cliente_info.split(" - ")[0]
            eliminar_cliente(cliente_id)
            self.actualizar_lista_clientes()
import customtkinter as ctk
from views.producto_view import ProductoView
from views.venta_view import VentaView
from views.cliente_view import ClienteView
from PIL import Image


class MainView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestión")
        self.geometry("600x400")
        self.resizable(False, False)

        # Configuración de apariencia
        ctk.set_appearance_mode("System")

        # Centro la ventana
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (600 // 2)
        y = (screen_height // 2) - (400 // 2)
        self.geometry(f"600x400+{x}+{y}")
        self.protocol("WM_DELETE_WINDOW", self.salir)


        # Botones para abrir las vistas
        self.cliente_btn = ctk.CTkButton(self, text="Gestión de Clientes", command=self.abrir_cliente_view)
        self.cliente_btn.place(x=50, y=50)

        self.producto_btn = ctk.CTkButton(self, text="Gestión de Productos", command=self.abrir_producto_view)
        self.producto_btn.place(x=50, y=100)

        self.venta_btn = ctk.CTkButton(self, text="Gestión de Ventas", command=self.abrir_venta_view)
        self.venta_btn.place(x=50, y=150)

        # Agregar una imagen decorativa al lado derecho
    
        try:
            imagen_pil = Image.open("assets/shrek.jpg")
            self.imagen = ctk.CTkImage(imagen_pil, size=(200, 200))
        except Exception as e:
            self.imagen = None  # Si no se encuentra la imagen, no la muestra

        if self.imagen:
            self.imagen_label = ctk.CTkLabel(self, image=self.imagen, text="")
            self.imagen_label.place(x=350, y=80)

    def abrir_cliente_view(self):
        cliente_view = ClienteView()
        cliente_view.mainloop()

    def abrir_producto_view(self):
        producto_view = ProductoView()
        producto_view.mainloop()

    def abrir_venta_view(self):
        venta_view = VentaView()
        venta_view.mainloop()
    
    def salir(self):
        self.destroy()
        self.quit()

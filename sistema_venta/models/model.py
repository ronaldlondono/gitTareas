from peewee import *; import peewee as pw
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'database', 'tienda.db')
# Inicializamos la conexión con la base de datos SQLite
db = SqliteDatabase(DB_PATH)

class BaseModel(pw.Model):
    class Meta:
        database = pw.SqliteDatabase('tienda.db')

class Producto(BaseModel):
    id = pw.AutoField(primary_key=True)
    nombre = pw.CharField(max_length=100, unique=True)
    precio = pw.DecimalField(max_digits=10, decimal_places=2)

class Cliente(BaseModel):
    id = pw.AutoField(primary_key=True)
    nombre = pw.CharField(max_length=100, unique=True)
    email = pw.CharField(max_length=100, unique=True)
    telefono = pw.CharField(max_length=15, unique=True)

class Venta(BaseModel):
    id = pw.AutoField(primary_key=True)
    fecha = pw.DateTimeField()
    cliente = pw.ForeignKeyField(Cliente, backref='ventas')
    producto = pw.ForeignKeyField(Producto, backref='ventas')
    total = pw.DecimalField(max_digits=10, decimal_places=2)
    cantidad = pw.IntegerField()

def create_tables():
    with db:
        db.create_tables([Producto, Cliente, Venta], safe=True)
# app.py
# Servicio de tareas usando Flask, Peewee y PostgreSQL (Render compatible)

from flask import Flask, request, jsonify
from flask_cors import CORS
from peewee import Model, CharField, TextField, BooleanField
from playhouse.db_url import connect
from dotenv import load_dotenv
import os

# Carga variables de entorno desde .env
def load_env():
    from pathlib import Path
    env_path = Path('.') / '.env'
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)

load_env()

# Conexión a la base de datos usando DATABASE_URL
# Ejemplo de URL: postgresql://user:pass@host:port/dbname
DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise RuntimeError("La variable de entorno DATABASE_URL no está definida")

try:
    db = connect(DATABASE_URL)
except Exception as e:
    raise RuntimeError(f"Error al conectar a la base de datos: {e}")


# Modelo base
def setup_models():
    class BaseModel(Model):
        class Meta:
            database = db

    class Tarea(BaseModel):
        titulo = CharField()
        descripcion = TextField(null=True)
        completado = BooleanField(default=False)

    return Tarea

Tarea = setup_models()

# Crear las tablas si no existen
db.connect()
if not db.table_exists('tarea'):
    db.create_tables([Tarea])

# Inicializar Flask
app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def health_check():
    return {"status": "ok", "message": "API corriendo"}

@app.route('/tareas', methods=['POST'])
def crear_tarea():
    data = request.get_json()
    tarea = Tarea.create(
        titulo=data['titulo'],
        descripcion=data.get('descripcion'),
        completado=data.get('completado', False)
    )
    return jsonify(model_to_dict(tarea)), 201

@app.route('/tareas', methods=['GET'])
def obtener_tareas():
    tareas = Tarea.select()
    return jsonify([model_to_dict(t) for t in tareas])

@app.route('/tareas/<int:id>', methods=['GET'])
def obtener_tarea(id):
    try:
        tarea = Tarea.get_by_id(id)
        return jsonify(model_to_dict(tarea))
    except Tarea.DoesNotExist:
        return jsonify({"error": "Tarea no encontrada"}), 404

@app.route('/tareas/<int:id>', methods=['PUT'])
def actualizar_tarea(id):
    try:
        tarea = Tarea.get_by_id(id)
        data = request.get_json()
        tarea.titulo = data.get('titulo', tarea.titulo)
        tarea.descripcion = data.get('descripcion', tarea.descripcion)
        tarea.completado = data.get('completado', tarea.completado)
        tarea.save()
        return jsonify(model_to_dict(tarea))
    except Tarea.DoesNotExist:
        return jsonify({"error": "Tarea no encontrada"}), 404

@app.route('/tareas/<int:id>', methods=['DELETE'])
def eliminar_tarea(id):
    try:
        tarea = Tarea.get_by_id(id)
        tarea.delete_instance()
        return jsonify({"mensaje": "Tarea eliminada correctamente"})
    except Tarea.DoesNotExist:
        return jsonify({"error": "Tarea no encontrada"}), 404

# Función auxiliar para serializar modelos
def model_to_dict(model):
    return {field: getattr(model, field) for field in model._meta.fields}

# Punto de entrada
if __name__ == '__main__':
    # puerto por defecto de Render
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

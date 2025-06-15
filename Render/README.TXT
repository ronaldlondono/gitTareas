# API de Gestión de Tareas

Este proyecto es una API REST para gestionar tareas (to-do list), construida con **Flask**, **Peewee** y **PostgreSQL**. Permite crear, leer, actualizar y eliminar tareas desde cualquier cliente HTTP. Es ideal para despliegues en servicios como **Render**.

## Características

- Crear nuevas tareas con título, descripción y estado de completado.
- Listar todas las tareas existentes.
- Consultar una tarea por su ID.
- Modificar tareas existentes.
- Eliminar tareas por ID.

## Tecnologías utilizadas

- **Python 3**
- **Flask** – Framework web ligero
- **Peewee** – ORM para SQLite/PostgreSQL
- **PostgreSQL** – Base de datos relacional
- **Flask-CORS** – Permite acceso desde otras aplicaciones
- **python-dotenv** – Gestión de variables de entorno
- **Render** – Plataforma de despliegue

## Instalación y ejecución local

1. Clona el repositorio:
   ```sh
   git clone https://github.com/tu-usuario/tu-repo.git
   cd tu-repo

2. Crea y activa un entorno virtual: 
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate

3. Instala las dependencias:
    pip install -r requirements.txt

4. Configura las variables de entorno en un archivo .env:
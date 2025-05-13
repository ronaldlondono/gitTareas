import pyodbc
from controller.controlador import Controlador

if __name__ == "__main__":
    server = "localhost"
    database = "control_inventario"
    username = "root"
    password = "V4qCr_r.t_V!TbN*"
    controlador = Controlador(server, database, username, password)
    #print(pyodbc.drivers())
    controlador.iniciar()
    


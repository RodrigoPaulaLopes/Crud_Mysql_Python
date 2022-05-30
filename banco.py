import mysql.connector

class Banco:
    def __init__(self):
        pass

    @staticmethod
    def criarConexao():
        return mysql.connector.connect(host="localhost", database="teste", user="root", password="root")
    @staticmethod
    def close():
        mysql.connector.close()
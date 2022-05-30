from banco import Banco

class Usuario:

    def __init__(self, id, nome, email, senha):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__senha = senha

    def getId(self):
        return self.__id
    def getNome(self):
        return self.__nome
    def setNome(self, nome):
        self.__nome = nome
    def getEmail(self):
        return self.__email
    def setEmail(self, email):
        self.__email = email
    def getSenha(self):
        return self.__senha
    def setSenha(self, senha):
        self.__senha = senha

from banco import Banco


class UsuarioDao:

    def __init__(self, conexao):
        self.conexao = conexao

    def select(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM usuarios")
        resultado = cursor.fetchall()
        return resultado
    def insert(self, usuario):
        sql = "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)"
        valores = (usuario.getNome(), usuario.getEmail(), usuario.getSenha())
        cursor = self.conexao.cursor()
        cursor.execute(sql, valores)

        self.conexao.commit()
        print("inserido com sucesso")
    def buscarPorId(self, id):
        sql = "SELECT * FROM usuarios WHERE id = %s"
        valores = (id,)
        cursor = self.conexao.cursor()
        cursor.execute(sql, valores)

        resultado = cursor.fetchall()
        return resultado


    def update(self, usuario):
        sql = "UPDATE usuarios SET nome = %s, email = %s, senha = %s WHERE id = %s"
        valores = (usuario.getNome(), usuario.getEmail(), usuario.getSenha(), usuario.getId())
        cursor = self.conexao.cursor()
        cursor.execute(sql, valores)

        self.conexao.commit()
        print("Alterado com sucesso")

    def delete(self, id):
        sql = "DELETE FROM usuarios WHERE id = %s"
        valores = (id, )
        cursor = self.conexao.cursor()
        cursor.execute(sql, valores)

        self.conexao.commit()
        print("Deletado com sucesso")

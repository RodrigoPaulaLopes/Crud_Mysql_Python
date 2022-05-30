from usuariodao import UsuarioDao
from usuario import Usuario
from banco import Banco
import os

print("##########################")
print("   Cadastro de usuarios   ")
print("##########################")


usuariodao = UsuarioDao(Banco.criarConexao())

resposta = 's'
while(resposta == 's'):
    print("Selecione uma opção: ")
    print("1 - ver todos os usuarios: ")
    print("2 - inserir um usuario: ")
    print("3 - editar um usuario: ")
    print("4 - excluir um usuario: ")
    print("5 - para sair do programa: ")
    escolha = int(input("Digite o comando: "))

    if escolha == 5:
        print("Até mais tarde!")
        break
    if escolha == 1:
      usuarios = usuariodao.select()
      for u in usuarios:
          print(f"Id: {u[0]} | Nome: {u[1]} | Email: {u[2]} |  Senha: {u[3]}")
      resposta = input("Deseja continuar? (s/n)")
      if(resposta == 's'):
          continue
      else:
          print("Até mais tarde")
    if escolha == 2:
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")
        senha = input("Digite o senha: ")

        usuario = Usuario(0, nome, email, senha)

        usuariodao.insert(usuario)
        os.system("cls")
    if escolha == 3:
        id = input("Digite o id: ")
        usuarios = usuariodao.buscarPorId(id)

        for u in usuarios:
            print(f"Id: {u[0]} | Nome: {u[1]} | Email: {u[2]} |  Senha: {u[3]}")

        nome = input("Digite o nome: ")
        email = input("Digite o email: ")
        senha = input("Digite o senha: ")

        usuario = Usuario(id, nome, email, senha)
        usuariodao.update(usuario)
    if escolha == 4:

        usuarios = usuariodao.select()
        for u in usuarios:
            print(f"Id: {u[0]} | Nome: {u[1]} | Email: {u[2]} |  Senha: {u[3]}")
        print("---------------------------------------------")
        id = input("Digite o id: ")

        usuariodao.delete(id)







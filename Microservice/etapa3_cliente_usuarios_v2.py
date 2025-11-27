import os 
os.system('clear')

"""
ETAPA 3: RPC com Dados - CLIENTE
================================

Conceito: Cliente interage com dados remotos (CRUD operations).
Create, Read, Update, Delete - tudo remotamente!
"""

import xmlrpc.client

print("=" * 60)
print("ETAPA 3: CLIENTE - GERENCIANDO USUÁRIOS REMOTAMENTE")
print("=" * 60)

def menu():
  print("-" * 60)
  print("Escolha uma das opções:")
  print("=================================")

  print("[1] - Criar usuário")
  print("[2] - Buscar usuário")
  print("[3] - Listar todos os usuários")
  print("[4] - Editar usuário")
  print("[5] - Deletar usuário\n")
  
  print("[0] - Exit")
  return input("\n👉 Digite sua escolha: ")


def title(msg):
    print("\n" + "=" * 60)
    print(f"{msg}")
    print("=" * 60)


def main():
  print("\n🔗 Conectando ao servidor de usuários...")
  try:
    servidor = xmlrpc.client.ServerProxy("http://localhost:8001", allow_none=True)
    print("✅ Conectado!\n")
    
    while True:
      escolha = menu()

      if escolha == "0":
          break
      
      # creating user
      if escolha == "1":
        title("📝 CRIANDO USUÁRIOS")
        
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")

        resposta = servidor.adicionar_usuario(nome, email)
        print(f"[CLIENTE] ✅ {resposta['mensagem']} - ID: {resposta['id']}") # type: ignore
      
      # Reading an user
      elif escolha == "2":
        title("🔍 BUSCANDO USUÁRIOS")

        id_usuario = int(input("Digite o ID do usuário: "))

        print(f"\n[CLIENTE] Buscando usuário {id_usuario}")
        resposta = servidor.buscar_usuario(id_usuario)
        if resposta['sucesso']: # type: ignore
          user = resposta['usuario'] # type: ignore
          print(f"[CLIENTE] ✅ Encontrado: {user['nome']} - {user['email']}") # type: ignore
      
      # Reading all users
      elif escolha == "3":
        title("📝 Listando TODOS os usuários")

        resposta = servidor.listar_usuarios()
        print(f"[CLIENTE] Total: {resposta['total']} usuários\n") # type: ignore
        for user in resposta['usuarios']: # type: ignore
          print(f"  #{user['id']}: {user['nome']} - {user['email']}") # type: ignore
      
      elif escolha == "4":
        # ========================================
        # UPDATE - Atualizar usuário
        # ========================================
        print("\n" + "=" * 60)
        print("✏️  ATUALIZANDO USUÁRIO")
        print("=" * 60)
      
        id_usuario = int(input("Digite o ID do usuário: "))
        novo_nome = input("Digite o novo nome (ou deixe vazio para manter): ")
        novo_email = input("Digite o novo email (ou deixe vazio para manter): ")

        resposta = servidor.atualizar_usuario(
          id_usuario, 
          novo_nome if novo_nome.strip() else None, # type: ignore
          novo_email if novo_email.strip() else None # type: ignore
        )

        if resposta['sucesso']: # type: ignore
          user = resposta['usuario'] # type: ignore
          print(f"[CLIENTE] ✅ Atualizado: {user['nome']} - {user['email']}") # type: ignore
      
      elif escolha == "5":
        # ========================================
        # DELETE - Deletar usuário
        # ========================================
        
        title("🗑️  DELETANDO USUÁRIO")

      
        id_usuario = int(input("Digite o ID do usuário: "))
        print(f"\n[CLIENTE] Deletando usuário ID {id_usuario}")
        resposta = servidor.deletar_usuario(id_usuario)
        print(f"[CLIENTE] ✅ {resposta['mensagem']}") # type: ignore
      else:
        print("Opção inválida")

  except ConnectionRefusedError:
      print("\n❌ ERRO: Servidor não está rodando!")
      print("📝 Execute: python scripts/etapa3_servidor_usuarios.py")
  except Exception as e:
      print(f"\n❌ ERRO: {e}")


if __name__ == "__main__":
    main()

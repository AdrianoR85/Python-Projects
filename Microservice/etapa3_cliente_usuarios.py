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


def main():
    print("\n🔗 Conectando ao servidor de usuários...")
    
    try:
        servidor = xmlrpc.client.ServerProxy("http://localhost:8001")
        print("✅ Conectado!\n")
        
        # ========================================
        # CREATE - Criar usuários
        # ========================================
        print("=" * 60)
        print("📝 CRIANDO USUÁRIOS")
        print("=" * 60)
        
        print("\n[CLIENTE] Criando usuário: João Silva")
        resposta = servidor.adicionar_usuario("João Silva", "joao@email.com")
        print(f"[CLIENTE] ✅ {resposta['mensagem']} - ID: {resposta['id']}") # type: ignore
        id_joao = resposta['id'] # type: ignore
        
        print("\n[CLIENTE] Criando usuário: Maria Santos")
        resposta = servidor.adicionar_usuario("Maria Santos", "maria@email.com")
        print(f"[CLIENTE] ✅ {resposta['mensagem']} - ID: {resposta['id']}") # type: ignore
        id_maria = resposta['id'] # type: ignore
        
        print("\n[CLIENTE] Criando usuário: Pedro Costa")
        resposta = servidor.adicionar_usuario("Pedro Costa", "pedro@email.com")
        print(f"[CLIENTE] ✅ {resposta['mensagem']} - ID: {resposta['id']}") # type: ignore
        
        # ========================================
        # READ - Ler/Buscar usuários
        #🔍 BUSCANDO USUÁRIOS ========================================
        print("\n" + "=" * 60)
        print("")
        print("=" * 60)
        
        print(f"\n[CLIENTE] Buscando usuário ID {id_joao}")
        resposta = servidor.buscar_usuario(id_joao)
        if resposta['sucesso']: # type: ignore
            user = resposta['usuario'] # type: ignore
            print(f"[CLIENTE] ✅ Encontrado: {user['nome']} - {user['email']}") # type: ignore
        
        print("\n[CLIENTE] Listando TODOS os usuários:")
        resposta = servidor.listar_usuarios()
        print(f"[CLIENTE] Total: {resposta['total']} usuários\n") # type: ignore
        for user in resposta['usuarios']: # type: ignore
            print(f"  #{user['id']}: {user['nome']} - {user['email']}") # type: ignore
        
        # ========================================
        # UPDATE - Atualizar usuário
        # ========================================
        print("\n" + "=" * 60)
        print("✏️  ATUALIZANDO USUÁRIO")
        print("=" * 60)
        
        print(f"\n[CLIENTE] Atualizando email de Maria...")
        resposta = servidor.atualizar_usuario(
            id_maria, 
            email="maria.santos@empresa.com" # type: ignore
        )
        if resposta['sucesso']:
            user = resposta['usuario']
            print(f"[CLIENTE] ✅ Atualizado: {user['nome']} - {user['email']}")
        
        # ========================================
        # DELETE - Deletar usuário
        # ========================================
        print("\n" + "=" * 60)
        print("🗑️  DELETANDO USUÁRIO")
        print("=" * 60)
        
        print(f"\n[CLIENTE] Deletando usuário ID {id_joao}")
        resposta = servidor.deletar_usuario(id_joao)
        print(f"[CLIENTE] ✅ {resposta['mensagem']}") # type: ignore
        
        print("\n[CLIENTE] Listando usuários restantes:")
        resposta = servidor.listar_usuarios()
        print(f"[CLIENTE] Total: {resposta['total']} usuários\n")# type: ignore
        for user in resposta['usuarios']: # type: ignore
            print(f"  #{user['id']}: {user['nome']} - {user['email']}")# type: ignore
        
        # ========================================
        # CONCEITOS IMPORTANTES
        # ========================================
        print("\n" + "=" * 60)
        print("💡 CONCEITOS IMPORTANTES")
        print("=" * 60)
        
        print("\n✓ Dados ficam NO SERVIDOR (não no cliente)")
        print("✓ Cliente faz requisições para manipular dados")
        print("✓ Múltiplos clientes veem os MESMOS dados")
        print("✓ Se reiniciar o cliente, dados continuam no servidor")
        print("\n📖 Do PDF (página 13):")
        print("   'Objeto distribuído pode ser acessado remotamente")
        print("    de qualquer lugar da rede'")
        
        print("\n✅ ETAPA 3 COMPLETA!")
        print("📚 Próximo: Etapa 4 - Microsserviços (HTTP)")
        print("   Execute: python scripts/etapa4_servico_usuarios.py")
        print("=" * 60)
        
    except ConnectionRefusedError:
        print("\n❌ ERRO: Servidor não está rodando!")
        print("📝 Execute: python scripts/etapa3_servidor_usuarios.py")
    except Exception as e:
        print(f"\n❌ ERRO: {e}")


if __name__ == "__main__":
    main()

"""
ETAPA 3: RPC com Dados - SERVIDOR de Usuários
==============================================

Conceito: Agora o servidor gerencia DADOS (não só cálculos).
Múltiplos clientes podem acessar e modificar os mesmos dados!

Baseado no conceito de RMI do PDF (páginas 13-14):
"Objetos distribuídos que podem ser acessados remotamente"
"""

from xmlrpc.server import SimpleXMLRPCServer
import time

print("=" * 60)
print("ETAPA 3: SERVIDOR RPC - SISTEMA DE USUÁRIOS")
print("=" * 60)


class ServicoUsuarios:
    """
    Serviço que gerencia usuários remotamente.
    Similar ao conceito de objeto distribuído (PDF página 12)
    """
    
    def __init__(self):
        # "Banco de dados" em memória - compartilhado entre todos os clientes!
        self.usuarios = {}
        self.proximo_id = 1
        print("\n💾 Banco de dados de usuários iniciado (em memória)")
    
    def adicionar_usuario(self, nome, email):
        """Adiciona um novo usuário"""
        print(f"\n[SERVIDOR] 📨 Requisição: adicionar_usuario({nome}, {email})")
        time.sleep(10)
        user_id = self.proximo_id
        self.proximo_id += 1
        
        self.usuarios[user_id] = {
            "id": user_id,
            "nome": nome,
            "email": email
        }
        
        print(f"[SERVIDOR] ✅ Usuário #{user_id} criado com sucesso")
        print(f"[SERVIDOR] 📊 Total de usuários: {len(self.usuarios)}")
        
        return {"sucesso": True, "id": user_id, "mensagem": "Usuário criado!"}
    
    def buscar_usuario(self, user_id):
        """Busca um usuário pelo ID"""
        print(f"\n[SERVIDOR] 📨 Requisição: buscar_usuario({user_id})")
        
        time.sleep(10)

        if user_id in self.usuarios:
            usuario = self.usuarios[user_id]
            print(f"[SERVIDOR] ✅ Usuário encontrado: {usuario['nome']}")
            return {"sucesso": True, "usuario": usuario}
        else:
            print(f"[SERVIDOR] ❌ Usuário #{user_id} não encontrado")
            return {"sucesso": False, "mensagem": "Usuário não encontrado"}
    
    def listar_usuarios(self):
        """Lista todos os usuários"""
        print(f"\n[SERVIDOR] 📨 Requisição: listar_usuarios()")
        print(f"[SERVIDOR] 📊 Retornando {len(self.usuarios)} usuários")
        
        time.sleep(10)

        return {
            "sucesso": True,
            "total": len(self.usuarios),
            "usuarios": list(self.usuarios.values())
        }
    
    def atualizar_usuario(self, user_id, nome=None, email=None):
        """Atualiza dados de um usuário"""
        print(f"\n[SERVIDOR] 📨 Requisição: atualizar_usuario({user_id})")
        
        time.sleep(10)

        if user_id not in self.usuarios:
            print(f"[SERVIDOR] ❌ Usuário #{user_id} não encontrado")
            return {"sucesso": False, "mensagem": "Usuário não encontrado"}
        
        if nome:
            self.usuarios[user_id]["nome"] = nome
        if email:
            self.usuarios[user_id]["email"] = email
        
        print(f"[SERVIDOR] ✅ Usuário #{user_id} atualizado")
        return {"sucesso": True, "usuario": self.usuarios[user_id]}
    
    def deletar_usuario(self, user_id):
        """Remove um usuário"""
        print(f"\n[SERVIDOR] 📨 Requisição: deletar_usuario({user_id})")
        
        time.sleep(10)
        
        if user_id in self.usuarios:
            del self.usuarios[user_id]
            print(f"[SERVIDOR] ✅ Usuário #{user_id} deletado")
            print(f"[SERVIDOR] 📊 Total de usuários: {len(self.usuarios)}")
            return {"sucesso": True, "mensagem": "Usuário deletado"}
        else:
            print(f"[SERVIDOR] ❌ Usuário #{user_id} não encontrado")
            return {"sucesso": False, "mensagem": "Usuário não encontrado"}


def iniciar_servidor():
    """Inicia o servidor RPC na porta 8001"""
    
    servidor = SimpleXMLRPCServer(
        ("localhost", 8001),
        allow_none=True,
        logRequests=False
    )
    
    # Registra o serviço de usuários
    servidor.register_instance(ServicoUsuarios())
    
    print("\n🚀 Servidor de Usuários iniciado!")
    print("📍 Endereço: http://localhost:8001")
    print("\n💡 Conceito importante:")
    print("   - Dados ficam NO SERVIDOR")
    print("   - MÚLTIPLOS clientes podem acessar os mesmos dados")
    print("   - Clientes não guardam dados, só fazem requisições")
    print("\n⏳ Aguardando requisições...")
    print("   (Execute etapa3_cliente_usuarios.py em outro terminal)")
    print("\n💪 Experimente:")
    print("   - Abra 2 ou 3 clientes ao mesmo tempo")
    print("   - Veja eles compartilhando os mesmos usuários!")
    print("=" * 60)
    
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\n\n🛑 Servidor encerrado!")


if __name__ == "__main__":
    iniciar_servidor()

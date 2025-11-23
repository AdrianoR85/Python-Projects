import os
import xmlrpc.client
os.system('clear')

"""
  ETAPA 2: RPC - CLIENTE (Faz chamadas remotas)
  ==============================================

  Conceito: Este é o CLIENTE que chama funções no SERVIDOR remoto

  Baseado página 6 do matérial de estudo.
  "O cliente envia mensagem ao servidor requisitando um procedimento.
  O cliente fica BLOQUADO até receber resposta."
"""

print("=" * 60)
print("ETAPA 2: CHAMADA RPC = FAZENDO CHAMADAS REMOTAS")
print("=" * 60)

def main():
  # Conecta ao servidor remoto
  print("\n🔗 Conectando ao servidor remoto...")
  print("     Endereço: http://localhost:8000")

  try:
    # Criar conexão com o servidor 
    servidor = xmlrpc.client.ServerProxy("http://localhost:8000")
    print("✅ conexão estabelecida!\n")

    # ==================================
    # TESTE 1: Soma Remota
    # ==================================
    print("=" * 60)
    print("TESTE 1: Chamada Remota - somar(10, 20)")
    print("=" * 60)

    print("\n[CLIENTE] Enviando requisição: somar(10, 20)")
    print("[CLIENTE] ⏸️  Cliente BLOQUEADO (aguardando resposta)...")

    # CHAMADA REMOTA - função está em OUTRO computador!
    resultado = servidor.somar(10,20)
    print(f"[CLIENTE] 📥 Resposta recebida: {resultado}")
    print("[CLIENTE] ▶️  Cliente DESBLOQUEADO (continua execução)")

    # ========================================
    # TESTE 2: Múltiplas operações
    # ========================================
    print("\n" + "=" * 60)
    print("TESTE 2: Múltiplas Operações Remotas")
    print("=" * 60)
    
    print("\n[CLIENTE] Requisição: subtrair(100, 30)")
    resultado = servidor.subtrair(100, 30)
    print(f"[CLIENTE] Resposta: {resultado}\n")
        
    print("[CLIENTE] Requisição: multiplicar(5, 8)")
    resultado = servidor.multiplicar(5, 8)
    print(f"[CLIENTE] Resposta: {resultado}")
    
    # ========================================
    # TESTE 3: Aumento salarial (como Etapa 1, mas REMOTO!)
    # ========================================
    print("\n" + "=" * 60)
    print("TESTE 3: Cálculo Remoto de Salário")
    print("=" * 60)
    
    print("\n[CLIENTE] Requisição: calcular_aumento_salario(5000, 10)")
    novo_salario = servidor.calcular_aumento_salario(5000, 10)
    print(f"[CLIENTE] Novo salário: R$ {novo_salario:.2f}")

    # ========================================
    # COMPARAÇÃO COM ETAPA 1
    # ========================================
    print("\n" + "=" * 60)
    print("🔍 COMPARAÇÃO: Etapa 1 vs Etapa 2")
    print("=" * 60)
    print("\nETAPA 1 (Local):")
    print("  ✓ Função na MESMA máquina")
    print("  ✓ Comunicação via MEMÓRIA (muito rápido)")
    print("  ✓ Sem rede, sem servidor")
    
    print("\nETAPA 2 (Remota - RPC):")
    print("  ✓ Função em OUTRA máquina (servidor)")
    print("  ✓ Comunicação via REDE (mais lento)")
    print("  ✓ Cliente fica BLOQUEADO esperando resposta")
    print("  ✓ Servidor pode estar em outro país!")
    
    print("\n📖 Do PDF (página 8):")
    print("   'Desempenho: chamadas remotas operam em")
    print("    velocidade mais reduzida que chamadas locais'")
    
    print("\n✅ ETAPA 2 COMPLETA!")
    print("📚 Próximo: Etapa 3 - RPC com dados (sistema de usuários)")
    print("   Execute: python scripts/etapa3_servidor_usuarios.py")
    print("=" * 60)
      
  except ConnectionRefusedError:
    print("\n❌ ERRO: Não foi possível conectar ao servidor!")
    print("📝 Certifique-se de que o servidor está rodando:")
    print("   python3 Microservice/etapa2_servidor.py")
  except Exception as e:
    print(f"\n❌ ERRO: {e}")

if __name__ == "__main__":
    main()
import os
os.system('clear')

"""
ETAPA 2: RPC - SERVIDOR (Calculadora Remota)
============================================

Conceito: Este é o SERVIDOR que vai receber chamadas REMOTAS.

Baseado no PDF página 5:
"RPC possibilita que um programa chame um procedimento em OUTRO espaço 
de endereço (outro computador na rede)"
"""

from xmlrpc.server import SimpleXMLRPCServer
import time

print("=" * 60)
print("ETAPA 2: SERVIDOR RPC - CALCULADORA REMOTA")
print("=" * 60)

class CalculadoraRemota:
  """
  Classe com métodos que serão chamados REMOTAMENTE
  Similar ao exemplo RMI do PDF (páginas 18-22)
  """
  
  def somar(self, a, b):
    """Operação remota: soma dois números"""
    print(f"\n[SERVIDOR] 📨 Requisição recebida: somar({a}, {b})")
    print(f"[SERVIDOR] ⚙️  Processando...")
    time.sleep(20)  # Simula processamento
    resultado = a + b
    print(f"[SERVIDOR] ✅ Resultado calculado: {resultado}")
    print(f"[SERVIDOR] 📤 Enviando resposta ao cliente...")
    return resultado
  
  def subtrair(self, a, b):
    """Operação remota: subtrai dois números"""
    print(f"\n[SERVIDOR] 📨 Requisição recebida: subtrair({a}, {b})")
    time.sleep(20)  # Simula processamento
    resultado = a - b
    print(f"[SERVIDOR] ✅ Resultado: {resultado}")
    return resultado
  
  def multiplicar(self, a, b):
    """Operação remota: multiplica dois números"""
    print(f"\n[SERVIDOR] 📨 Requisição recebida: multiplicar({a}, {b})")
    time.sleep(20)  # Simula processamento
    resultado = a * b
    print(f"[SERVIDOR] ✅ Resultado: {resultado}")
    return resultado
  
  def calcular_aumento_salario(self, salario, percentual):
    """
    A MESMA função da Etapa 1, mas agora REMOTA!
    Compare com etapa1_local.py
    """
    print(f"\n[SERVIDOR] 📨 Requisição: calcular_aumento_salario({salario}, {percentual}%)")
    print(f"[SERVIDOR] ⚙️  Processando aumento salarial...")
    time.sleep(20)
    novo_salario = salario * (1 + percentual / 100)
    print(f"[SERVIDOR] ✅ Novo salário: R$ {novo_salario:.2f}")
    return novo_salario


def iniciar_servidor():
  """Inicia o servidor RPC na porta 8000"""

  # Criar servidor na porta 8000
  servidor = SimpleXMLRPCServer(
    ("localhost", 8000),
    allow_none=True,
    logRequests=False # Desativar logs automáticos
  )

  # Registra a calculadora para ser acessada remotamente
  servidor.register_instance(CalculadoraRemota())
  print("\n🚀 Servidor RPC iniciado!")
  print("📍 Endereço: http://localhost:8000")
  print("\n📖 Conceito (PDF página 6):")
  print("   'O servidor fica em estado de ESPERA até que")
  print("    uma mensagem de requisição seja recebida'")
  print("\n⏳ Aguardando requisições dos clientes...")
  print("   (Execute etapa2_cliente.py em outro terminal)")
  print("=" * 60)

  # Loop infinito aguardando requisição
  try:
    servidor.serve_forever()
  except KeyboardInterrupt:
    print("\n\n🛑 Servidor encerrado!")


if __name__ == "__main__":
  iniciar_servidor()
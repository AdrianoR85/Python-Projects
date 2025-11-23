import os
os.system('clear')

"""
  ETAPA 1: CHAMADA Local de Função
  ================================

  Conceito: Função está na MESMA máquina, tudo acontece localmente.

  "Uma rotina A coloca argumentos na memória e transfere controle para um procedimento P, que processa e retorna o resultado"
"""

print("=" * 60)
print("ETAPA 1: CHAMADA LOCAL DA FUNÇÃO")
print("=" * 60)

# Este é o procedimento da função local
def calcular_aumento_salario(salario_atual, percentual):
  """
    Função que calcula o novo salário com aumento
    Está na MESMA máquina, MESMA memória
  """
  print(f"\n[PROCEDIMENTO] Recebendo: R$ {salario_atual}, aumento de {percentual}%")

  #Processa o cálculo
  novo_salario = salario_atual * (1 + percentual / 100)

  return novo_salario


# Está é a ROTINA A (quem chama a função)
def main():
  print("\n[ROTINA A] Iniciando...")

  # Dados na memória local
  salario = 5000.00
  aumento = 10

  print(f"[ROTINA A] Salário atual: R$ {salario}")
  print(f"[ROTINA A] Aumento: {aumento}%")

  # CHAMADA LOCAL - função está na mesma máquina
  print("\n[ROTINA A] Chamando procedimento local...")
  resultado = calcular_aumento_salario(salario, aumento)

  # Recebe o resultado da memória local
  print(f"\n[ROTINA A] Resultado recebido: R$ {resultado:.2f}")

  print("\n" + "=" * 60)
  print("OBSERVAÇÃO")
  print("- Tudo acontece na MESMA máquina")
  print("- Comunicação via MEMÓRIA RAM (rápida)")
  print("- Sem rede, sem servidorm sem cliente")
  print("=" * 60)

if __name__ == "__main__":
  
  main()

  print("\n ETAPA 1 COMPLETA")
  print("Próximo: Etapa 2 - Transformar isso em chamada REMOTA (RPC)")
  print("Executar: python3 Microservice/etapa1_local.py")
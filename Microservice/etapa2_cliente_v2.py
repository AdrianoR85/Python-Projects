import os
import time
import xmlrpc.client

os.system('clear')

print("=" * 60)
print("ETAPA 2: CLIENTE RPC - Modo Interativo")
print("=" * 60)

def menu():
  print("-" * 60)
  print("\n📌 Escolha uma operação:")
  print("1 - Somar")
  print("2 - Subtrair")
  print("3 - Multiplicar")
  print("4 - Calcular aumento salarial")
  print("0 - Sair")
  return input("\n👉 Digite sua escolha: ")

def main():
  print("\n🔗 Conectando ao servidor RPC...")
  time.sleep(10)
  servidor = xmlrpc.client.ServerProxy("http://localhost:8000")
  print("✅ Conexão estabelecida!\n")

  while True:
    escolha = menu()

    if escolha == "0":
      print("\n👋 Encerrando cliente... até mais!")
      break
    
    try:
      if escolha in ["1", "2", "3"]:
        a = float(input("\nDigite o primeiro número: "))
        b = float(input("Digite o segundo número: "))

        print("\n⏳ Enviando requisição ao servidor... aguardando resposta...")

        operacao = ''
        resultado = 0

        if escolha == '1':
          resultado = servidor.somar(a, b)
          operacao = "Soma"
        elif escolha == '2':
          resultado = servidor.subtrair(a, b)
          operacao = "Subtrair"
        elif escolha == "3":
          resultado = servidor.multiplicar(a, b)
          operacao = "Multiplicação"
        
        print(f"\n📥 Resultado ({operacao}): {resultado}")
      
      elif escolha == "4":
        salario = float(input("\nDigite o salário atual: R$ "))
        percentual = float(input("Digite o percentual de aumento: "))

        print("\n⏳ Processando...")

        novo_salario = servidor.calcular_aumento_salario(salario, percentual)
        print(f"\n📥 Novo salário calculado: R$ {novo_salario:.2f}")

      else:
                print("\n⚠️ Opção inválida! Tente novamente.")  
    except Exception as e:
      print(f"\n❌ Erro durante requisição RPC: {e}")

if __name__ == "__main__":
  main()
# ========== Sequencia de fibonacci ==========
print("="*15,  end=' ')
print("Sequencia de fibonacci ", end='')
print("="*15)
valorSequencial = int(input("Valor para a sequencia: "))
valorInicial = 0
valorDois = 1
valorFinal = 2
print(f" {valorInicial} -> {valorDois}", end='')
for i in range(valorSequencial):
    print(f" -> {valorFinal} ", end='')
    valorInicial = valorDois
    valorDois = valorFinal
    valorFinal = valorInicial + valorDois




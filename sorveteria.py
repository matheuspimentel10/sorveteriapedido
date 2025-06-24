print("Seja bem-vindo à nossa sorveteria!")

# Exibe o menu
print("\nCardápio de Sorvetes:")
print("-" * 35)
print("SABOR      | TAMANHO | PREÇO")
print("Pistache   | P       | R$  9.00")
print("Pistache   | M       | R$ 14.00")
print("Pistache   | G       | R$ 18.00")
print("Baunilha   | P       | R$ 11.00")
print("Baunilha   | M       | R$ 16.00")
print("Baunilha   | G       | R$ 20.00")
print("-" * 35)

# Total acumulado
total = 0

continuar = True

while continuar:
    # Solicita o sabor
    sabor = input("\nDigite o sabor (PE para Pistache ou BA para Baunilha): ").upper()

    if sabor not in ['PE', 'BA']:
        print("Sabor inválido. Tente novamente.")
        continue

    # Solicita o tamanho
    tamanho = input("Digite o tamanho (P/M/G): ").upper()

    if tamanho not in ['P', 'M', 'G']:
        print("Tamanho inválido. Tente novamente.")
        continue

    # Define o preço com base no sabor e tamanho
    preco = 0
    if sabor == 'PE':
        if tamanho == 'P':
            preco = 9
        elif tamanho == 'M':
            preco = 14
        elif tamanho == 'G':
            preco = 18
    elif sabor == 'BA':
        if tamanho == 'P':
            preco = 11
        elif tamanho == 'M':
            preco = 16
        elif tamanho == 'G':
            preco = 20

    total += preco

    print(f"Item adicionado! Total atual da compra: R$ {total:.2f}")

    # Pergunta se deseja continuar
    resposta = input("Deseja adicionar mais algo? (s/n): ").lower()
    if resposta != 's':
        continuar = False

# Exibe o valor final da compra
print(f"\nValor final da compra: R$ {total:.2f}")
print("Obrigado por comprar conosco!")
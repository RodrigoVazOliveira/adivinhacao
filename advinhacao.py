print("=================================")
print("Bem vindo ao jogo de adivinhacao!")
print("=================================")

numeric_secret = 42
numeric_user = int(input("Digite um o seu numero: "))

print("Voce digitou ", numeric_user)
accept = numeric_secret == numeric_user
numeric_great = numeric_user > numeric_secret
numeric_minor = numeric_user < numeric_secret

if accept:
    print("Voce acertou!")
else:
    if numeric_great:
        print("Maior que o numero do sorteio")
    elif numeric_minor:
        print("O numero e o menor que sorteio")

print("Fim do jogo!")
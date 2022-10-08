print("Bem vindo ao jogo de adivinhacao!")
print("=================================")

numeric_secret = 42
numeric_user = int(input("Digite um o seu numero: "))

print("Voce digitou ", numeric_user)
if numeric_secret == numeric_user:
    print("Voce acertou!")
else:
    print("Voce errou!")

print("Fim do jogo!")
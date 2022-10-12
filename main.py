import advinhacao
import user_system

print("========================================")
print("========== Bem vindo ===================")
print("========================================")

print("Escolha o jogo")
print("(1) Adivinhacao\n(2) Verificar usuario do sistema")
number_game = int(input("Por favor, digite a sua escolha: "))

if number_game == 1:
    advinhacao.advinha()
elif number_game == 2:
    user_system.check_user()

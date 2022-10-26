# coding: utf-8
def switch_fruits():
    fruits = ['Banana', 'Macã', 'Pera', 'Uva', 'Melancia', 'Jamelao']
    fruits_requested = input("Qual a fruta que deseja consultar? ")

    if fruits_requested in fruits:
        print("Sim, temos a fruta.")
    else:
        print("Não temos a fruta.")


def check_index_fruits():
    fruits = ['Banana', 'Macã', 'Pera', 'Uva', 'Melancia', 'Jamelao']
    fruits_search = "Melancia"

    if fruits_search in fruits:
        print("o index da fruta e {}".format(fruits.index(fruits_search)))
    else:
        print("Desculpa, a {} não está na lista frutas".format(fruits_search))

def main_program():
    print("| =================== BEM VINDO ==================|")
    print("1. Consultar uma fruta.")
    print("2. verificar index de fruta")
    numeric_option = int(input("Digite uma das duas opcões: "))

    if numeric_option == 1:
        switch_fruits()
    elif numeric_option == 2:
        check_index_fruits()
    else:
        print("Opcão inválida!")


if __name__ == "__main__":
    main_program()

# coding: utf-8
def switch_fruits():
    fruits = ['Banana', 'Macã', 'Pera', 'Uva', 'Melancia', 'Jamelao']
    fruits_requested = input("Qual a fruta que deseja consultar? ")

    if fruits_requested in fruits:
        print("Sim, temos a fruta.")
    else:
        print("Não temos a fruta.")


if __name__ == "__main__":
    switch_fruits()

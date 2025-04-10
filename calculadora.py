
# Calculadora Científica em Python

import math

def menu():
    print("Selecione a operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potência")
    print("6 - Raiz Quadrada")
    print("7 - Logaritmo")
    print("8 - Seno")
    print("9 - Cosseno")
    print("10 - Tangente")
    print("0 - Sair")

def calculadora():
    while True:
        menu()
        escolha = input("Digite a opção: ")
        
        if escolha == '0':
            print("Encerrando...")
            break

        if escolha in ['1', '2', '3', '4', '5']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            
            if escolha == '1':
                print("Resultado:", num1 + num2)
            elif escolha == '2':
                print("Resultado:", num1 - num2)
            elif escolha == '3':
                print("Resultado:", num1 * num2)
            elif escolha == '4':
                if num2 != 0:
                    print("Resultado:", num1 / num2)
                else:
                    print("Erro: divisão por zero.")
            elif escolha == '5':
                print("Resultado:", math.pow(num1, num2))
        
        elif escolha == '6':
            num = float(input("Digite o número: "))
            if num >= 0:
                print("Resultado:", math.sqrt(num))
            else:
                print("Erro: raiz quadrada de número negativo.")
        
        elif escolha == '7':
            num = float(input("Digite o número: "))
            if num > 0:
                print("Resultado:", math.log(num))
            else:
                print("Erro: logaritmo de número não positivo.")
        
        elif escolha in ['8', '9', '10']:
            angulo = float(input("Digite o ângulo em graus: "))
            rad = math.radians(angulo)
            
            if escolha == '8':
                print("Resultado:", math.sin(rad))
            elif escolha == '9':
                print("Resultado:", math.cos(rad))
            elif escolha == '10':
                print("Resultado:", math.tan(rad))
        
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    calculadora()

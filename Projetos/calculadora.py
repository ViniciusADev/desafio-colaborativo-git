print('///BEM VINDO A CALCULADORA CIENTÍFICA///')

menu = (
             "\nID das funções da calculadora científica\n"
             "|1-  Soma(+)         |2- Subtração(-) |\n"   
             "|3- Multiplicação(X) |4- Divisão(÷)   |\n")
print(menu)


while True:                                                                     
    try:                                                                        
        id = input('Digite o ID(Digite "0" para sair | Digite "m" ou "M" ver o menu novamente): ')

        if id == "0":
            print("\nSaindo... Tchau:\n")
            break                                                               
        elif id == "m" or id == "M": 
            print(menu)

        elif id == "1":   
            num1 = int(input("Digite o primeiro número: "))
            num2 = int(input("Digite o segundo número: "))
            resultado_soma = num1 + num2
            print(f"O resultado da sua soma é: {resultado_soma}")

        elif id == "2":   
            # Subtração (ID: 2)
            pass

        elif id == "3":   
            # Multiplicação (ID: 3)
            pass
            
        elif id == "4":   
            # Divisão (ID: 4)
            pass

        else:
            print("\nDigite um dos ID´s da tabela acima \n")
            print('Caso esteja tentando acessar o menu use "m" ou "M"\n')

    except ValueError:                                                            
          print('Você digitou algum valor não numerico ou colocou "," para números rais tente colocar ".". Tente novamente, vai da certo!\n')

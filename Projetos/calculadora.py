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
            num1 = int(input(f"\n Digite o primeiro número: \n "))
            num2 = int(input(f"\n Digite o segundo número: \n "))
            resultado_soma = num1 + num2
            print(f"\n O resultado da soma realizada é: {resultado_soma} \n")

        elif id == "2":   
            # Subtração (ID: 2)
            pass

        elif id == "3":   
            # Multiplicação (ID: 3)
            pass
            
        elif id == "4":   
          git 


        else:
            print("\nDigite um dos ID´s da tabela acima \n")
            print('Caso esteja tentando acessar o menu use "m" ou "M"\n')

    except ValueError:                                                            
          print('Você digitou algum valor não numerico ou colocou "," para números rais tente colocar ".". Tente novamente, vai da certo!\n')

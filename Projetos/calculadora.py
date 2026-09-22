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
            print("\nSaindo... Tchau:)\n")
            break                                                               
        elif id == "m" or id == "M": 
            print(menu)

        elif id == "1":   
            # Soma (ID: 1)
            pass

        elif id == "2":   
            # Subtração (ID: 2)
            pass

        elif id == "3":   
            # Multiplicação (ID: 3)
            pass
            
        elif id == "4":   
          num1 =int(input ("\nDigite o primeiro número: \n"))
          num2 =int(input ("\nDigite o segundo número: \n"))
          resultado_div = num1 / num2
         print("O resultado da operação e igual a" , resultado_div)

          


        else:
            print("\nDigite um dos ID´s da tabela acima \n")
            print('Caso esteja tentando acessar o menu use "m" ou "M"\n')

    except ValueError:                                                            
          print('Você digitou algum valor não numerico ou colocou "," para números rais tente colocar ".". Tente novamente, vai da certo!\n')

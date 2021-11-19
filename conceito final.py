print('CONCEITO FINAL') #Nome do programa
print('Escolha a opcção que deseja\n1 - Iniciar programa\n2 - Encerrar programa')
opcao = int(input('Qual opção você deseja - 1 ou 2: ')) #Opção a ser escolhida)

while True: #Loop proposital
    if (opcao == 1):
        nome = input('Digite o nome do aluno: ')
        nota = float(input('Digite a nota do aluno: '))
        if (nota < 0 or nota >10):
            print('Nota inválida. Encerrando o programa...')
            break
        elif (0 <= nota <= 2.9):
            conceito = 'E'
            print('Nome do aluno: {}' .format(nome))
            print('Nota final: {}' .format(nota))
            print('Conceito final: {}' .format(conceito))
            break
        elif (3 <= nota <= 4.9):
            conceito = 'D'
            print('Nome do aluno: {}' .format(nome))
            print('Nota final: {}' .format(nota))
            print('Conceito final: {}' .format(conceito))
            break
        elif (5 <= nota <= 6.9):
            conceito = 'C'
            print('Nome do aluno: {}' .format(nome))
            print('Nota final: {}' .format(nota))
            print('Conceito final: {}' .format(conceito))
            break
        elif (7 <= nota <= 8.9):
            conceito = 'B'
            print('Nome do aluno: {}' .format(nome))
            print('Nota final: {}' .format(nota))
            print('Conceito final: {}' .format(conceito))
            break
        elif (9 <= nota <= 10):
            conceito = 'A'
            print('Nome do aluno: {}' .format(nome))
            print('Nota final: {}' .format(nota))
            print('Conceito final: {}' .format(conceito))
            break   
    elif (opcao == 2):
        print('Encerrando o programa ...')
        break
    else:
        print('Opcão inválida. Encerrando o programa')
        break
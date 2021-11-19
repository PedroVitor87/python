print('CALCULADORA')
print('Escolha a operação desejada:')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')

while True:
    print('Para encerrar o programa digite:\nsair')
    op = input('Qual operação deseja fazer? ')
    
    if op == '+' or op == '-' or op == '*' or op == '/':
        x = int(input('Digite um número: '))
        y = int(input('Digite outro número: '))
    if (op == '+'):
        res = x + y
        print('Resultado: {} + {} = {}' .format(x,y,res))
        continue
    elif (op == '-'):
        res = x - y
        print('Resultado: {} - {} = {}' .format(x,y,res))
        continue
    elif (op == '*'):
        res = x * y
        print('Resultado: {} * {} = {}' .format(x,y,res))
        continue
    elif (op == '/'):
        res = x / y
        print('Resultado: {} / {} = {}' .format(x,y,res))
        continue
    elif (op == 'sair'):
        print('Encerrando o programa ...')
        break
    else:
        print('Operação inválida')
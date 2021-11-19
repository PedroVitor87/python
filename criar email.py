def criarEmail(nome, sobrenome, telefone):
    email = nome[0].lower() + sobrenome.lower() + telefone + '@algoritmos.com.br'
    print('Sra. {} {}, seu e-mail é {}'.format(nome, sobrenome, email))

nome = (input('Digite o seu nome: '))
sobrenome = (input('Digite o seu sobrenome: '))
telefone = (input('Digite os dois últimos dígitos do seu número de telefone: '))

criarEmail(nome, sobrenome, telefone)
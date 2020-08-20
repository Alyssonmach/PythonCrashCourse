# recebendo entradas e mostrandos as saídas ao usuário

# especificar o tipo de dado a ser recebido é uma boa prática
# a entrada padrão é uma string
name = str(input('Qual o seu nome? '))
age = int(input('Qual a sua idade? '))

# mostrando os dados de saída ao usuário

print('Olá {}, você tem {} anos!'.format(name, age))

# aspas em strings não são problemas para o python!

print('\nAspas simples')
print("Aspas duplas")
print('''Aspas triplas''')

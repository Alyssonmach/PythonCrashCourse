# concatenar strings é muito fácil em python.

nome1 = 'Alysson '
nome2 = 'Machado'

nome = nome1 + nome2
print(nome, '\n')

# uma string é armazenada dessa forma:

nome = ['A', 'l', 'y', 's', 's', 'o', 'n', ' ', 'M', 'a', 'c', 'h', 'a', 'd', 'o']
print(nome, '\n')

# Nós podemos ver apenas algumas letras

nome = 'Alysson Machado'
print(nome[0], '\n')

# Você pode selecionar partes de strings

print(nome[0:7] + nome[7:15], '\n')

# Verificar se uma string é um palíndromo é muito fácil em python

print(nome[::-1], '\n')

# o python possui uma série de funções prontas para serem usadas!

print(nome.lower(), nome.upper(), nome.title())

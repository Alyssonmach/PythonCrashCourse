# Tipos de dados booleanos são representados em dois estados diferentes: 
# 1 ou 0 (verdadeiro ou falso)

ativado = True
desativado = False

print(ativado)
print(desativado, '\n')

# também há o estado de negação e as disjunções lógicas (e/ou)

print(not ativado)
print(not desativado, '\n')

print(ativado and desativado)
print(ativado and ativado)
print(desativado and desativado, '\n')

print(ativado or desativado)
print(ativado or ativado)
print(desativado or desativado, '\n')

# operadores matemáticos podem ser usados

print(7 > 5)
print(7 < 5, '\n')

print(ativado == ativado)
print(ativado != desativado, '\n')

print(7 <= 7)
print(8 >= 9)




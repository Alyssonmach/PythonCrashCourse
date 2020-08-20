# concatenating string is a very easy task in python.

name1 = 'Alysson'
name2 = 'Machado'

name = name1 + name2
print(name, '\n')

# a string is stored this way:

name = ['A', 'l', 'y', 's', 's', 'o', 'n', ' ', 'M', 'a', 'c', 'h', 'a', 'd', 'o']
print(name, '\n')

# we can see just a few letters.

name = 'Alysson Machado'
print(name[0], '\n')

# you can also select parts of the string.

print(name[0:7] + name[7:15], '\n')

# have you ever seen a palindrome? in python check this is very trivial:

print(name[::-1], '\n')

# testing functions on strings is also a great tool.

print(name.lower(), name.upper(), name.title())

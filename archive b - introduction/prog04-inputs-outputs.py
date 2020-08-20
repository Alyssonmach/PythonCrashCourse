# receiving input data from user

# specification of data format is good practice, 
# as standard input is a string;
name = str(input('What\'s your name? '))
age = int(input('What\'s your age? '))

# output of data to the user

print('Hello {}, you are {} years old!'.format(name, age))

# quotes in strings are no problem for python!

print('\nSingle quotes')
print("Double quotes")
print('''Triple quotes''')

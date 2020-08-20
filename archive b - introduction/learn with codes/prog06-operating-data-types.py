# Boolean types are represented in two states: true or false.

activated = True
disabled = False

print(activated)
print(disabled, '\n')

# there is also a state of negation and logical disjunction.

print(not activated)
print(not disabled, '\n')

print(activated and disabled)
print(activated and activated)
print(disabled and disabled, '\n')

print(activated or disabled)
print(activated or activated)
print(disabled or disabled, '\n')

# mathematical operators can be used

print(7 > 5)
print(7 < 5, '\n')

print(activated == activated)
print(activated != disabled, '\n')

print(7 <= 7)
print(8 >= 9)




first_name = 'ada'
last_name = "lovelace"

# programmer format "i like complicated things, love me"
idiot_format = first_name.capitalize().__add__(" " + last_name.capitalize())

# cool programmer format
cool_format = first_name + " " + last_name

print(idiot_format)
print(cool_format.title())
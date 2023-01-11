#tipo primitivo e informações sobre valor

word_input = input('Digite algo: ')
print('O tipo primitivo é ', type(word_input))
print('Só tem espaços? ', word_input.isspace())
print('É um numero? ', word_input.isnumeric())
print('É alfabético? ', word_input.isalpha())
print('É alfanumérico? ', word_input.isalnum())
print('Está em maiúsculas? ', word_input.isupper())
print('Está em minúsculas? ', word_input.islower())
print('Está capitalizada? ', word_input.istitle())

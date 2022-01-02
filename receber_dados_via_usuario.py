from datetime import date

nome = input('Qual é o seu nome?')
print(f' Seja bem vindo!! {nome}')

idade = input('Quantos ano você tem?')
print(f'{nome} tem {idade} anos')

time = date.today().year
print(f'{nome} nasceu em {time - int(idade)}')




"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite o seu nome:')
print(nome)
idade = input('Digite a sua idade:')
print(idade)
if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
if ' ' in nome:
     print("Desculpa, você deixou campos vazios.")
else:
    print("Seu nome NÃO contém espaços")

print(f'Seu nome tem {len(nome)} letras')
print(f'A primeira letra do seu nome é {nome[0]} ')
print(f' A última letra do seu nome é {nome[-1]}')
    

variavel_nome = ('Caio')
print(len(variavel_nome)[3])

# Introdução ao try/except
# try -> tentar executar algo
# except -> ocorreu algukm erro ao tentar executar

numero_str = input('Vou dobrar o numero que vc digitar: ')
try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#   print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#    print('Isso não é um número')


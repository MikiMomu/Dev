# input = função
nome = input ('Qual o seu nome? ')
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')
int_numero_1 = int(numero_1)
int_numero_2 = int (numero_2)

print(f'O seu nome é {nome}')
print(f'A soma dos números é: {numero_1 + numero_2}')

# if / elif.../ else
# se / se não se / se não

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == "entrar": 
    print('Você entrou no sistema') 
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Essa opção não existe.')
    
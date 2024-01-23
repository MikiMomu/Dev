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
    
condicao1 = True
condicao2 = True
condicao3 = True
condicao4 = True

if condicao1:
    print('Codigo para condição 1')
elif conficao2:
    print('Codigo para condição 2')
elif conficao3:
    print('Codigo para condição 3')
elif conficao4:
    print('Codigo para condição 4')
else:
    print('')

if 10 == 10:
    print('Outro if')
    
print('Fora do if')    

# BreakPoint servem para parar o código em uma determinada linha
# StepOver serve para que o interpretador executa uma determinada linha de código
# Debugger serve para entender como o interpretador está operando

# Operadores de comparação (relacionais)
# OP->Significado -> Exemplo (True)
# > maior ex: 2 > 1
# >= maior ou igual ex: 2 >= 2
# < menor ex: 1 < 2
# <= menor ou igual 2 <= 2
# == igual ex: a = a
# != diferente ex: a != b
maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'a'
diferente = 'a' != 'b'
print(diferente)

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )

# Operadore lógicos 
# and (e) or (ou) not (não)
# and - Todas condições precisam ser 
# verdadeiras.
# Se qualquer valor for considerado falso,
# a aexpressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

entrada + input('[E]ntrar [S]air: ')
senha_digitada = input ('Senha: ')

senha_permitida = '12345'
# if True
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

# Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print(senha)
print(True and False and True)
print(bool(''))

# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True
print(not True) # False
print(not False) # True

senha = input('Senha: ')

if senha == '12345':
   print('Entrou')
if not senha:
    print('Nada foi digitado')
else:
    print('Senha incorreta')

# Operadore in e not in
# Strings são iteráveis(Torna possível navegar item por item)
# 0 1 2 3 4 5 (Indices positivos)
# C A I O
# -6-5-4-3-2-1 (Indices Negativos)
# in ->  Estar Entre
# not in -> Não Estar Entre
nome = 'Caio'
print(nome[2])
print(nome[-4])
print('a' in nome)
print(10 * '-')
print('z' in nome)
print('io' in nome)
print('ko' in nome)

nome = input ('Digite seu nome:')
encontrar = input ('Digite o que deseja encontrar:')

if encontrar in nome :
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não esta em {nome}')
    
# Interploação básico de strings
# s - string
# d e i - int
# f - float
# x e X - Hexadecimal(ABCDEF0123456789)

nome = ' Caio'
preco = 1000.95897643
variavel= '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04x' % (15, 15))

# Formatação básica de strigs
# s - string
# d - int
# f - float
# .<número de digitos>f
# x ou X - Hexadecimal
# (Caractere)(><^)(quantidade)
# > - Esquerda
# < - Direita
# ^ - Centro
# Sinal - + ou -
# Ex: 0>-100,.1f
# Conversion flags - !r !s ! a

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')

# Fatiamento de strings
# 012345678
# Olá mundo
# -987654321
# Fatiamento [i:f:p] [::]
# Obs : a função len retorna a qtd
# de caracteres da str

variavel = 'Olá mundo'
print(len(variavel)[3])

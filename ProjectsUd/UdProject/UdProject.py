print('Hello')# Exibição Hello
print('Batata') # Exibição da Batata

print(1+1)
""""""   
# (DocString)São Comentarios que sao lidos pelo codigo
# DocString não tem limite de linhas diferente do # que possui limite de uma linha
""""""

print(123,321,sep='-',end= '\r\n')
print(321,321,sep="",end= '\n')
# /r/n -> CRLF
# /n->LF
# O python diferencia letras Maiusculas de minusculas
   
    # Python = Linguagem de Programação
    # Tipo de tipagem = Dinamica/ Forte
    # str->string->Texto
"""
    Strings sao textos que estão dentro das aspas
"""
# Aspas simples
print('Caio Gall')
print(1,"Caio 'Gall' ")

# Aspas duplas
print("Caio Gall")

# Escape
print("Caio \"Gall\"")

# r
print(r"Caio\"Gall\"")

# Tipos int e float 
# int -> Número inteiro
# O tipo int representa qualquer número
# positivo ou negativo. int sem sinal é considerado
# positivo
print(11) # Int
print(-11) # Int
print(0) # Int

# float -> Número com ponto flutuante
# O tipo float representa qualquer número
# positivo ou negativo com ponto flutuante
# float sem sinal é considerado positivo
print(1.1) # float
print(0.0, -1.5) # float

# A função type mostra o tipo que o Python
# Inferiu ao valor
print(type('Gall'))
print(type(0),type(1.1),type(0.0))

# Tipo de dado bool (boolean)
# Ao questionar algo em um programa,
# só existem duas respostas possíveis:
# sim (True) ou não (false)
# Existem vários operadores para "questionar".
# Dentre eles o ==, que é um operador lógico que 
# questiona se um valor é igual a outro
print(10 == 10) # Sim => True (Verdadeiro)
print(10 == 12) # Não => False (Falso)
print(type(True))
print(type(False))
print(type(10 == 10))
print(type(10 == 12))

# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool
print(int('1'), type(int('1')))
print(type(float('1') + 1))
print(bool(''))
print(str(11) + 'b')

# Variáveis são usadas para salvar algo na memória do computador.
# PEP8: inicie variáveis com letras minúsculas, pode usar
# números e underline _.
# O sinal de = é o operador de atribuição. Ele é usado para
# atribuir um valor e um nome (variável).
# Uso: nome_variável = expressão
nome_completo = 'Caio Gall'
soma_dois_mais_dois = 2 + 2
int_um = bool('1')
print(int_um, type (int_um))
print(nome_completo, soma_dois_mais_dois) 

nome = "Caio"
sobrenome = 'Gall'
idade = 18
ano_de_nascimento = 2005
maior_de_idade = idade >= 18
altura = 1.75
print('Nome:', nome, 'Idade', idade)
print('É maior de idade?', maior_de_idade) 

print(nome)
print(sobrenome)
print(idade)
print(ano_de_nascimento)
print('É maior de idade?', maior_de_idade)
print(altura)

adicao = 10 + 10
print('Adição', adicao)

subtracao = 10 - 5
print('Subtração', subtracao)

multiplicacao = 10 * 20
print('Multiplicação', multiplicacao)

divisao = 10 / 2 # O retorno é sempre float
print('Divisão', divisao)

divisao_inteira = 20 // 2 # O resultado sempre corta as casas decimais
print('Divisão Inteira', divisao_inteira)

exponenciacao = 2 ** 4
print('Exponenciação', exponenciacao)

modulo = 55 % 2 # resto da divisão 
print("Módulo", modulo)

print(10 % 8 == 0)
print(16 % 8 == 0)
print(15 % 2 == 0)
print(12 % 2 == 0)
print(24 % 8 == 0)

concatenacao = 'A' + 'B' + 'C'
print(concatenacao)

a_dez_vezes = 'A' * 10
tres_vezes_caio = 3 * 'Caio'
print(a_dez_vezes)
print(tres_vezes_caio)

# 1 (n + n)
# 2. **
# 3. * / // %
# 4. + -
conta_1 = (1 + 1) ** (5 + 5)
print(conta_1)

nome = 'Llag Oiac'
altura = 1.75
peso = 75
imc = peso / (altura * altura)

# ... -> Elipses ele geralmente e utilizado como place rolder

print(nome, 'tem', altura, 'de altura',)
print( 'tem', peso, 'kg', 'e seu IMC é')
print(imc)

# Llag Oiac tem 1.75 de altura,
# pesa 75 Kg e seu IMC é
# IMC = peso / (altura x altura)

"f-strings"

# Como formatar uma string

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'tem {peso} Kg, e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Formatação de strings com o método format

a = 'A'
b = 'B'
c = 1.1
string = 'a = {0} b = {1} c = {2:.2f}'
formato = string.format(
    a,b,c)

print(formato)



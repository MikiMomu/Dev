import random

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
special_characters = '!@#$%^&*()_+-=[]{}|;:,./<>?'

for_pass = lower_case + upper_case + numbers + special_characters

tamanho_da_senha = 12

password = "".join(random.sample(for_pass, tamanho_da_senha))
print ("My password is:",(password))
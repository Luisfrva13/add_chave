import os

pessoa = {
    'Nome': input('Informe seu nome:'),
    'Idade': input('Informe sua idade:'),
    'Profissão': input('Informe sua profissão:')
    }

nova_chave = input('Informe o novo novo campo:')
novo_dado = input('Informe o novo dado:')
pessoa[nova_chave] = novo_dado

os.system('cls')

for chave in pessoa:
    print(f'{chave}:{pessoa.get(chave)}')

print('')

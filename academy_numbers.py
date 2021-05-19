from time import sleep

dados = [] # ---> inserir todos os dados aqui.
dessa_forma_tem_que_ser = [{'nome': 'Isabela Araujo', 'idade': 20, 'estado': 'SC'}, {'nome': 'Roberto', 'idade': 31, 'estado': 'PR'}]
android = [['Isabela Araujo',20,'SC'],['Emilly Sousa',19,'SP'],['Miguel Fernandes',27,'SC']]
android_1 = {'nome':'Roberto','idade':31,'estado':'PR'}
android_2 = {'nome':'Isabela Araujo','idade':20,'estado':'SC'}
copia_lista_android_2 = []
copia_lista_android_2.append(android_2)
copia_lista_android_2.append(android_1)
ios = ''
qa = ''
soma_idade = 0
contador = 0

# print(f'{len(copia_lista_android_2)}')
# print(f'{copia_lista_android_2[contador]["idade"]}')
# print(f'{copia_lista_android_2}')

while contador < len(copia_lista_android_2):
    conversor_idade = copia_lista_android_2[contador]['idade']
    soma_idade += conversor_idade
    contador += 1
    # if contador == len(copia_lista_android_2):
    #     break

print(f'Total de idade é {soma_idade} ')

# print(f'{len(copia_lista_android_2)}')
print(f'{copia_lista_android_2}')
# for c, i in enumerate(copia_lista_android_2):
#     soma_idade += copia_lista_android_2[-1]['idade']

# print(f'{copia_lista_android_2[0]["idade"]}')
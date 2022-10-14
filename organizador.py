# .-*- coding: utf-8 -*-.
import os
import shutil

# Avaliando se o diretório é o de trabalho. Caso não exista, 
# ele será criado
pasta_inicial = os.getcwd()
pasta_correta = 'C:\\Users\\rmart\\Documents\\Python_Scripts\\'

if os.path.isdir(pasta_correta):
    print('a pasta raiz já existe, continuando...')
else:
    print('a pasta raiz ainda não existe. criando... ')
    os.mkdir(pasta_correta)    
    print('Pasta raiz criada')

# avaliando se já está na pasta correta. Caso não esteja,
# ele muda.
if pasta_inicial != pasta_correta:
    print('pasta errada. corrigindo...')
    os.chdir(pasta_correta)
    print('mudei o diretorio para ' + pasta_correta)
else:
    print('a pasta estava correta. prosseguindo ...')

# usuario cria palavra chave
arquivos = os.listdir()
palavrachave = input("Digite a palavra-chave: ")

# se não existir pasta com aquela palavra-chave, ele cria
if os.path.isdir(pasta_correta + palavrachave):
    print('pasta verificada, prosseguindo...')
else:
    print('a pasta ainda não existe. criando... ')
    os.mkdir(palavrachave)    
    print('Pasta criada...')

# varre o diretório procurando caracteres bizarros nos 
# nomes e os move
for i in arquivos:
    i = i.replace("!", "",-1)
    i = i.replace("@", "",-1)
    i = i.replace("#", "",-1)
    i = i.replace("[", "",-1)
    i = i.replace("]", "",-1)

## varre o diretório procurando arquivos com a palavra-chave
## e os move para a pasta de mesmo nome
#     if palavrachave in i:   
#         shutil.move(i, pasta_correta + palavrachave)
#         print('arquivado')
#     else:
#         print('mantido na pasta de origem')
# 

os.walk
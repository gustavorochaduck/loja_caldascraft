import time
import os
import bcrypt
from pynput.keyboard import Key, Controller
import json


#installation
def installation():
    keyboard = Controller()

    keyboard.press(Key.cmd)
    keyboard.release(Key.cmd)
    time.sleep(0.5)
    keyboard.type('cmd')
    time.sleep(0.5)
    keyboard.press(Key.enter)
    time.sleep(0.5)
    keyboard.release(Key.enter)
    time.sleep(0.5)
    #keyboard.type('pip install bcrypt')
    keyboard.type('ping 8.8.8.8')
    keyboard.press(Key.enter)
    time.sleep(0.5)
    keyboard.release(Key.enter)


def hashed(text):
    # Converte a string para bytes
    text_bytes = text.encode('utf-8')
    hashing = bcrypt.hashpw(text_bytes, bcrypt.gensalt())
    return hashing

def view_list():
    return print('test')

def salvar_hash(hash_gerado):
    # Define o nome do arquivo JSON
    arquivo_json = 'desafios.json'

    # Carrega o conteúdo do arquivo, ou cria uma estrutura vazia se o arquivo não existir
    if os.path.exists(arquivo_json):
        with open(arquivo_json, 'r') as file:
            dados = json.load(file)
    else:
        dados = {"Desafios": []}

    # Cria o novo desafio e adiciona ao JSON
    novo_desafio = {
        "nr_Desafio": len(dados["Desafios"]) + 1,
        "Resposta": str(hash_gerado)  # Converte o hash para string
    }
    dados["Desafios"].append(novo_desafio)

    # Salva a estrutura atualizada no arquivo JSON
    with open(arquivo_json, 'w') as file:
        json.dump(dados, file, indent=4)

    print(f"Desafio {novo_desafio['nr_Desafio']} salvo com sucesso!")
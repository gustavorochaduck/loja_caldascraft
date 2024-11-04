#Tenho que Estudar sobre estas 3 bibliotecas

import bcrypt
import os
import json

def decrypt():

    json_location = 'cryptografy\desafios.json'

    if not os.path.exists(json_location):
        print('Arquivo nao encontrado')
        return[]

    with open(json_location, 'r') as file:
        dados = json.load(file)

    return dados['Desafios']  # Retorna a lista de desafios

    # Exemplo de uso
    if __name__ == "__main__":
        desafios = carregar_desafios()  # Carrega os desafios

        for desafio in desafios:  # Itera sobre cada desafio
            nr_desafio = desafio['nr_Desafio']
            resposta = desafio['Resposta']
            print(f"Número do Desafio: {nr_desafio}, Resposta (hash): {resposta}")


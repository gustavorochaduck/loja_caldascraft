import time
import functions as fc

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

print('''if you are using the program for the first time, I recommend that you select [Library installation]. 
If you have the bcrypt library in version 4.2.0, you can start the program [RUN].''')

print('-=-'*20)
print('1 - [RUN]')
print('2 - [installation]')
print('-=-'*20)
selection = int(input('Select: '))
print('-=-'*20)

if selection == 1:
    print('1 - [view hashed list]')
    print('2 - [hashing a text]')
    print('-=-'*20)
    selection1 = int(input('Select: '))

    if selection1 == 1:
        fc.view_list

    elif selection1 == 2:
        text = input('Type the Text: ')
        hash_var = fc.hashed(text)
        print(fc.hashed(text))
        print('-=-'*20)
        print('You want to Save?')
        add_confirm = str(input('Type [Y] to yes and [N] to no: ').lower())
        
        if add_confirm == 'y':
            fc.salvar_hash(hash_var)
        
        if add_confirm == 'n':
            input('Type [ENTER] to close the program: ')

elif selection == 2:
    fc.installation()
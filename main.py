meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            "TROLAR": "Fazer algo errado de propósito ou sem querer",
            "SAFE": "Ficar de boa, tranquilo",
            "TILTAR": "Se estressar com algo",
            "CHAPEI": "Fui burro",
            "BOT": "Normalmente usado pra chamar alguém de ruim...",
            }

word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")

if word in meme_dict.keys():
    # O que devemos fazer se a palavra for encontrada?
    print(meme_dict[word])
else:
    # O que devemos fazer se a palavra não for encontrada?
    print("Nao sei, devo atualizar meu repertório")

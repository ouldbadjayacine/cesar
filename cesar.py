def dechiffrer(text):
    original_tab = [['e', '0.159'], ['a', '0.094'], ['i', '0.084'], ['s', '0.079'], ['t', '0.073'], ['n', '0.072'],
                    ['r', '0.065'], ['u', '0.062'], ['l', '0.053'], ['o', '0.051'], ['d', '0.034'], ['m', '0.032'],
                    ['p', '0.029'], ['q', '0.029'], ['c', '0.026'], ['v', '0.021'], ['b', '0.01'], ['f', '0.01'],
                    ['j', '0.009'], ['j', '0.009'], ['h', '0.008'], ['x', '0.003'], ['z', '0.003'], ['y', '0.002'],
                    ['k', '0.00'], ['w', '0.00']]
    tab = []

    texte = text.lower()

    alphabet = "abcdefjhijklmnopqrstuvwxyz"

    espace = 0

    # Initialisation

    for i in alphabet:
        position = ord(i) - 97
        lettre = []
        lettre.append(i)
        lettre.append("0")
        tab.append(lettre)

    for caractere in text:

        if caractere == " ":
            espace += 1
            continue

        if caractere == "’":
            espace += 1
            continue

        position = ord(caractere) - 97

        a = int(tab[position][1])
        a += 1
        tab[position][1] = a

    len_net = len(text) - espace

    for i in tab:
        i[1] = format(int(i[1]) / len_net, '.3f')

    tab.sort(key=lambda x: x[1], reverse=True)

    i = 0
    k = 0
    taille = 15
    while i < taille:
        k += ord(tab[i][0]) - ord(original_tab[i][0])
        i += 1

    k = int(k / taille)

    # Déchiffrement de message

    for cle in range(k - 1, k + 2):

        message = ""

        for caractere in text:

            if caractere == " ":
                message += " "
                continue

            a = ord(caractere) - cle

            if a < 79:

                message += chr(a + 26)

            else:
                message += chr(a)
        print("\n")
        print("clé = ", cle)
        print("Message déchiffrer :")
        print(message)
        print()


msg_chiffre = input("saisi le message chiffré :")

dechiffrer(msg_chiffre)

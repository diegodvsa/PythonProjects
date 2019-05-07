import random

def imprimir_mensagem_abertura():
    print('-------------------------')
    print('----- Jogo da Forca -----')
    print('-------------------------')

def imprimir_mensagem_vencedor():
    print('Parabéns, você ganhou!')
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprimir_mensagem_perdedor(palavra_secreta):
    print('Você foi enforcado!')
    print('A palavra era {}'.format(palavra_secreta))
    print("    _______________         ")
    print("   /               \        ")
    print("  /                 \       ")
    print(" /                   \      ")
    print(" |   XXXX     XXXX   |      ")
    print(" |   XXXX     XXXX   |      ")
    print(" |         x         |      ")
    print(" |                   |      ")
    print(" |     _________     |      ")
    print(" \    /         \\    /      ")
    print("  \_________________/      ")

    

def definir_palavra_secreta():
    palavras = []
    with open("palavras.txt","r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
    
    aleatorio = random.randrange(0,len(palavras))
    palavra_secreta = palavras[aleatorio].upper()
    return palavra_secreta

def pedir_chute():
    chute = input('Digite uma letra ')
    chute = chute.strip().upper()
    return chute

def marcar_chute_correto(chute, letras_acertadas,palavra_secreta):
    posicao = 0 
    for letra in palavra_secreta:
        if(chute.upper() == letra.upper()):            
            letras_acertadas[posicao] = letra
        posicao = posicao + 1
    
def jogar():

    imprimir_mensagem_abertura()

    palavra_secreta = definir_palavra_secreta()

    letras_acertadas = ['_' for letra in palavra_secreta]

    acertou = False
    enforcou = False

    print(letras_acertadas)

    tentativas = 5

    while(not acertou and not enforcou):
        chute = pedir_chute()

        if(chute in palavra_secreta):
           marcar_chute_correto(chute,letras_acertadas,palavra_secreta) 
        else:
            tentativas -= 1

        acertou = '_' not in letras_acertadas

        enforcou = tentativas == 0

        print(letras_acertadas)

    if(acertou):
        imprimir_mensagem_vencedor()
    else:
        imprimir_mensagem_perdedor(palavra_secreta)

    print('\nFim do jogo!')
        
jogar()

input("Pressione qualquer tecla para sair...")
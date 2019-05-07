import random #importa classe random para gerar numeros aleatorios

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

    
#função para definir aleatoriamente uma palavra secreta no arquivo palavras
def definir_palavra_secreta():
    palavras = [] #inicia lista palavras
    with open("palavras.txt","r") as arquivo: #with para abrir arquivo e fechar automaticamente no modo leitura (definido com "r")
        for linha in arquivo: #para cada linha no arquivo
            linha = linha.strip() #trata linha tirando espaço e caracteres especiais 
            palavras.append(linha) #adiciona linha na lista
    
    aleatorio = random.randrange(0,len(palavras)) #gera numero aleatorio no intervalo da quantidade de palavras

    palavra_secreta = palavras[aleatorio].upper() #inicializa palavra secreta recebendo palavra aleatoria da lista

    return palavra_secreta #retorna a palavra sorteada

#função para pedir o chute ao jogador
def pedir_chute():
    chute = input('Digite uma letra ')
    chute = chute.strip().upper()
    return chute

#função para percorrer palavra e substituir com o chute
def marcar_chute_correto(chute, letras_acertadas,palavra_secreta):
    posicao = 0 
    for letra in palavra_secreta:
        if(chute.upper() == letra.upper()):            
            letras_acertadas[posicao] = letra
        posicao = posicao + 1

#função que inicia o jogo
def jogar():

    imprimir_mensagem_abertura()

    palavra_secreta = definir_palavra_secreta()

    letras_acertadas = ['_' for letra in palavra_secreta] #cria lista com '_' substituindo cada letra da palavra secreta

    acertou = False
    enforcou = False

    print(letras_acertadas) #imprime as lacunas da palavra escondida

    tentativas = 5 #define numero de tentativas

    #loop para verificar vitória por letra jogada
    while(not acertou and not enforcou):
        chute = pedir_chute()

        if(chute in palavra_secreta): #verifica se a letra chutada está contida na palavra secreta
           marcar_chute_correto(chute,letras_acertadas,palavra_secreta)  #marca chute correto
        else:
            tentativas -= 1 #menos 1 tentativa

        acertou = '_' not in letras_acertadas #verifica se palavra está completa

        enforcou = tentativas == 0 #verifica se acabaram as tentativas (fim de jogo)

        print(letras_acertadas) #imprime as letras acertadas e as lacunas da palavra

    if(acertou):
        imprimir_mensagem_vencedor()
    else:
        imprimir_mensagem_perdedor(palavra_secreta)

    print('\nFim do jogo!')
        
jogar()

input("Pressione qualquer tecla para sair...")
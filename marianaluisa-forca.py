import random #Importa a biblioteca random para gerar números aleatórios                                                                                                                                        

#palavras = ['abacate','chocolate','paralelepipedo','goiaba']  #Gerado uma variável que contém uma lista de palavras
palavras = []
letrasErradas = '' 
letrasCertas = ''
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def palavrasescolhidas(): #Define funcões
    global palavras #Define que a função pertence a todo o programa
    while True:  #Estrutura de repetição
        palavrasescolhidas = input('Digite a palavra que deseja para o jogo: ') #Pergunta a pessoa as palavras de deseja para o jogo
        if palavrasescolhidas == "":  #Se der enter sem escrever a palavra
            break                   #Parar
        palavras.append(palavrasescolhidas) #Indica que as palavras que a pessoa escolher é para ser adicionada à lista palavras 

        
def principal(): #O def define funções
    """
    Função Princial do programa
    """
    print('F O R C A') #Imprime a palavra FORCA na tela
    palavrasescolhidas()  #Chama a função
    palavraSecreta = sortearPalavra() #Variável que chama uma função
    palpite = ''  #Pede palpite sobre uma letra da palavra sorteada 
    desenhaJogo(palavraSecreta,palpite)

    while True: #Estrutura de repetição enquanto a condição dada for verdadeira
        palpite = receberPalpite() 
        desenhaJogo(palavraSecreta,palpite)
        if perdeuJogo(): #Comando de fluxo que executa quando a função é verdadeira
            print('Voce Perdeu!!!')
            break   #Quebra ou interrompe o fluxo natural do programa
        if ganhouJogo(palavraSecreta):
            print('Voce Ganhou!!!')
            break            
        
def perdeuJogo():
    global FORCAIMG #Define que esta não é uma variável local,mas que pertence a todo programa
    if len(letrasErradas) == len(FORCAIMG): #A função len retorna um valor tipo inteiro
        return True  #Forma de retornar dados quando a condição é verdadeira
    else:
        return False  #Forma de retornar dados quando a condição é falsa
    
def ganhouJogo(palavraSecreta):
    global letrasCertas
    ganhou = True #Função que indica se é vardadeiro o que a variável diz
    for letra in palavraSecreta: #For gera um loop dentro de uma lista e o in indica a lista em que vai percorrer 
        if letra not in letrasCertas: #Letra não está dentro da lista lestrasCertas
            ganhou = False #Função que indica se é falso o que a variável diz
    return ganhou #Forma de retornar dados    
        


def receberPalpite():
    
    palpite = input("Adivinhe uma letra: ")
    palpite = palpite.upper()
    if len(palpite) != 1:
        print('Coloque um unica letra.')
    elif palpite in letrasCertas or palpite in letrasErradas: #Elif é uma sentença que possa ser avaliada como verdadeira ou falsa e or é como "ou"
        print('Voce ja disse esta letra.')
    elif not "A" <= palpite <= "Z": #Elif é uma sentença que possa ser avaliada como falsa
        print('Por favor escolha apenas letras')
    else: #É executado quando a condição if acima for falsa
        return palpite
    
    
def desenhaJogo(palavraSecreta,palpite): #Função para desenhar o jogo
    global letrasCertas
    global letrasErradas
    global FORCAIMG

    print(FORCAIMG[len(letrasErradas)]) #Imprime um elemento da lista FORCAIMG que é correspondente ao número de letras erradas
    
     
    vazio = len(palavraSecreta)*'-' #Para cada letra adiciona um tracinho
    
    if palpite in palavraSecreta:
        letrasCertas += palpite
    else:
        letrasErradas += palpite

    for letra in letrasCertas:
        for x in range(len(palavraSecreta)):
            if letra == palavraSecreta[x]:
                vazio = vazio[:x] + letra + vazio[x+1:]
                
    print('Acertos: ',letrasCertas ) #Imprime na tela as letras que forem certas
    print('Erros: ',letrasErradas)  #Imprime na tela as letras que forem erradas
    print(vazio)
     

def sortearPalavra():
    global palavras
    return random.choice(palavras).upper() #Retorna na biblioteca random e escolhe um comando e o deixa todo em maiúsculo

    
principal() #Chama o programa principal

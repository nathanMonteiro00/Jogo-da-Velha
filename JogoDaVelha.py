######################################################
# Programação Funcional / Programção I (2021/2)
# EP2 - Jogo da Velha
# Nome: Nathan Rodrigues Monteiro
# Matrícula: 2021200097
######################################################

import random
from os import system, name

def getMatricula():
    """
    Retorna a matricula do aluno como string
    """
    return "2021200097"

def getNome():
    """
    Retorna o nome completo do aluno
    """
    return "Nathan Rodrigues Monteiro"

def limpaTela(): 
	if name == 'nt': 
		system('cls') 
	else: 
		system('clear') 

def OutroJoga(T):
    """
    Função onde o jogador decide em que local vai posicionar sua letra.
    Essa função também é responsável por mostrar o tabuleiro atualizado a cada jogada feita.
    """
    CIN = "\033[1;37m"
    RED = "\033[1;31m"
    RST = '\033[00m'
    Tabuleiro(T) 
    try:       
        marcação = int(input(f"{CIN}\nQual posição você deseja marcar (1-9)?: {RST}" ))
    except:# se escolher outra letra
        print(f"{RED}Atenção!! Você só pode escolher um valor entre 1 e 9{RST}")
        return OutroJoga(T)

    if marcação <= 0 or marcação > 9:
        print(f"{RED}Atenção!! Você só pode escolher um valor entre 1 e 9{RST}")
        return OutroJoga(T)    
    
    elif T[marcação] != " ":
        print(f"{RED}Atenção!! Você deve escolher um campo vazio{RST}")
        return OutroJoga(T)

    else:
        return marcação
        
def Jogo2(tab,simb,simb2):# quando o computador joga
    """
    Função que recebe a jogada que o computador vai realizar,atualiza o tabuleiro,recebe a quantidade de
    campos vazios e o valor que vai determinar se ele ganhou ou deu empate.Caso ele 
    não tenha ganho ou sua jogada não resulte em empate,a partida continua normalmente com a vez do jogador.
    """
    RST = '\033[00m'
    RED = "\033[1;31m"
    CIN = "\033[1;37m"
    jogada = jogadaComputador(tab,simb)
    tabAtt = tab[:]
    tabAtt[jogada] = simb
    quantidade = fazConta(tabAtt) # quantidade de campos vazios
    ganhou = QuemGanha(tabAtt,simb,quantidade)
    
    if ganhou == 1:
        Tabuleiro(tabAtt)
        print(f"{RED}Você perdeu! O computador ficou com a vitória!{RST}")
        exit()
    elif ganhou == 2:
        Tabuleiro(tabAtt)
        print(f"{CIN}Xiii... Deu velha, o jogo terminou empatado!!{RST}")
        exit()
    else:
        Jogo(tabAtt,simb2,simb)


def Jogo(tab,simb,simb2):# quando o jogador joga
    """
    Essa função recebe o local em que o jogador deseja que sua letra seja posicionada,
    atualiza o tabuleiro e verifica se ele ganhou. Caso ele 
    não tenha ganho ou sua jogada não resulte em empate,a partida continua normalmente com a vez do computador.
    """
    RST = '\033[00m'
    GREEN = "\033[1;32m"
    CIN  = "\033[1;37m"
    jogada = OutroJoga(tab) 
    tabAtt = tab[:]
    tabAtt[jogada] = simb
    quantidade = fazConta(tabAtt)
    
    ganhou = QuemGanha(tabAtt,simb,quantidade)

    if ganhou == 1:
        Tabuleiro(tabAtt)
        print(f"{GREEN}Parabéns! Você ganhou!{RST}")
        exit()

    elif ganhou == 2:
        Tabuleiro(tabAtt)
        print(f"{CIN}Xiii... Deu velha, o jogo terminou empatado!!{RST}")
        exit()

    else:
        Jogo2(tabAtt,simb2,simb)
    
def qualSimbolo(simb):
    """
    Função que identifica qual o símbolo do jogador humano e retorna seu valor.
    """

    if simb == "X":
        simbJ = "O"
        return simbJ 

    elif simb == "O":
        simbJ = "X"
        return simbJ 
    
def jogadaComputador(t, simb):
    """
    Recebe o tabuleiro e o simbolo (X ou O) do computador e determina onde o computador deve jogar
    O tabuleiro pode estar vazio (caso o computador seja o primeiro a jogar) ou com algumas posições preenchidas, 
    sendo a posição 0 do tabuleiro descartada.

    Parâmetros:
    tabuleiro: lista de tamanho 10 representando o tabuleiro
    simboloComputador: letra do computador

    Retorno:
    Posição (entre 1 e 9) da jogada do computador

    Estratégia:
    Primeiro o computador verifica se ele tem alguma chance de ganhar.Caso não tenha, verifica se possui
    chance de derrota e, se possuir, ele marca no campo devido para que não perca.

    Caso não tenha chance de perder nem de ganhar e, dependendo da jogada do outro jogador,
    o computador sempre vai optar por jogar pelos cantos.Se todos os cantos estiverem preenchidos,
    a prioridade é marcar o meio e por último os centros de alguma linha ou coluna.
    """
    tab = t[:]

    # computador verifica se pode ganhar
    if (tab[2] == simb and tab[3] == simb) or (tab[4] == simb and tab[7] == simb) or (tab[5] == simb and tab[9] == simb):
        if tab[1] == " ":
            return 1 
        
    if (tab[1] == simb and tab[3] == simb) or (tab[5] == simb and tab[8] == simb):
        if tab[2] == " ":
            return 2
    
    if (tab[1] == simb and tab[2] == simb) or (tab[6] == simb and tab[9] == simb) or (tab[5] == simb and tab[7] == simb):
        if tab[3] == " ":
            return 3
        
    if (tab[1] == simb and tab[7] == simb) or (tab[5] == simb and tab[6] == simb): 
        if tab[4] == " ":
            return 4
    
    if (tab[4] == simb and tab[6] == simb) or (tab[2] == simb and tab[8] == simb) or (tab[3] == simb and tab[7] == simb) or (tab[1] == simb and tab[9] == simb):
       if tab[5] == " ":
           return 5
    
    if (tab[4] == simb and tab[5] == simb) or (tab[3] == simb and tab[9] == simb):
        if tab[6] == " ":
            return 6

    if (tab[1] == simb and tab[4] == simb) or (tab[8] == simb and tab[9] == simb) or (tab[5] == simb and tab[3] == simb):
        if tab[7] == " ":
            return 7
    
    if (tab[7] == simb and tab[9] == simb) or (tab[5] == simb and tab[2] == simb):
        if tab[8] == " ":
            return 8

    if (tab[7] == simb and tab[8] == simb) or (tab[6] == simb and tab[3] == simb) or (tab[1] == simb and tab[5] == simb):
        if tab[9] == " ":
            return 9

    # verifica se pode perder
    simb2 = qualSimbolo(simb) # recebe o símbolo do jogador humano

    if (tab[2] == simb2 and tab[3] == simb2) or (tab[4] == simb2 and tab[7] == simb2) or (tab[5] == simb2 and tab[9] == simb2):
        if tab[1] == " ":
            return 1 
        
    if (tab[1] == simb2 and tab[3] == simb2) or (tab[5] == simb2 and tab[8] == simb2):
        if tab[2] == " ":
            return 2
    
    if (tab[1] == simb2 and tab[2] == simb2) or (tab[6] == simb2 and tab[9] == simb2) or (tab[5] == simb2 and tab[7] == simb2):
        if tab[3] == " ":
            return 3
        
    if (tab[1] == simb2 and tab[7] == simb2) or (tab[5] == simb2 and tab[6] == simb2): 
        if tab[4] == " ":
            return 4
    
    if (tab[4] == simb2 and tab[6] == simb2) or (tab[2] == simb2 and tab[8] == simb2) or (tab[3] == simb2 and tab[7] == simb2) or (tab[1] == simb2 and tab[9] == simb2):
       if tab[5] == " ":
           return 5
    
    if (tab[4] == simb2 and tab[5] == simb2) or (tab[3] == simb2 and tab[9] == simb2):
        if tab[6] == " ":
            return 6

    if (tab[1] == simb2 and tab[4] == simb2) or (tab[8] == simb2 and tab[9] == simb2) or (tab[5] == simb2 and tab[3] == simb2):
        if tab[7] == " ":
            return 7
    
    if (tab[7] == simb2 and tab[9] == simb2) or (tab[5] == simb2 and tab[2] == simb2):
        if tab[8] == " ":
            return 8

    if (tab[7] == simb2 and tab[8] == simb2) or (tab[6] == simb2 and tab[3] == simb2) or (tab[1] == simb2 and tab[5] == simb2):
        if tab[9] == " ":
            return 9

    c = fazConta(tab)
    if c == 9: # computador é o primeiro a jogar

        canto = [1,3,7,9] #vai sempre começar jogando por algum canto
        escolhe = random.choice(canto) 
        return escolhe 
    
    if c == 8: # adversário jogou primeiro
        if tab[1] != " " or tab[3] != " " or tab[7] != " " or tab[9] != " ":
            return 5
        
    if c == 6:
        if (tab[1] == simb2 and tab[9] == simb2) or (tab[3] == simb2 and tab[7] == simb2):
            return 4
        
    #se tiver alguma posição nos cantos que ainda esteja vazia
    if tab[1] == " ":
        return 1
    if tab[3] == " ":
        return 3
    if tab[7] == " ":
        return 7
    if tab[9] == " ":
        return 9

    # se o meio estiver vazio
    if tab[5] == " ":
        return 5
    
    # restou
    if tab[2] == " ":
        return 2
    if tab[4] == " ":
        return 4
    if tab[6] == " ":
        return 6
    if tab[8] == " ":
        return 8

def fazConta(tab,c = 0,i = 1):
    """
    Função responsável por contar a quantidade de campos vazios que ainda restam no tabuleiro 
    e retorná-la.
    """
    if i > 9:
        return c

    elif " " in tab[i]:
        return fazConta(tab,c + 1,i + 1)
    
    else:
       return fazConta(tab,c,i + 1)

def QuemGanha(tab,simb,quantidade):
    """
    Função que faz a análise do tabuleiro e, a partir disso, retorna um valor
    caso o jogo tenha um vitorioso,se terminou em empate(quantidade de campos vazios igual a 0 
    sem nenhuma possibilidade de vitória) ou se o jogo continua normalmente.
    """
    
    # verificação das diagonais
    if tab[1] == simb and tab[5] == simb and tab[9] == simb:
       return 1
    
    elif tab[3] == simb and tab[5] == simb and tab[7] == simb:
        return 1
    
    # verificação na vertical
    elif tab[1] == simb and tab[4] == simb and tab[7] == simb:
        return 1
    
    elif tab[2] == simb and tab[5] == simb and tab[8] == simb:
        return 1

    elif tab[3] == simb and tab[6] == simb and tab[9] == simb: 
        return 1
    # verificação na horizontal
    elif tab[1] == simb and tab[2] == simb and tab[3] == simb:
        return 1

    elif tab[4] == simb and tab[5] == simb and tab[6] == simb:
        return 1
    
    elif tab[7] == simb and tab[8] == simb and tab[9] == simb:
        return 1

    elif quantidade == 0: # quando empata
        return 2
    
    else:
        return 0

def começa():
    """
    Escolhe, aleatoriamente, entre o jogador(j) e o computador(C) 
    para decidir quem começa jogando. Após isso, a função retorna a letra escolhida.
    """
    l = ["j","C"]
    comecou = random.choice(l)

    return comecou

def começaPrograma():
    """
    Função responsável pelo armazenamento do tabuleiro inicial com todas as casas vazias e
    recepção do resultado de quem deve começar jogando. Aqui o jogador escolhe com qual símbolo vai querer jogar e,
    a partir disso, é estabelecido qual deverá ser o símbolo do computador.

    Após as verificações,é enviado os dados para outra função para que o jogo se inicie.
    """
    RST = '\033[00m'
    RED = "\033[1;31m"
    YELLOW  = "\033[1;33m"
    MAG = "\033[1;35m"
    tabuleiro = [" "," "," "," "," "," "," "," "," "," "]
    simbolo = input(f"{MAG}Você que jogar com X ou O?: {RST}")

    if simbolo == "X" or simbolo == "x":
        c = começa()
        if c == "j":
            print(f"{YELLOW}Você começa!{RST}")
            Jogo(tabuleiro,"X","O")

        else:
            print(f"{YELLOW}O computador vai começar.{RST}")
            Jogo2(tabuleiro,"O","X")
    
    elif simbolo == "O" or simbolo == "o":
        c = começa()
        if c == "j":
            print(f"{YELLOW}Você começa!{RST}")
            Jogo(tabuleiro,"O","X")

        else:
            print(f"{YELLOW}O computador vai começar.{RST}")
            Jogo2(tabuleiro,"X","O")
    else:
        print(f"{RED}Atenção! Você só pode escolher X ou O.{RST}")
        começaPrograma()

def Tabuleiro(t):
    
    """
    Função responsável pela impressão do tabuleiro.
    """
    MAG = "\033[1;35m"
    RST = '\033[00m'
    print(f" {MAG}{t[7]} | {t[8]} | {t[9]} ")
    print(f"---+---+---")
    print(f" {t[4]} | {t[5]} | {t[6]} ")
    print(f"---+---+---")
    print(f" {t[1]} | {t[2]} | {t[3]}{RST} ")


def main():
    limpaTela()
    #Você pode, se quiser, comentar os dois prints abaixo:
    #print(getNome())
    #print(getMatricula())
    RST = '\033[00m'
    CIN = "\033[1;37m"
    print(f"{CIN}Seja bem-vindo(a) ao jogo da Velha!{RST}")
    começaPrograma()

################################
## NÃO ALTERE O CÓDIGO ABAIXO ##
################################
if __name__ == "__main__":
    main()

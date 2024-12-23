#### Importation de module
from random import *

#Message de bienvenue
print("================")
print(" TIC TAC TOE :) ")
print("================")

# Choix du nbr de joueurs
j=0
while j!=1 and j !=2:
    j=int(input("Jouez-vous seul (1) ou à deux (2) ?  "))

if j==1:
    pseudo_joueur=input("Quel est ton nom ? ")

# Set up des variables
x_moves,o_moves = [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]
possible_moves = ["a1","a2","a3","b1","b2","b3","c1","c2","c3"]
coup_joueur=(0,0)
jeu_fini=False
winner=""
ordre=randint(1,2)

# Fonction d'affichage de la grille de jeu
def show_grid(x_moves,o_moves):
    print("    a   |   b   |    c    ")
    for i in range(3):
        print(" -------+-------+--------")
        print(f"{i+1}   {'x'*x_moves[3*i]}{'o'*o_moves[3*i]}       {'x'*x_moves[3*i+1]}{'o'*o_moves[3*i+1]}         {'x'*x_moves[3*i+2]}{'o'*o_moves[3*i+2]}")

# Fonction du tour d'un joueur
def tour_joueur(joueur_moves,joueur):
    global possible_moves,jeu_fini,x_moves,o_moves,coup_joueur
    show_grid(x_moves,o_moves)
    coup_joueur=(0,0)
    
    while coup_joueur not in possible_moves:
        if j==1 and joueur=="Bot":
            coup_joueur=choice(possible_moves)
        else:    
            coup_joueur = input(f"Ou joues-tu joueur {joueur} ? ")
    
    if coup_joueur[0]=="a":
        joueur_moves[3*(int(coup_joueur[1])-1)]=1
    elif coup_joueur[0]=="b":
        joueur_moves[int(coup_joueur[1])*3-2]=1      
    elif coup_joueur[0]=="c":
        joueur_moves[3*int(coup_joueur[1])-1]=1
    
    possible_moves.remove(coup_joueur)

    if possible_moves==[]:
            show_grid(x_moves,o_moves)
            jeu_fini=True

    for i in range(20):
        print("")
    
    checkwin(joueur_moves,joueur)

# Fonction de vérification de victoire
def checkwin(player_moves,joueur):
    global jeu_fini,winner
    for i in range(3):
        if player_moves[i]==player_moves[i+1]==player_moves[i+2]==1:
            jeu_fini = True
            break
        elif player_moves[i]==player_moves[i+3]==player_moves[i+6]==1:
            jeu_fini = True
            break
    if player_moves[0]==player_moves[4]==player_moves[8]==1 or player_moves[2]==player_moves[4]==player_moves[6]==1:
        jeu_fini = True

    if jeu_fini==True:
        winner=joueur
    
# Boucle principale
while jeu_fini==False: 
    if j==2:
        tour_joueur(x_moves,"X")
        if jeu_fini==True:
            break
        tour_joueur(o_moves,"O")

    elif j==1:
        if ordre==1:
            tour_joueur(x_moves,pseudo_joueur)
            if jeu_fini==True:
                break
            tour_joueur(o_moves,"Bot")
            
        elif ordre==2:
            tour_joueur(o_moves,"Bot")
            if jeu_fini==True:
                break
            tour_joueur(x_moves,pseudo_joueur)
            
        
# Affichage du vaincueur
print("")
if winner=="":
    print("Match nul !")
else:
    print(f"Victoire de {winner} !")

# Message d'au revoir
print("")
print("======================")
print(" Merci d'avoir joué ! ")
print("======================")

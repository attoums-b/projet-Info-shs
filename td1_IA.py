"""
CONSTRUCTION DE LA MACHINE DE TURING :
LES FONTIONS
-faire une fonction qui va générer les differents etats possibles
-faire une fonction qui va parcourir le ruban et effectuer les actions
DANS LE MAIN
-créer un ruban initial avec des valeurs initiales
-créer un dictionnaire dont la clé sera les etats et les valeurs seront les actions à effectuer
-dans ma fonction je fais les différentes actions en fonction des etats

LES ACTIONS POSSIBLES
-1ere action: je change les etats(e1,e2 ou eFinal)
-2e action: soit je fais rien soit j'ajoute  1 ou 0 la ou se trouve ma tete
-3e action:  je me déplace soit à gauche ou à droite



"""

#LES FONTIONS (1)


def parcourir_ruban(ruban, table_transition, position, etat):
    # Lire le symbole à la position actuelle
    symbole_lu = ruban[position]
    
    # Chercher la transition correspondante dans la table
    if (etat, symbole_lu) in table_transition:
        nouv_etat, nouv_valeur, deplacement = table_transition[(etat, symbole_lu)]
        
        # Mettre à jour le ruban à la position actuelle
        if nouv_valeur == 1 or nouv_valeur == 0: 
            ruban[position] = nouv_valeur
        
        # Mettre à jour l'état de la machine
        etat = nouv_etat
        
        # Déplacer la tête de lecture
        if deplacement == "d":  # Si la direction est droite
            position += 1
        elif deplacement == "g":  # Si la direction est gauche
            position -= 1
        # Si la direction est "n" (ne rien faire), on ne change pas la position.
        
    return ruban, position, etat


def ajouter_valeur(ruban, table_transition):
    etat = "e1"  # On commence à l'état e1
    position = 0  # La tête commence à la deuxième position du ruban (ignorer l'espace initial)
    
    # Tant que la machine n'atteint pas l'état final, on continue à exécuter les transitions
    while etat != "eFinal":
        ruban, position, etat = parcourir_ruban(ruban, table_transition, position, etat)
    
    return ruban



   

    


def main(): 
    ruban = [" ",0,1,1,0,1,0,0," "]


    table_transition = {
        ("e1"," ") : ("e1","_","d"),
        ("e1",1) : ("e2","_","_"),
        ("e1",0) : ("e2","_","_"),
        ("e2"," ") : ("eFinal","_","_"),
        ("e2",1) : ("e2","_","d"),
        ("e2",0) : ("e1",1,"d")
        
    }

    res = ajouter_valeur(ruban,table_transition)
    print(f"nouveau ruban: {res} ")



    
 

main()             

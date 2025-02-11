"""
MACHINE DE TURING

"""
def parcourir_ruban(ruban, table_transition):
    etat = "e1"
    position =  0
   

    

    while etat != "eFinal" and position < len(ruban):
        symbole_lu = ruban[position]
        if(etat,symbole_lu) in table_transition:
            nouv_etat, nouv_valeur, deplacement = table_transition[(etat,symbole_lu)]

            #mise à jour de l'etat
            etat = nouv_etat

            #mise à jour de la valeur dans la liste
            #si la nouvelle valeur est différente de rien(ici "_")  alors on met cette valeur
            if nouv_valeur != "_":
                ruban[position] = nouv_valeur
            
            

            #deplacement de la tete de lecture 

            if deplacement == "d":
                position +=1

            elif deplacement =="g":
               position -= 1

    return ruban,nouv_etat


def main():
    #definir le ruban sous forme de liste 
    ruban = [" ",0,1,1,0,1,0,0," "]
    #définir la table de transition sous forme de dictionnaire 
    table_transition = {
        ("e1"," ") : ("e1","_","d"),
        ("e1",1) : ("e2","_","_"),
        ("e1",0) : ("e2","_","_"),
        ("e2"," ") : ("eFinal","_","_"),
        ("e2",1) : ("e2","_","d"),
        ("e2",0) : ("e1",1,"d")

    }

    #appeler la fonction qui permet de faire la transition 
    res,res2 = parcourir_ruban(ruban,table_transition)

    #afficher le nouveau ruban formé
    print("le nouveau ruban est: ",res)
    print("vous etes donc à: ",res2)


main()






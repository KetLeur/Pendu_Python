from getpass import getpass
mot = getpass(" joueur 1 veuillez saisir le mot secret: ")
TENTATIVES = 7
AFFICHAGE_DU_PENDU = ""
LETTRES_TROUVEES = ""

for l in mot:
  AFFICHAGE_DU_PENDU = AFFICHAGE_DU_PENDU + "_ "

print(">> Bienvenue dans le pendu <<")

while TENTATIVES > 0:                                       #ici on dit que temps que le nombre de tentative restante est supérieur à 0 alors le jeu continue
  print("\nMot à deviner : ", AFFICHAGE_DU_PENDU)
  proposition = input("proposez une lettre : ")[0:1].lower()

 
  if proposition in mot:                                    #on définit ici que si la proposition du joueur est une partie du mot alors on lui dis que c'est bon
      LETTRES_TROUVEES = LETTRES_TROUVEES + proposition
      print("-> Bien vu!")
  else:                                                     #sinon ici on affiche que c'est raté et que de faites on affiche le pendu
    TENTATIVES = TENTATIVES - 1
    print("-> Nope\n")
    if TENTATIVES==0:
        print(" ==========Y= ")
    if TENTATIVES<=1:
        print(" ||/       |  ")
    if TENTATIVES<=2:
        print(" ||        0  ")
    if TENTATIVES<=3:
        print(" ||       /|\ ")
    if TENTATIVES<=4:
        print(" ||       /|  ")
    if TENTATIVES<=5:                    
        print("/||           ")
    if TENTATIVES<=6:
        print("==============\n")

#la on affiche le nombre de lettres qu'il va falloir deviner en mettant des _ popur chaque lettre
  AFFICHAGE_DU_PENDU = ""
  for x in mot:
      if x in LETTRES_TROUVEES:
          AFFICHAGE_DU_PENDU += x + " "
      else:
          AFFICHAGE_DU_PENDU += "_ "

#La on définit que si il n'y a plus de _ la partie se finit
  if "_" not in AFFICHAGE_DU_PENDU:
      print(">>> Gagné! <<<")
      break
     
print("\n Fin de partie    ")
# \n sert de retour à la ligne
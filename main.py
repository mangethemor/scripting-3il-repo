#Premier TP
#a = ["a", "b", "c"]
#b = 0
#for enregistrements in a:
#    print("Ma lettre : ",enregistrements)
#    print(f"{b}. Ma lettre : {enregistrements}, elle est super")
#    b = b + 1

#for number,enregistrements in enumerate(a): #Affiche (0, x), d'abord la valeur de l'incrémentation et x la valeur qu'elle contient
#    print(f"{number}. Ma lettre : {enregistrements}, elle est super")
#    b = b + 1


#dans une fonction, return fait sortir de la fonction

#def printeuse(chaine, nombre):
#    return chaine*nombre

#print(printeuse("Hello world"+'\n', 5))

#Pour mettre des valeurs par défaut dans les arguments des focntions

#def printeuse(chaine="Bonjour", nombre=4):
#    return chaine*nombre

#print(printeuse())

#stdin (standard input), stdout (standard output), stderr (standard erreur)
#import sys
#sys.stdout.write("Hello") #pour écrire sur la sortie
#sys.stderr.write("Mon erreur \n") #Pour écrire une rreur

#a = sys.stdin.readline() #Récupérer ce qui a été passé en entrée
#print(a)

#TP 2 
# import os
# import sys

# #print(sys.argv[0])
# #print(os.listdir("C:\\Users")) #Liste tous
# directory_input = sys.argv[1]
# list_dir = os.listdir(directory_input)
# #print(list_dir)

# for number, directory in enumerate(list_dir):
#     print(f"{number}. : {directory}")
# print(f"Le contenu de mon répertoire : {list_dir}")

#TP3
import sys

print(sys.argv[1], sys.argv[2], sys.argv[3])
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

# #TP3
# import sys

# directory_input, prenom, mon_age = sys.argv[1], sys.argv[2], sys.argv[3]

# print(f"Votre répertoire : {directory_input}, votre prénom : {prenom}, votre âge : {mon_age}")

# #avec with open pas besoin de close le fichier

#TP4
# import sys

# if sys.argv[4]:
#     print("OK")
# else:
#     print("NON")

# file_name, content, content_end, looping = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

# with open(file_name, "a") as f:
#     print(type(looping))
#     for i in range(int(looping)):
#         f.write(content+'\n')
#     f.write(content_end)

#TP1(S2) le print

print("Twinkle, twinkle, little star,\n         How I wonder what you are!\n                Up above the world so high,\n                Like a diamond in the sky. \n Twinkle, twinkle, little star,\n          How I wonder what you are")
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
#print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")


#TP2(S2) fonction
# import sys

# def compteurMajMin(phrase):
#     maj = 0
#     min = 0
#     for word in phrase:
#         if word.lower() == word:
#             maj = maj + 1
#         if word.upper() == word:
#             min = min + 1
#     print(f"Il y a {maj} majuscules et {min} minuscules")

# str_chain = sys.argv[1]
# compteurMajMin(str_chain)

#Solution 
# def count_letters(string):
#   upper_count = 0
#   lower_count = 0
#   for char in string:
#     if char.isupper():
#       upper_count += 1
#     elif char.islower():
#       lower_count += 1
  
#   return upper_count, lower_count

# import sys
# def changestr(phrase):
#     maj_count = 0
#     fouthword=phrase[0:3]
#     for word in fouthword:
#         if word.isupper():
#             maj_count= maj_count+1
#     if maj_count >=2:
#         print(phrase.upper())
#         #print(maj_phrase)
#     else:
#         print(phrase)

# str_chain = sys.argv[1]
# changestr(str_chain)

#prendre un texte et le mettre dans une liste

# def words_to_list(String)
#     return String.split()
# print(words_to_list("Bonjour les gens"))

tab = ['2', '3', '4', '1', '6', '6', '13', '1', '45', '2']

prec_enr = 0
for enregistrement in tab:

    if int(enregistrement) > int(prec_enr):
        prec_enr = enregistrement

print(prec_enr)

#Solution
def maxlist(list):

    return max(list)

print(maxlist([65,88,105,55,22,36]))
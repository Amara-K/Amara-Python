#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Amara.K
#
# Created:     23/09/2018
# Copyright:   (c) Amara.Koïta 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
jour=int(input("entrer un jour "))                                                 #Variable concernant le jour désiré par l'utilisateur
mois=str(input("entrer un mois"))                                                  #Variable concernant le mois désiré par l'utilisateur
                                                                                   #le mois "août" et "décembre" doivent etre écrit de la bonne manière
mois_30j=["avril","juin","septembre","novembre"]                                   #liste concernant les mois qui contient 30 jours pour gestion d'érreur
année=int(input("entrer une année"))                                               #Variable concernant l'année désiré par l'utilisateur

while année<1582 or (année==1582 and mois!="novembre" and mois!="décembre"):       #Condition qui détermine si la date est valide

    année=int(input(" Ces méthodes de calcul sont valables pour les dates à partir du 1er novembre 1582. \n Entrer une année correspondante"))

while jour<1 or jour>31:                                                          # gestion d'erreur pour jours invalide
    jour=int(input("Entrer un jour compris entre 1 et 31 "))


while jour>30 and mois in mois_30j :                                              #gestion d'erreur pour mois à 30 jours
    jour=int(input(" Vous avez choisi un mois qui ne possède que 30 jours, \n veuillez saisir un nouveau jour "))


while jour>29 and mois=="février":                                                #gestion d'erreur pour mois de février
    jour=int(input(" Le mois de février ne comprend que 28 jours (et 29jours dans une année bissextile), \n veuillez recommencer "))


calcul=0                                                                          #Variable qui va stocker mes calculs par rapport au 2 derniers chiffres de l'année
a=0                                                                               #Variable qui va sotcker le résultat de la fonction ajout_selon_mois
b=0                                                                               #Variable qui va sotcker le résultat de la fonction bissextile
c=0                                                                               #Variable qui va sotcker le résultat de la fonction siècle



#else:
calcul=année%100                                                                 #Utilisation du modulo pour garder que les 2 derniers chiffres
calcul=calcul+int(calcul/4)                                                      #On ajout 1/4 de ce chiffre en ignorant les restes
calcul=calcul+jour                                                               # On ajoute la journée du mois


def ajout_selon_mois(mois,calcul):                                               #fonction qui concerne "Selon le mois on ajoute"
    if mois=="février" or mois=="mars" or mois=="novembre":
        calcul+=3
    if  mois=="avril" or mois=="juillet":
        calcul+=6
    if mois=="mai":
        calcul+=1
    if mois=="juin":
        calcul+=4
    if mois=="août":
        calcul+=2
    if mois=="septembre" or mois=="décembre":
        calcul+=5

    return (calcul)


a=ajout_selon_mois(mois,calcul)


def bissextile(mois,année,a):                                                     # fonction qui Si l'année est bissextile on lui retire 1
    if année%400==0 or année%4==0:
        if mois=="janvier" or mois=="février":
            a-=1
    return(a)

b=bissextile(mois,année,a)
#bissextile(mois,année,a)

def siècle(année,b):                                                              #Fonction "Selon le siècle, on ajoute"
    if int(année/100)==16 or int(année/100)==20:
        b+=6
    if int(année/100)==17 or int(année/100)==21:
        b+=4
    if int(année/100)==18:
        b+=2

    return(b)
c=siècle(année,b)

#siècle(année,b)
def déterminationjours(jour,mois,année,c):                                        #fonction qui détermine le jour de la semaine de la date énoncer par l'utilisateur
    c=c%7

    if c==0:
        print("Le",jour,mois,année,"est un Dimanche")
    elif c==1:
                 print("Le",jour,mois,année,"est un Lundi")
    elif c==2:
                print("Le",jour,mois,année,"est un Mardi")
    elif c==3:
                 print("Le",jour,mois,année,"est un Mercredi")
    elif c==4:
                print("Le",jour,mois,année," est un Jeudi")
    elif c==5:
                print("Le",jour,mois,année," est un Vendredi")
    elif c==6:
                print("Le",jour,mois,année," est un Samedi")
    return(c)

déterminationjours(jour,mois,année,c)




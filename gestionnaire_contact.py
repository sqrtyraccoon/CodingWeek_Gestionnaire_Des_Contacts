import os
from colorama import Fore, Style


#  Variables
contacts = []

#   Fonctions
def clear():
    os.system("clear")

def bienvenue():
    BIENVENUE = print(f"""{Fore.YELLOW}#----------Bienvenue dans le gestionnaire des contacts!----------#
       {Fore.RED}| search | show_all | add | remove | clear | exit |
{Fore.YELLOW}#----------------------------------------------------------------#""")

def help():
    HELP = print(f"""{Fore.YELLOW}#-------------------Commandes Disponible-------------------#
     {Fore.RED}| search | show_all | add | remove | clear | exit |
{Fore.YELLOW}#-----------------------------------------------------------#""")

def add_contact():
    try:
        add_name = input("Saisissez le nom du contact à ajouter > ")
        add_num = input("Saisissez le numéro du contact à ajouter > ")
        contact = {
        'nom': add_name,
        'num': add_num
    }
        contacts.append(contact)

        clear()
        print(f"""{Fore.GREEN}{add_name} ({add_num}) a été ajouté avec succès!
{Fore.RED}Tapez la commande {Fore.MAGENTA}'clear' {Fore.RED}pour afficher la liste des commandes disponible""")
    except:
        print("Erreur.")


def remove_contact():
    remove_contact = input("Saisissez le nom du contact à supprimer > ")
    for d in contacts:
        if d.get('nom') == remove_contact:
            contacts.remove(d)
        print(f"""{Fore.GREEN}{remove_contact} a été supprimé avec succès!
{Fore.RED}Tapez la commande {Fore.MAGENTA}'clear' {Fore.RED}pour afficher la liste des commandes disponible""")
        break


def show_all():
    print(f"""{Fore.RED}Tapez la commande {Fore.MAGENTA}'clear' {Fore.RED}pour afficher la liste des commandes disponible{Fore.WHITE}""")
    print(contacts)


def search_contact():
    pass



#  Boucle du programme
clear()
bienvenue()
while True:
    cmd = input(f'{Fore.YELLOW}meow > {Fore.LIGHTWHITE_EX}')
    if cmd == "exit":
        clear()
        break
    if cmd == "clear":
        clear()
        help()
    if cmd == "add":
        clear()
        add_contact()
    if cmd == "remove":
        remove_contact()
    if cmd == "show_all":
        clear()
        show_all()
    if cmd == "search":
        clear()
        search_contact()
    

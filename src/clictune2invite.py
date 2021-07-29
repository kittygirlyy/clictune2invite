import requests, os, time, html5lib
from bs4 import BeautifulSoup
from colorama import Fore, Style, init; init()

def logo():
    os.system("cls")
    print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + f'''
  _________  ________  ___ 
  \_   ___ \ \_____  \|   |                  Made by n3k0girl | C++/html5/css3/js/ dev|
  /    \  \/  /  ____/|   |                  
  \     \____/       \|   |                  Make your link faster with C2I
   \______  /\_______ \___|                            
                 
    ''' + Style.RESET_ALL)

resp = ""

def get_request():
    global resp
    pages = 0
    url = "https://www.clictune.com/links/index/" + str(pages)
    pages2 = 0
    pages = int(input(Fore.LIGHTGREEN_EX + f"\n                     [V]Veuillez mettre le nombre de pages (1000 liens = 1 page) =>"))
    cookies = input(Fore.LIGHTGREEN_EX + f"\n                     [V]Veuillez mettre votre cookie de session =>")
    cookies = "ci_session=" + cookies
    while pages2 <= pages:
        pages2 += 1
        click  = requests.get(url, headers = {'Cookie': cookies})
        resp = click.content

def bs4_links():
    soup = BeautifulSoup(resp, "html5lib")
    infos = soup.find_all("a")
    print("\n")
    for lien in infos:
        if "https://www.clictune.com/" in lien.text:
            print(lien.attrs['href'])

if  __name__ == '__main__':
    logo()
    get_request()
    bs4_links()
    print(Style.RESET_ALL + Fore.LIGHTRED_EX + f"\n                     [X]Si le programme ne vous ressort 0 liens, veuillez verifier que votre cookie est valide..." + Style.RESET_ALL)
    input(Fore.RESET + f"\n{Fore.WHITE}Appuyez sur entrée pour quitter...")

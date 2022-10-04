import time
import requests
import random
import threading
import colorama
from colorama import Fore
colorama.init()
import os,sys

os.system('cls')
sys.stdout.write("\x1b]2;Bled Generator | Genning Accounts | Bled V1\x07")
os.system(f'mode con: cols=103 lines=25')

def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text

class generator:

    def __init__(self):

        self.amount = 0
        self.requestsent = 0

        print(f'''
       *          .       *        {Fore.BLUE}██████{Fore.RESET}╗{Fore.BLUE} ██{Fore.RESET}╗{Fore.BLUE}     ███████╗██████╗    {Fore.RESET}*     *    *     '   *      '
            *       '       '      {Fore.BLUE}██{Fore.RESET}╔══{Fore.BLUE}██{Fore.RESET}╗{Fore.BLUE}██{Fore.RESET}║     {Fore.BLUE}██{Fore.RESET}╔════╝{Fore.BLUE}██{Fore.RESET}╔══{Fore.BLUE}██{Fore.RESET}╗           '    *   '   *
              *      *       '     {Fore.BLUE}██████{Fore.RESET}╔╝{Fore.BLUE}██{Fore.RESET}║     {Fore.BLUE}█████{Fore.RESET}╗{Fore.BLUE}  ██{Fore.RESET}║{Fore.BLUE}  ██{Fore.RESET}║     *               *   ' 
      *   '*         '      *    * {Fore.BLUE}██{Fore.RESET}╔══{Fore.BLUE}██{Fore.RESET}╗{Fore.BLUE}██{Fore.RESET}║     {Fore.BLUE}██{Fore.RESET}╔══╝ {Fore.BLUE} ██{Fore.RESET}║{Fore.BLUE}  ██{Fore.RESET}║      *         '  '  *  '   *
      *    *     '         '       {Fore.BLUE}██████{Fore.RESET}╔╝{Fore.BLUE}███████{Fore.RESET}╗{Fore.BLUE}███████{Fore.RESET}╗{Fore.BLUE}██████{Fore.RESET}╔╝     *    *     '                
   *       *    *     '   *    '   ╚═════╝ ╚══════╝╚══════╝╚═════╝   *    *     '          *
               *    *     '         '  *     *    *    *     '         '  *     *                                                 
        ''')
        self.invite = input('               Invite: ')
        print('               Sending ')


        def gen(self):

            try:

                for i in range(1):

                    self.amount += 0
                    self.requestsent +=1
                    sys.stdout.write(f"\x1b]2;Bled Generator | Genned: {self.amount} | Requests Sent: {self.requestsent} | Bled V1\x07")

                    self.proxiess = open('utils/proxies.txt', 'r').read().splitlines()
                    self.proxy = random.choice(self.proxiess)

                    self.names = open('utils/names.txt', 'r').read().splitlines()
                    self.name = random.choice(self.names)

                    session = requests.Session()

                    session.proxies = {
                        'https': f'http://{self.proxy}',
                        'http': f'http://{self.proxy}',
                    }

                    password = randstr(10)
                    firstname = randstr(5)
                    lastname = randstr(5)
                    fullname = f"{firstname} {lastname}"
                    email = randstr(8) + '@gmail.com'

                    json = {"name":self.name,"email":email,"password":password,"fullName":fullname}

                    r = session.post('https://www.guilded.gg/api/users?type=email', json=json)
                    cookie = r.cookies["hmac_signed_session"]
         

                    session.headers = {"cookie": f"hmac_signed_session={cookie}"}
                    resp = session.put(f"https://www.guilded.gg/api/invites/{self.invite}")

                    accountinfo = open('utils/accounts.txt', 'a+')
                    accountinfo.write(f'{email}:{password}\n')

                    self.amount += 1

                    sys.stdout.write(f"\x1b]2;Bled Generator | Genned: {self.amount} | Bled V1\x07")

            except:
                gen(self)


        while True:

            if threading.active_count() < 500:

                threading.Thread(target = gen,args = [self]).start()


generator()

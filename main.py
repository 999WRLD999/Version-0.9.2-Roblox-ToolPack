import requests
import threading
import os
from colorama import Fore
import random
import string
from itertools import cycle
os.system('color')



print(f'[1] Friend Bot\n[2] Follow bot\n[3] Proxyless Friend bot\n[4] Proxyless cookie checker\n[5] UserID Generator\n[6] Ally Bot\n[7] GroupID Generator\n[8] Proxyless GroupID Generator\n[9] Model Buyer\n[10] Model Favorite Bot\n[11] Game Favorite Bot\n[12] Status Changer\n[13] Description Changer\n[14] UnFollow Bot\n[15] UserName Converter' + Fore.RESET)
amount = 0

with open('cookies.txt','r+', encoding='utf-8') as f:
    cookie = cycle(f.read().splitlines())
with open('proxies.txt', 'r+', encoding='utf-8') as f:
    proxy = cycle(f.read().splitlines())

print('\n\n')
choice = input('>>>> ')
def friendbot():
    while True:
        try:
            cookies = {'.ROBLOSECURITY': next(cookie)}

            proxies = {
                'https': 'https://' + next(proxy)
            }


            gathtoken = requests.post('https://www.roblox.com/api/item.ashx?rqtype=purchase&productID=%7BproductId%7D&expectedCurrency=1&expectedPrice=%7Bprice%7D&expectedSellerID=%7BsellerId%7D', cookies=cookies)
            token = gathtoken.headers['x-csrf-token']

            sendfriend = requests.post(f'https://friends.roblox.com/v1/users/{clientid}/request-friendship', cookies=cookies,
                                       headers={'x-csrf-token': token}, proxies=proxies)
            if sendfriend.status_code == 200:
                print(f'{Fore.GREEN}[ + ] Friend Request sent: {clientid}{Fore.RESET}')
            else:
                print(f'{Fore.RED}[ - ] Dead Proxy or already friended{Fore.RESET}')
        except Exception as proxerror:
            print(f'{Fore.RED}[ - ] Error: {proxerror}{Fore.RESET}')
def followbot():
    while True:
        try:
            cookie = open('cookies.txt', 'r').read().split('\n')
            cookierandom = random.choice(cookie)
            proxypool = open('proxies.txt', 'r').read().split('\n')

            cookies = {'.ROBLOSECURITY': cookierandom}

            proxies = {
                'https': 'https://' + random.choice(proxypool)
            }

            gathtoken = requests.post('https://auth.roblox.com/v2/logout', cookies=cookies)
            token = gathtoken.headers['x-csrf-token']

            headers = {'x-csrf-token': token}

            sendfollow = requests.post(f'https://friends.roblox.com/v1/users/{clientid}/follow', cookies=cookies, proxies=proxies, headers=headers)

            if sendfollow.status_code == 200:
                print(f'[{Fore.GREEN} + ] Follow sent: {clientid}{Fore.RESET}')
            else:
                print(f'{Fore.RED}[ - ] Dead Proxy{Fore.RESET}')
        except Exception as proxerror:
            print(f'{Fore.RED}[ - ] Error: {proxerror}{Fore.RESET}')


def unproxyfriend():
    while True:
        try:
            cookies = {'.ROBLOSECURITY': next(cookie)}

            gathtoken = requests.post('https://auth.roblox.com/v2/logout', cookies=cookies)
            token = gathtoken.headers['x-csrf-token']

            sendfriend = requests.post(f'https://friends.roblox.com/v1/users/{clientid}/request-friendship', cookies=cookies,headers={'x-csrf-token': token})
            if sendfriend.status_code == 200:
                print(f'{Fore.GREEN}[ + ] Friend request sent: {clientid}{Fore.RESET}')
            else:
                print(f'{Fore.RED}[ - ] Already friended, Retrying. . .{Fore.RESET}')
        except Exception as proxerror:
            print(f'{Fore.RED}[ - ] Error: {proxerror}{Fore.RESET}')
def proxylesschecker():
    while True:
        cookie = open('cookies.txt','r').read().split('\n')
        cookierandom = random.choice(cookie)

        cookies = {
            '.ROBLOSECURITY': cookierandom
        }

        checkcookie = requests.get('https://www.roblox.com/users/564684169/friends', cookies=cookies)

        if checkcookie.status_code == 200:

            readcookies = open('validcookies.txt', 'r').read().split('\n')
            if cookierandom in readcookies:
                print(f'{Fore.RED}[ - {Fore.RESET}] Cookie already in file: {cookierandom}')
            else:
                print(f'[{Fore.GREEN} - {Fore.RESET}] Cookie Valid: {cookierandom}')
                with open('validcookies.txt', "a+") as f:
                    f.write(cookierandom + "\n")
        else:
            print(f'[{Fore.RED} - ] Dead Cookie: {cookierandom}{Fore.RESET}')
def userid_gen():
    while True:
        try:
            randomnum = ''.join(random.choices(string.digits, k=9))

            findid = requests.get(f'https://www.roblox.com/users/{randomnum}/profile')

            if findid.status_code == 200:
                print(f'{Fore.GREEN}[ + ] ID Valid: {randomnum}{Fore.RESET}')
                with open('validids.txt', "a+") as f:
                    f.write(f'{randomnum}' + '\n')
            else:
                print(f'{Fore.RED}[ - ] ID Invalid: {randomnum}{Fore.RESET}')
        except Exception as err:
            print(f'{Fore.RED}Error: {err}{Fore.RESET}')
def groupally():
    while True:
        try:
            groupids = open('validgroupids.txt', 'r').read().split('\n')

            randomid = random.choice(groupids)
            cookies = {'.ROBLOSECURITY': selfcookie}
            proxies = {
                'https': 'https://' + next(proxy)
            }

            gathtoken = requests.post('https://auth.roblox.com/v2/logout', cookies=cookies)
            token = gathtoken.headers['x-csrf-token']

            headers = {'x-csrf-token': token}

            sendally = requests.post(f'https://groups.roblox.com/v1/groups/{selfgroupid}/relationships/allies/{randomid}', proxies=proxies, headers=headers, cookies=cookies)

            if sendally.status_code == 200:
                print(f'{Fore.GREEN}[ + ] Ally Sent: {randomid}{Fore.RESET}')
            else:
                print(f'{Fore.RED}[ - ] Something Failed, Retrying. . .{Fore.RESET}')
        except Exception as err:
            print(f'{Fore.RED}[ - ] Error: {err}{Fore.RESET}')
def groupidgen():
    while True:
        try:
            randomnum = ''.join(random.choices(string.digits, k=6))

            proxies = {
                'https': 'https://' + next(proxy)
            }

            checkgroup = requests.get(f'https://groups.roblox.com/v1/groups/{randomnum}', proxies=proxies)

            if checkgroup.status_code == 200:
                print(f'{Fore.GREEN}[ + ] GroupID Valid: {randomnum}{Fore.RESET}')
                with open('validgroupids.txt', 'a+') as f:
                    f.write(f'{randomnum}' + '\n')
            else:
                print(f'{Fore.RED}[ - ] GroupID Invalid: {randomnum}{Fore.RESET}')
        except Exception as err:
            print(f'{Fore.RED}[ - ] Error: {err}{Fore.RESET}')
def proxylessgroupidgen():
    while True:
        try:
            randomnum = ''.join(random.choices(string.digits, k=6))

            checkgroup = requests.get(f'https://groups.roblox.com/v1/groups/{randomnum}')

            if checkgroup.status_code == 200:
                print(f'{Fore.GREEN}[ + ] GroupID Valid: {randomnum}{Fore.RESET}')
                with open('validgroupids.txt', 'a+') as f:
                    f.write(f'{randomnum}' + '\n')
            else:
                print(f'{Fore.RED}[ - ] GroupID Invalid: {randomnum}{Fore.RESET}')
        except Exception as err:
            print(f'{Fore.RED}[ - ] Error: {err}{Fore.RESET}')
def modelbuyer():
    while True:
        try:

            cookies = {'.ROBLOSECURITY': next(cookie)}

            gathtoken = requests.post('https://auth.roblox.com/v2/logout', cookies=cookies)
            token = gathtoken.headers['x-csrf-token']

            proxies = {
                'https': 'https://' + next(proxy)
            }

            data = {
                'expectedCurrency': '1',
                'expectedPrice': '0',
                'expectedSellerId': ownermodel
            }

            buymodel = requests.post(f'https://economy.roblox.com/v1/purchases/products/{modelid}', cookies=cookies, proxies=proxies, headers={'x-csrf-token': token}, data=data)
            deletemodel = requests.post('https://www.roblox.com/asset/delete-from-inventory', data={'assetId': modelid},proxies=proxies, cookies=cookies, headers={'x-csrf-token': token})
            if buymodel.status_code == 200:
                print(f'{Fore.GREEN}[ + ] Bought Model: {modelid}{Fore.RESET}')
            else:
                print(f'{Fore.RED}[ - ] Dead Proxy or Already Bought, Retrying. . .{Fore.RESET}')
            if deletemodel.status_code == 200:
                print(f'{Fore.GREEN}[ + ] Deleted Model: {modelid}{Fore.RESET}')
            else:
                print(f'{Fore.RED}[ - ] Dead Proxy or Deleted model, Retrying. . .{Fore.RESET}')
        except Exception as err:
            print(f'{Fore.RED}[ - ] Error: {err}{Fore.RESET}')
def favoritemodel():
    while True:
        try:

            cookies = {'.ROBLOSECURITY': next(cookie)}

            gathtoken = requests.post('https://auth.roblox.com/v2/logout', cookies=cookies)
            token = gathtoken.headers['x-csrf-token']

            proxies = {
                'https': 'https://' + next(proxy)
            }

            data = {
                'itemTargetId': shirtid,
                'favoriteType': 'Asset',
            }

            sendfav = requests.post('https://www.roblox.com/v2/favorite/toggle', data=data, headers={'x-csrf-token': token},proxies=proxies, cookies=cookies)

            if sendfav.status_code == 200:
                print(f'{Fore.GREEN}[ + ] Favorited: {shirtid}{Fore.RESET}')
            else:
                print(f'{Fore.RED}[ - ] Dead Proxy or Deleted model, Retrying. . .{Fore.RESET}')
        except Exception as err:
            print(f'{Fore.RED}[ - ] Error: {err}{Fore.RESET}')
def favoritegame():
    while True:
        try:

            cookies = {'.ROBLOSECURITY': next(cookie)}

            gathtoken = requests.post('https://auth.roblox.com/v2/logout', cookies=cookies)
            token = gathtoken.headers['x-csrf-token']

            proxies = {
                'https': 'https://' + next(proxy)
            }

            data = {
                'assetID': shirtid,
            }

            sendfav = requests.post(' https://www.roblox.com/favorite/toggle', data=data, headers={'x-csrf-token': token},proxies=proxies, cookies=cookies)

            if sendfav.status_code == 200:
                print(f'{Fore.GREEN}[ + ] Favorited: {shirtid}{Fore.RESET}')
            else:
                print(f'{Fore.RED}[ - ] Dead Proxy{Fore.RESET}')
        except Exception as err:
            print(f'{Fore.RED}[ - ] Error: {err}{Fore.RESET}')
def cookienorm():
    while True:
        try:
            cookie = open('cookies.txt', 'r').read().split('\n')
            cookierandom = random.choice(cookie)

            cookies = {'.ROBLOSECURITY': cookierandom}

            gathtoken = requests.post('https://auth.roblox.com/v2/logout', cookies=cookies)
            token = gathtoken.headers['x-csrf-token']

            proxypool = open('proxies.txt', 'r').read().split('\n')
            proxies = {
                'https': 'https://' + random.choice(proxypool)
            }

            setcostume = requests.post('https://www.roblox.com/home/updatestatus', data={'status': f'{status}',}, headers={'x-csrf-token': token}, cookies=cookies, proxies=proxies)
            if setcostume.status_code == 200:
                print(f'{Fore.GREEN}[ + ] Status set: {status}{Fore.RESET}')
            else:
                print(f'{Fore.RED}[ - ] Dead Proxy, or something failed, Retrying. . .{Fore.RESET}')
        except Exception as err:
            print(f'{Fore.RED}[ - ] Error: {err}{Fore.RESET}')
def descriptionchange():
    while True:
        try:

            cookies = {'.ROBLOSECURITY': next(cookie)}

            gathtoken = requests.post('https://auth.roblox.com/v2/logout', cookies=cookies)
            token = gathtoken.headers['x-csrf-token']

            proxies = {
                'https': 'https://' + next(proxy)
            }


            changedesc = requests.post('https://accountinformation.roblox.com/v1/description', cookies=cookies,proxies=proxies, headers={'x-csrf-token': token},data={'description': content})

            if changedesc.status_code == 200:
                print(f'{Fore.GREEN}[ + ] Cookie changed Description: {content}{Fore.RESET}')
            else:
                print(f'{Fore.RED}[ - ] Dead Proxy or already changed, Retrying. . .{Fore.RESET}')
        except Exception as err:
            print(f'{Fore.RED}[ - ] Error: {err}{Fore.RESET}')
def unfollow():
    while True:
        try:
            cookies = {'.ROBLOSECURITY': next(cookie)}

            gathtoken = requests.post('https://auth.roblox.com/v2/logout', cookies=cookies)
            token = gathtoken.headers['x-csrf-token']

            proxypool = open('proxies.txt', 'r').read().split('\n')
            proxies = {
                'https': 'https://' + random.choice(proxypool)
            }

            unfollow = requests.post(f'https://friends.roblox.com/v1/users/{unfollowid}/unfollow', proxies=proxies, cookies=cookies, headers={'x-csrf-token': token})
            if unfollow.status_code == 200:
                print(f'{Fore.GREEN}[ + ] Unfollowed: {unfollowid}')
            else:
                print(f'{Fore.RED}[ - ] Dead Proxy or Not followed, Retrying. . .')
        except Exception as err:
            print(f'{Fore.RED}[ - ] Error: {err}')
def usernamechecker():
    while True:
        try:
            cookieCHECK = next(cookie)
            cookies = {'.ROBLOSECURITY': cookieCHECK}

            proxies = {
                'https': 'https://' + next(proxy)
            }

            checkuser = requests.get('https://www.roblox.com/mobileapi/userinfo', cookies=cookies, proxies=proxies)
            usernam = checkuser.json()['UserName']

            if checkuser.status_code == 200:
                print(f'{Fore.GREEN}[ + ] Username: {usernam} Cookie: {cookieCHECK}')
                with open('usernames.txt', 'a+') as f:
                    if cookieCHECK in f:
                        print(f'{Fore.RED}[ - ] Error: Cookie already in file{Fore.RESET}')
                    f.write(f'Username: {usernam} Cookie: {cookieCHECK} \n')
            else:
                print(f'{Fore.RED}[ - ] Dead Proxy, Retrying. . .{Fore.RESET}')

        except Exception as err:
            print(f'{Fore.RED}[ - ] Error: {err}{Fore.RESET}')
if choice == '1':
    clientid = input('Enter an ID: ')
    num = int(input('Threads: '))
    for i in range(num):
        t1 = threading.Thread(target=friendbot).start()
if choice == '2':
    clientid = input('Enter an ID: ')
    num = int(input('Threads: '))
    for i in range(num):
        t1 = threading.Thread(target=followbot).start()
if choice == '3':
    clientid = input('Enter an ID: ')
    num = int(input('Threads: '))
    for i in range(num):
        t1 = threading.Thread(target=unproxyfriend).start()
if choice == '4':
    num = int(input('Threads: '))
    for i in range(num):
        t1 = threading.Thread(target=proxylesschecker).start()
if choice == '5':
    num = int(input('Threads: '))
    for i in range(num):
        t1 = threading.Thread(target=userid_gen).start()
if choice == '6':
    selfcookie = input('Enter your cookie: ')
    selfgroupid = input('Enter your group ID: ')
    num = int(input('Threads: '))
    for i in range(num):
        t1 = threading.Thread(target=groupally).start()
if choice == '7':
    num = int(input('Threads: '))
    for i in range(num):
        t1 = threading.Thread(target=groupidgen).start()
if choice == '8':
    num = int(input('Threads: '))
    for i in range(num):
        t1 = threading.Thread(target=proxylessgroupidgen).start()
if choice == '9':
    modelid = input('Enter a model ID: ')
    ownermodel = input('Enter the owner\'s ID: ')
    num = int(input('Threads: '))
    for i in range(num):
        t1 = threading.Thread(target=modelbuyer).start()
if choice == '10':
    shirtid = input('Enter a shirt/pant ID: ')
    num = int(input('Threads: '))
    for i in range(num):
        t1 = threading.Thread(target=favoritemodel).start()
if choice == '11':
    shirtid = input('Enter a game ID: ')
    num = int(input('Threads: '))
    for i in range(num):
        t1 = threading.Thread(target=favoritegame).start()
if choice == '12':
    status = input('Enter a Status: ')
    num = int(input('Threads: '))
    for i in range(num):
        t1 = threading.Thread(target=cookienorm).start()
if choice == '13':
    content = input('Enter a description: ')
    num = int(input('Threads: '))
    for i in range(num):
        t1 = threading.Thread(target=descriptionchange).start()
if choice == '14':
    unfollowid = input('Enter an ID: ')
    num = int(input('Threads: '))
    for i in range(num):
        t1 = threading.Thread(target=unfollow).start()
if choice == '15':
    num = int(input('Threads: '))
    for i in range(num):
        t1 = threading.Thread(target=usernamechecker).start()

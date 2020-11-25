import requests
import threading
import os
from colorama import Fore
import random
import time, string
os.system('color')


print(f'[1] Friend Bot\n[2] Follow bot\n[3] Proxyless Friend bot\n[4] Proxyless cookie checker\n[5] UserID Generator\n[6] Ally Bot\n[7] GroupID Generator\n[8] Proxyless GroupID Generator\n[9] Model Buyer\n[10] Model Favorite Bot\n[11] Game Favorite Bot' + Fore.RESET)
amount = 0

print('\n\n\n\n')
choice = input('>>>> ')
def friendbot():

    while True:
        try:
            cookie = open('cookies.txt', 'r').read().split('\n')
            cookierandom = random.choice(cookie)
            proxypool = open('proxies.txt', 'r').read().split('\n')

            cookies = {'.ROBLOSECURITY': cookierandom}

            proxies = {
                'https': 'https://' + random.choice(proxypool)
            }


            gathtoken = requests.post('https://www.roblox.com/api/item.ashx?rqtype=purchase&productID=%7BproductId%7D&expectedCurrency=1&expectedPrice=%7Bprice%7D&expectedSellerID=%7BsellerId%7D', cookies=cookies)
            token = gathtoken.headers['x-csrf-token']

            sendfriend = requests.post(f'https://friends.roblox.com/v1/users/{clientid}/request-friendship', cookies=cookies,
                                       headers={'x-csrf-token': token}, proxies=proxies)
            if sendfriend.status_code == 200:
                print(f'[{Fore.GREEN} + {Fore.RESET}] Friend Request sent: {clientid}')
            else:
                print(f'[{Fore.RED} - {Fore.RESET}] Dead Proxy or already friended')
        except Exception as proxerror:
            print(f'[{Fore.RED} - {Fore.RESET}] Error: {proxerror}')
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
                print(f'[{Fore.GREEN} + {Fore.RESET}] Follow sent: {clientid}')
            else:
                print(f'[{Fore.RED} - {Fore.RESET}] Dead Proxy')
        except Exception as proxerror:
            print(f'[{Fore.RED} - {Fore.RESET}] Erorr: {proxerror}')


def unproxyfriend():
    while True:
        try:
            cookie = open('cookies.txt', 'r').read().split('\n')
            cookierandom = random.choice(cookie)

            cookies = {'.ROBLOSECURITY': cookierandom}

            gathtoken = requests.post('https://auth.roblox.com/v2/logout', cookies=cookies)
            token = gathtoken.headers['x-csrf-token']

            sendfriend = requests.post(f'https://friends.roblox.com/v1/users/{clientid}/request-friendship', cookies=cookies,headers={'x-csrf-token': token})
            if sendfriend.status_code == 200:
                print(f'[{Fore.GREEN} + {Fore.RESET}] Friend request sent: {clientid}')
            else:
                print(f'[{Fore.RED} - {Fore.RESET}] Already friended, Retrying. . .')
        except Exception as proxerror:
            print(f'[{Fore.RED} - {Fore.RESET}] Error: {proxerror}')
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
                print(f'[{Fore.RED} - {Fore.RESET}] Cookie already in file: {cookierandom}')
            else:
                print(f'[{Fore.GREEN} - {Fore.RESET}] Cookie Valid: {cookierandom}')
                with open('validcookies.txt', "a+") as f:
                    f.write(cookierandom + "\n")
        else:
            print(f'[{Fore.RED} - {Fore.RESET}] Dead Cookie: {cookierandom}')
def userid_gen():
    try:
        while True:
            randomnum = ''.join(random.choices(string.digits, k=9))

            findid = requests.get(f'https://www.roblox.com/users/{randomnum}/profile')

            if findid.status_code == 200:
                print(f'[{Fore.GREEN} + {Fore.RESET}] ID Valid: {randomnum}')
                with open('validids.txt', "a+") as f:
                    f.write(f'{randomnum}' + '\n')
            else:
                print(f'[{Fore.RED} - {Fore.RESET}] ID Invalid: {randomnum}')
    except Exception as err:
        print(f'Error: {err}')
def groupally():
    try:
        while True:
            proxypool = open('proxies.txt', 'r').read().split('\n')
            groupids = open('validgroupids.txt', 'r').read().split('\n')

            randomid = random.choice(groupids)
            cookies = {'.ROBLOSECURITY': selfcookie}
            proxies = {
                'https': 'https://' + random.choice(proxypool)
            }

            gathtoken = requests.post('https://auth.roblox.com/v2/logout', cookies=cookies)
            token = gathtoken.headers['x-csrf-token']

            headers = {'x-csrf-token': token}

            sendally = requests.post(f'https://groups.roblox.com/v1/groups/{selfgroupid}/relationships/allies/{randomid}', proxies=proxies, headers=headers, cookies=cookies)

            if sendally.status_code == 200:
                print(f'[{Fore.GREEN} + {Fore.RESET}] Ally Sent: {randomid}')
            else:
                print(f'[{Fore.RED} - {Fore.RESET}] Something Failed, Retrying. . .')
    except Exception as err:
        print(f'[{Fore.RED} - {Fore.RESET}] Dead Proxy')
def groupidgen():
    try:
        while True:
            randomnum = ''.join(random.choices(string.digits, k=6))

            proxypool = open('proxies.txt', 'r').read().split('\n')
            proxies = {
                'https': 'https://' + random.choice(proxypool)
            }

            checkgroup = requests.get(f'https://groups.roblox.com/v1/groups/{randomnum}', proxies=proxies)

            if checkgroup.status_code == 200:
                print(f'[{Fore.GREEN} + {Fore.RESET}] GroupID Valid: {randomnum}')
                with open('validgroupids.txt', 'a+') as f:
                    f.write(f'{randomnum}' + '\n')
            else:
                print(f'[{Fore.RED} - {Fore.RESET}] GroupID Invalid: {randomnum}')
    except Exception as err:
        print(f'[{Fore.RED} - {Fore.RESET}] Dead Proxy')
def proxylessgroupidgen():
    try:
        while True:
            randomnum = ''.join(random.choices(string.digits, k=6))

            checkgroup = requests.get(f'https://groups.roblox.com/v1/groups/{randomnum}')

            if checkgroup.status_code == 200:
                print(f'[{Fore.GREEN} + {Fore.RESET}] GroupID Valid: {randomnum}')
                with open('validgroupids.txt', 'a+') as f:
                    f.write(f'{randomnum}' + '\n')
            else:
                print(f'[{Fore.RED} - {Fore.RESET}] GroupID Invalid: {randomnum}')
    except Exception as err:
        print(f'[{Fore.RED} - {Fore.RESET}] Error: {err}')
def modelbuyer():
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

            data = {
                'expectedCurrency': '1',
                'expectedPrice': '0',
                'expectedSellerId': ownermodel
            }

            buymodel = requests.post(f'https://economy.roblox.com/v1/purchases/products/{modelid}', cookies=cookies, proxies=proxies, headers={'x-csrf-token': token}, data=data)
            deletemodel = requests.post('https://www.roblox.com/asset/delete-from-inventory', data={'assetId': modelid},proxies=proxies, cookies=cookies, headers={'x-csrf-token': token})
            if buymodel.status_code == 200:
                print(f'[{Fore.GREEN} + {Fore.RESET}] Bought Model: {modelid}')
            else:
                print(f'[{Fore.RED} - {Fore.RESET}] Dead Proxy or Already Bought, Retrying. . .')
            if deletemodel.status_code == 200:
                print(f'[{Fore.GREEN} + {Fore.RESET}] Deleted Model: {modelid}')
            else:
                print(f'[{Fore.RED} - {Fore.RESET}] Dead Proxy or Deleted model, Retrying. . .')
        except Exception as err:
            print(f'[{Fore.RED} - {Fore.RESET}] Error: {err}')
def favoritemodel():
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

            data = {
                'itemTargetId': shirtid,
                'favoriteType': 'Asset',
            }

            sendfav = requests.post('https://www.roblox.com/v2/favorite/toggle', data=data, headers={'x-csrf-token': token},proxies=proxies, cookies=cookies)

            if sendfav.status_code == 200:
                print(f'[{Fore.GREEN} + {Fore.RESET}] Favorited: {shirtid}')
            else:
                print(f'[{Fore.RED} - {Fore.RESET}] Dead Proxy or Deleted model, Retrying. . .')
        except Exception as err:
            print(f'[{Fore.RED} - {Fore.RESET}] Error: {err}')
def favoritegame():
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

            data = {
                'assetID': shirtid,
            }

            sendfav = requests.post(' https://www.roblox.com/favorite/toggle', data=data, headers={'x-csrf-token': token},proxies=proxies, cookies=cookies)

            if sendfav.status_code == 200:
                print(f'[{Fore.GREEN} + {Fore.RESET}] Favorited: {shirtid}')
            else:
                print(f'[{Fore.RED} - {Fore.RESET}] Dead Proxy')
        except Exception as err:
            print(f'[{Fore.RED} - {Fore.RESET}] Error: {err}')


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

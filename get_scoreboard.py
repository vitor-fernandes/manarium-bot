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

urllib3.disable_warnings()

wallet = ['0x68cDa53539fC7c5A365f2b61E131A732Cb2f2068']
games = ['Spiky Walls', 'To The Moon', 'In The Woods']

# Generate GSessionID & SID
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


# 3º Request after GSessionID SID
def three(gsessionid, sid, project_name):
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

    data = 'count=1&ofs=2&req0___data__=%7B%22database%22%3A%22projects%2Fplayground-bsc%2Fdatabases%2F(default)%22%2C%22addTarget%22%3A%7B%22query%22%3A%7B%22structuredQuery%22%3A%7B%22from%22%3A%5B%7B%22collectionId%22%3A%22{}%22%7D%5D%2C%22orderBy%22%3A%5B%7B%22field%22%3A%7B%22fieldPath%22%3A%22__name__%22%7D%2C%22direction%22%3A%22ASCENDING%22%7D%5D%7D%2C%22parent%22%3A%22projects%2Fplayground-bsc%2Fdatabases%2F(default)%2Fdocuments%22%7D%2C%22targetId%22%3A6%7D%7D'.format(project_name.replace(' ', '%20'))

    response = requests.post('https://firestore.googleapis.com/google.firestore.v1.Firestore/Listen/channel', headers=headers, params=params, data=data, verify=False)



# 4º Request after GSessionID SID
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


# 5º Request after GSessionID SID (Get Score)
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


def get_score(wallet, project_name):
    gsessionid, sid = one(wallet)
    two(gsessionid, sid)
    three(gsessionid, sid, project_name)
    four(gsessionid, sid)
    raw_score = five(gsessionid, sid)

    formated_score = format_score(raw_score, project_name)

    return formated_score

def format_score(scoreboard, game_name):
    scores = re.findall('\"score\":\{\"integerValue\":\"([0-9]{0,})\"}', scoreboard.replace(' ','').replace('\n',''))
    wallets = re.findall('\{\"stringValue\":\"(0x+[0-9a-zA-Z]{0,})\"\}', scoreboard.replace(' ','').replace('\n',''))

    all_in = []

    for i in range(len(scores)):
        all_in.append([wallets[i], int(scores[i])])

    sorted_list = sorted(all_in, key=operator.itemgetter(1), reverse=True)

    print('[+] {}\' Scoreboard [+]\n - {}\n================================================\n'.format(game_name, "\n - ".join(player[0] + ":" + str(player[1]) for player in sorted_list)))


def main():
    for game in games:
        get_score(wallet[0], game)
        

if __name__ == '__main__':
    main()
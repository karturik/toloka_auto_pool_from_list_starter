import requests
import toloka.client as toloka
import time

URL_API = "https://toloka.yandex.ru/api/v1/"
OAUTH_TOKEN = ''
HEADERS = {"Authorization": "OAuth %s" % OAUTH_TOKEN, "Content-Type": "application/JSON"}
toloka_client = toloka.TolokaClient(OAUTH_TOKEN, 'PRODUCTION')

r = requests.get('https://toloka.dev/api/v1/requester', headers=HEADERS).json()
balance = r['balance']
print('Account balance: ', balance)

if balance >= 100:
    list_of_pools = []

    print('Pool list for start: ', list_of_pools)

    for pool in list_of_pools:
        tries = 0
        while tries < 10:
            try:
                r = requests.post(f'https://toloka.dev/api/v1/pools/{pool}/open', headers=HEADERS)
                print(r.content)
                if 'DOES_NOT_EXIST' in str(r.content):
                    raise NameError('Cant find pool')
                print('Pool started: ', pool)
                tries = 10
            except Exception as e:
                tries += 1
                print(f'Error, try {tries}/10')
                time.sleep(2)
                if 'Cant find pool' in str(e):
                    print('Change account')
                    if OAUTH_TOKEN == '':
                        OAUTH_TOKEN = ''
                    elif OAUTH_TOKEN == '':
                        OAUTH_TOKEN = ''
                    HEADERS = {"Authorization": "OAuth %s" % OAUTH_TOKEN, "Content-Type": "application/JSON"}
                    toloka_client = toloka.TolokaClient(OAUTH_TOKEN, 'PRODUCTION')
                else:
                    print('Pool already started: ', e)


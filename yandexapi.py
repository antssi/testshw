import requests
import time

token = ''

uri = 'https://cloud-api.yandex.net'
headers = {
    'Accept': 'application/json',
    'Authorization': 'OAuth {}'.format(token)
}

def status_check():
    response = requests.get(uri + '/v1/disk', headers=headers)
    return response.status_code

def folder_check(path):
    params = {'path': path}
    response = requests.get(uri + '/v1/disk/resources', headers=headers, params=params)
    if response.status_code == 200:
        return True
    else:
        return False

def folder_create(path):
    time.sleep(2)
    params = {'path': path}
    if folder_check(path) is True:
        return f'already exist'
    response = requests.put(uri + '/v1/disk/resources', headers=headers, params=params)
    time.sleep(2)
    if response.status_code == 201:
        code_status = response.status_code
        return code_status, folder_check(path)
    return f'check status'


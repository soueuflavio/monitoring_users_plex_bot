"""
Monitoring users plex and stop Docker transmission and deluge
"""
import time
import requests
from config import TOKEN_ID,CHAT_ID,tautulli_apikey,tautulli_url_port,docker_nas_url
response = requests.get('http://'+tautulli_url_port+'/api/v2?apikey='+tautulli_apikey+'&cmd=get_activity')

if response.status_code == 200:
    payload = response.json()

    qtde_Usuario = int(payload.get("response").get("data").get("stream_count"))
    if qtde_Usuario == 0:
        print('Nao encontrado espectadores')
        response = requests.get('http://'+docker_nas_url+'/containers/json?filters={"status":["paused"],"name":["delugeTv","transmissionMovies"]}')
        if response.status_code == 200:
            containers = response.json()
            for container in containers:
                print('Retomando serviços' + container.get("Id"))
                response = requests.post('http://'+docker_nas_url+'/containers/'+container.get("Id")+'/unpause')

    else:
        print('Encontrado ' + str(qtde_Usuario) + ' espectadores')
        response = requests.get('http://'+docker_nas_url+'/containers/json?filters={"status":["running"],"name":["delugeTv","transmissionMovies"]}')
        if response.status_code == 200:
            containers = response.json()
            for container in containers:
                print('Parando serviços' + container.get("Id"))
                response = requests.post('http://'+docker_nas_url+'/containers/'+container.get("Id")+'/pause')

elif response.status_code == 404:
    print('Not Found.')

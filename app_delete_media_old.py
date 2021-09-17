"""
Monitoring users plex and stop Docker transmission and deluge
"""
import datetime
from config import *
from datetime import timedelta
import os # import the os module

def formatHour(days_and_time):
    days = days_and_time.days
    seconds = days_and_time.seconds
    hours = seconds//3600
    minutes = (seconds//60)%60
    result = 'd' + str(days) + 'h' + str(hours) + 'm' + str(minutes)
    return result

def apagarFilmesAntigos():
        # Apagar diretório temporario com filmes antigos no servidor
    delete_path = "/media/downloads/movies/deleting"
    try:
        os.rmdir(delete_path)
    except OSError:
        print ("Deletion of the directory %s failed" % delete_path)
    else:
        print ("Successfully deleted the directory %s" % delete_path)
    return 'sucess'


def filter_movies_directory():
    # Criar diretório temporario para migrar filmes a apagar
    create_path = "/media/downloads/movies/deleting"
    try:
        os.mkdir(create_path)
    except OSError:
        print ("Creation of the directory %s failed" % create_path)
    else:
        print ("Successfully created the directory %s " % create_path)

    # Navigate diretório /media/downloads/movies/complete e obter titulos antigos
    path = '/media/downloads/movies/complete'
    listaDiretorio = os.listdir(path)

    print("---------------------------------------------------------------------------------------------------")
    datetime_today = datetime.datetime.now()
    days_valid = timedelta(days = 22)

    print("Date Today: " + str(datetime_today) + "Days is Valid: " + str(days_valid))
    print("---------------------------------------------------------------------------------------------------")
    print("- Move Directory: " + path + " to: "+ create_path + '/')
    print("---------------------------------------------------------------------------------------------------")

    listaDiretorio.sort()
    for nomePasta in listaDiretorio:
        fullpath = path +'/'+ nomePasta
        #print(os.stat(path +'/'+ nomePasta).st_ctime)
        datetime_file = datetime.datetime.fromtimestamp(os.stat(fullpath).st_ctime)
        dif_date_file_create = (datetime_today - datetime_file)
            
        if dif_date_file_create > days_valid:
            
            dataDisponivel = str(formatHour(dif_date_file_create))

            os.rename(path + '/' + nomePasta, create_path + '/' + nomePasta)

            print('Disponivel: ' + str(dataDisponivel) + " Move: " + nomePasta )

filter_movies_directory()
#apagarFilmesAntigos()

from bs4 import BeautifulSoup
import requests
def rastreio(cod_ras,last,horas =[],eventos =[]):
    #Sending Post
    rastreio = requests.post('https://www2.correios.com.br/sistemas/rastreamento/resultado.cfm',data = {'Objetos':cod_ras}).text
    soup = BeautifulSoup(rastreio,"html5lib")
    #Scraping 
    for table in soup.find_all('table',class_='listEvent sro'):
        for hora in table.find_all('td',class_='sroDtEvent'):
            horas.append(hora.text.replace('\n','').replace('      ',''))
        for evento in table.find_all('td',class_='sroLbEvent'):
            eventos.append(evento.text.replace('\n',''))
    #Printing 
    if (len(horas) < 1):
        print('Número de rastreio '+ cod_ras +' incorreto ou inexistente !'+'\n')
    else:
        print('Rastreio : '+cod_ras)
        for x in range(0,len(horas)):
            print(horas[x] + ' - '+ eventos[x])
    #Clearing Lists
    horas.clear()
    eventos.clear()
      
def Main():
    horas = []
    eventos = []
    cod_rastreio = ['JT936833164BR','JT936836452BR']
    for x in range(0,len(cod_rastreio)):
        rastreio(cod_rastreio[x],horas,eventos)
        print('\n')
    
Main()

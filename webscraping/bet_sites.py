import requests 
import json
import csv



headersA = {
"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
"Accept": "application/json",
"Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6",
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"X-NewRelic-ID" : "VQUOU1VRDRABV1RUDwADUFwJ",
"Connection": "keep-alive",
"newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjEzOTIzMjUiLCJhcCI6IjEzNTY4MTQ3NTQiLCJpZCI6IjNjYWViNDgwMTI4NTY0NTQiLCJ0ciI6IjcwNTAxZWY2ZDk5NjNhN2E3MWE1OTdhODJmMTI5MDgwIiwidGkiOjE2MzU2ODczNDk4NDB9fQ==",
"X-Requested-With": "XMLHttpRequest",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Dest": "empty",
"Cookie": "fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef = WAe9uchwvvaABHfmTfm5000nUfSyiwHKY3+UOr5rVN0"
}

#inutile = ["tracestate: 1392325^@nr=0-1-1392325-1356814754-3caeb48012856454----1635687349840",
#           "traceparent: 00-70501ef6d9963a7a71a597a82f129080-3caeb48012856454-01", "sec-ch-ua-mobile: ?0"]

headersB = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
}
urlA = 'https://www.goldbet.it/getOverviewEvents/0?idDiscipline=1&idTournament=93&idSection=0&tournamentName=Serie%20A&isFromUser=true'

urlB = 'https://www.goldbet.it/getOverviewEvents/0?idDiscipline=1&idTournament=1626630&idSection=0&tournamentName=Serie%20B&isFromUser=true'

urlC = 'https://www.goldbet.it/getOverviewEvents/0?idDiscipline=1&idTournament=36068&idSection=0&tournamentName=Serie%20C%20-%20Girone%20B&isFromUser=true'

urlP = 'https://www.goldbet.it/getOverviewEvents/0?idDiscipline=1&idTournament=38094&idSection=0&tournamentName=Campionato%20Primavera&isFromUser=true'
#Primavera italiana
urlBI = 'https://www.goldbet.it/getOverviewEvents/0?idDiscipline=1&idTournament=26623&idSection=0&tournamentName=Championship&isFromUser=true'
#BI sta per serie B inglese, cioè la Championship

urlCI = 'https://www.goldbet.it/getOverviewEvents/0?idDiscipline=1&idTournament=26637&idSection=0&tournamentName=League%20One&isFromUser=true'
#CI sta per serie C inglese, cioè la League One

urlCN = 'https://www.goldbet.it/getOverviewEvents/0?idDiscipline=1&idTournament=26672&idSection=0&tournamentName=Conference%20National&isFromUser=true'
#CN sta per Conference National, covo di criminali

responseSERIEA = requests.get(urlA, headers=headersA)
responseSERIEB = requests.get(urlB, headers=headersB)
responseSERIEC = requests.get(urlC, headers=headersB)
responsePRIMAVERA = requests.get(urlP, headers=headersB)
responseBI = requests.get(urlBI, headers=headersB)
responseCI = requests.get(urlCI, headers=headersB)
responseCN = requests.get(urlCN, headers=headersB)

def CreaLista(data, superlista):
    for partita in data:
        INTERESTING_DATA = {'partita': partita['en'], 'orario': partita['ed'], 'quota1': partita['mmkW']['111;355;4001;0;0']['spd']['0.0']['asl'][0]['ov'], 'quotaX': partita['mmkW']['111;355;4001;0;0']['spd']['0.0']['asl'][1]['ov'],
                            'quota2': partita['mmkW']['111;355;4001;0;0']['spd']['0.0']['asl'][2]['ov'], 'under0.5': partita['mmkW']['111;355;4002;0;0']['spd']['0.5']['asl'][0]['ov'], 'over0.5': partita['mmkW']['111;355;4002;0;0']['spd']['0.5']['asl'][1]['ov'],
                            'under1.5': partita['mmkW']['111;355;4002;0;0']['spd']['1.5']['asl'][0]['ov'], 'over1.5': partita['mmkW']['111;355;4002;0;0']['spd']['1.5']['asl'][1]['ov'], 'under2.5': partita['mmkW']['111;355;4002;0;0']['spd']['2.5']['asl'][0]['ov'],
                            'over2.5': partita['mmkW']['111;355;4002;0;0']['spd']['2.5']['asl'][1]['ov'], 'under3.5': partita['mmkW']['111;355;4002;0;0']['spd']['3.5']['asl'][0]['ov'], 'over3.5': partita['mmkW']['111;355;4002;0;0']['spd']['3.5']['asl'][1]['ov'],
                            'GG': partita['mmkW']['111;355;4004;0;0']['spd']['0.0']['asl'][0]['ov'], 'NG': partita['mmkW']['111;355;4004;0;0']['spd']['0.0']['asl'][1]['ov'], '1X': partita['mmkW']['111;355;4006;0;0']['spd']['0.0']['asl'][0]['ov'], '1-2': partita['mmkW']['111;355;4006;0;0']['spd']['0.0']['asl'][1]['ov'],
                            'X2': partita['mmkW']['111;355;4006;0;0']['spd']['0.0']['asl'][2]['ov']}
        superlista.append(INTERESTING_DATA)
        OmegaListone.append(INTERESTING_DATA)

gamedataA = responseSERIEA.json()
dataA = gamedataA['leo']
with open("jsonresponseA.json", "w") as outfileA:
    outfileA.write(json.dumps(gamedataA['leo'], indent=2))

gamedataB = responseSERIEB.json()
dataB = gamedataB['leo']
with open("jsonresponseB.json", "w") as outfileB:
    outfileB.write(json.dumps(gamedataB['leo'], indent=2))

gamedataC = responseSERIEC.json()
dataC = gamedataC['leo']
with open("jsonresponseC.json", "w") as outfileC:
    outfileC.write(json.dumps(gamedataC['leo'], indent=2))

gamedataP = responsePRIMAVERA.json()
dataP = gamedataP['leo']
with open("jsonresponsePrimavera.json", "w") as outfileP:
    outfileP.write(json.dumps(gamedataP['leo'], indent=2))

gamedataBI = responseBI.json()
dataBI = gamedataBI['leo']
with open("jsonresponseBI.json", "w") as outfileBI:
    outfileBI.write(json.dumps(gamedataBI['leo'], indent=2))

gamedataCI = responseCI.json()
dataCI = gamedataCI['leo']
with open("jsonresponseCI.json", "w") as outfileCI:
    outfileCI.write(json.dumps(gamedataCI['leo'], indent=2))

gamedataCN = responseCN.json()
dataCN = gamedataCN['leo']
with open("jsonresponseCN.json", "w") as outfileCN:
    outfileCN.write(json.dumps(gamedataCN['leo'], indent=2))

OmegaListone = []

#print(partita[0]['en'] + ", orario: " + partita[0]['ed'] + " quota 1: " + str(partita[0]['mmkW']['111;355;4001;0;0']['spd']['0.0']['asl'][0]['ov']) + " quota X: "
#      + str(partita[0]['mmkW']['111;355;4001;0;0']['spd']['0.0']['asl'][1]['ov']) + " quota 2: " + str(partita[0]['mmkW']['111;355;4001;0;0']['spd']['0.0']['asl'][2]['ov']))
#print(gamepartita)
superListA = []
superListB = []
superListC = []
superListP = []
superListBI = []
superListCI = []
CreaLista(dataA, superListA)
CreaLista(dataB, superListB)
CreaLista(dataC, superListC)
CreaLista(dataP, superListP)
CreaLista(dataBI, superListBI)
CreaLista(dataCI, superListCI)



with open("DATI.csv", 'w') as csvfile:
    keys = ['partita', 'orario', 'quota1', 'quotaX', 'quota2', 'under0.5', 'over0.5', 'under1.5',
            'over1.5', 'under2.5', 'over2.5', 'under3.5', 'over3.5', 'GG', 'NG', '1X', '1-2', 'X2']
    w = csv.DictWriter(csvfile, fieldnames=keys)
    w.writeheader()
    w.writerows(OmegaListone)

with open("omegaListone.json", "w") as omegaListoneFile:
    omegaListoneFile.write(json.dumps(OmegaListone, indent=2))

print(OmegaListone)
#REFRESH CONTINUO E VEDERE QUALI QUOTE SONO QUELLE CON IL MAGGIORE CALO NEI VARI REFRESH (CIOE VEDERE IL DELTA)
import flask
import pymongo
import random
from flask import jsonify
from flask import request 
connessione = pymongo.MongoClient("mongodb+srv://admin:123@dbcluster.rxes2.mongodb.net/DBCluster?retryWrites=true&w=majority")#connessione con stringa
print(connessione.list_database_names())#stampa connessione
dataName  = connessione["DB_PAROLE"]
dataCollection=dataName["DB_nomi"]#aggiungere altre due collection per le restanti parole
dataCollectionVerbi=dataName["DB_verbi"] #collection verbi


def ricercaParole(dataCollection,dataCollectionVerbi):
    oggetto = ""
    scelta= random.randint(0,8913)
    for i in dataCollection.find({"id":scelta},{"_id":0},):
        soggetto=i['nome'] #variabile che conterrà il valore del soggetto 1
        print(soggetto)
    scelta= random.randint(0,334952)
    for i in dataCollectionVerbi.find({"id":scelta},{"_id":0},):
        verbo=i['valore'] #variabile che conterrà il valore del verbo
        print(verbo)
    scelta= random.randint(0,8913)
    for i in dataCollection.find({"id":scelta},{"_id":0},):
        oggetto=i['nome'] #variabile che conterrà il valore dell'oggetto
        print(oggetto)




    return soggetto,verbo,oggetto

def parolaDiPartenza (dataCollection,dataCollectionVerbi):
    soggetto = input('inserisci la parola di partenza')
    scelta= random.randint(0,334952)
    for i in dataCollectionVerbi.find({"id":scelta},{"_id":0},):
        verbo=i['valore'] #variabile che conterrà il valore del verbo
        print(verbo)
    scelta= random.randint(0,8912)
    for i in dataCollection.find({"id":scelta},{"_id":0},):
        oggetto=i['nome'] #variabile che conterrà il valore dell'oggetto
        print(oggetto)



    return soggetto," ",verbo," ",oggetto
def ricercaAzione (dataCollectionVerbi):
    scelta= random.randint(0,334952)
    for i in dataCollectionVerbi.find({"id":scelta},{"_id":0},):
        verbo=i['valore'] #variabile che conterrà il valore del verbo
        print(verbo)
    return verbo
    

def ScriviDati(a,b):
    print(a," ",b)
    
    
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/Genera', methods=['GET'])
def home():
    return jsonify(ricercaParole(dataCollection,dataCollectionVerbi))

@app.route('/Spunto',methods =['GET'])
def spunto():
    return jsonify(parolaDiPartenza (dataCollection,dataCollectionVerbi))

@app.route('/Azione',methods =['GET'])
def azione():
    return jsonify(ricercaAzione (dataCollectionVerbi))




    

    
app.run()
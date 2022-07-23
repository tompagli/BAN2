from time import strftime
import pymongo
from connection import *




def insert_db(tupla,dados):
    mydb = connect_db()
    mycol = mydb[tupla]

    if mycol == 'Instrumento':
        dados_l = dados.split(",")
        nome = dados_l[0] 
        cod_interno = dados_l[1] 
        cod_play = dados_l[2]
        mydict = { "nome": nome, "cod_interno": cod_interno, "cod_play":cod_play}
        x = mycol.insert_one(mydict)
        return x 
    
    if mycol == 'Musica':
        dados_l = dados.split(",")
        titulom = dados_l[0]
        autor = dados_l[1] 
        cod_mus= (dados_l[2])
        cod_dis= (dados_l[3])
        mydict = { "titulom": titulom, "autor": autor, "cod_mus":cod_mus, "cod_dis": cod_dis}
        x = mycol.insert_one(mydict)
        return x
    
    if mycol == 'Disco':
        dados_l = dados.split(",")
        titulod = (dados_l[0])
        data = strftime(dados_l[1])
        id = (dados_l[2])
        formato = (dados_l[3])
        cod_mus = (dados_l[4])
        cod_b = (dados_l[5])
        mydict = {"titulod": titulod, "data": data, "id": id, "formato": formato, "cod_mus": cod_mus, "cod_b": cod_b}
        x = mycol.insert_one(mydict)
        return x
    
    if mycol == 'Musico':       
        dados_l = dados.split(",")
        nome = (dados_l[0])
        n_regs = (dados_l[1])
        telefone = (dados_l[2]) 
        casa = (dados_l[3])
        n_banda = (dados_l[4])
        cod_play = (dados_l[5])
        mydict = {"nome": nome, "n_regs": n_regs, "telefone": telefone, "casa": casa, "n_banda":n_banda, "cod_play": cod_play}
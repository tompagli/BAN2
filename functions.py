
from time import strftime
from unittest.util import strclass
import psycopg2
from classes import *

lista_instrumento = []
lista_tocar = []
lista_musica = []
lista_disco = []
lista_musico = []
lista_endereco = []
lista_banda = []
lista_produtor = []

def insert(table,dados):
    connection=psycopg2.connect("dbname=gravadora user=postgres password=udesc") ## conexao com o bd
    cursor=connection.cursor() 
    if table == 'Instrumento' : ##instrumento

        dados_l = dados.split(",")
        nome = dados_l[0] #str(input()) ## input do q entra na tupla
        cod_interno = dados_l[1] # int(input())

        cursor.execute("INSERT INTO Instrumento VALUES(%s,%s)", (nome,cod_interno)) ##injetar os valores na tabela
        connection.commit()
        
        instrumento_instance = instrumento(nome,cod_interno)
        lista_instrumento.append(instrumento_instance)

    if table == 'tocar' : ##tocar

        dados_l = dados.split(",")
        cod_int = int(dados_l[0]) 
        cod_mus= int(dados_l[1]) 

        cursor.execute("INSERT INTO tocar VALUES(%s,%s)", (cod_int,cod_mus))
        connection.commit()

        tocar_instance = tocar(cod_int,cod_mus)
        lista_tocar.append(tocar_instance)

    if table == 'Musica' : ##musica

        dados_l = dados.split(",")
        titulom = dados_l[0] #str(input()) ## input do q entra na tupla
        autor = dados_l[1] # int(input())
        cod_mus= int(dados_l[2])
        cod_dis= int(dados_l[3])

        cursor.execute("INSERT INTO Musica VALUES(%s,%s,%s,%s)", (titulom,autor,cod_mus,cod_dis))
        connection.commit()

        musica_instance = musica(titulom,autor,cod_mus,cod_dis)
        lista_musica.append(musica_instance)

    if table == 'Disco' : ##disco

        dados_l = dados.split(",")
        titulod = str(dados_l[0]) #str(input()) ## input do q entra na tupla
        data = strftime(dados_l[1]) # int(input())
        id = int(dados_l[2])
        formato = str(dados_l[3])
        cod_mus = int(dados_l[4])
        cod_b = int(dados_l[5])

        cursor.execute("INSERT INTO Disco VALUES(%s,%s,%s,%s,%s,%s)", (titulod,data,id,formato,cod_mus,cod_b))
        connection.commit()

        disco_instance = disco(titulod,data,id,formato,cod_mus,cod_b)
        lista_disco.append(disco_instance)

    if table == 'Musico' : ##musico
        
        dados_l = dados.split(",")
        nome = str(dados_l[0])
        n_regs = int(dados_l[1])
        num_tel = int(dados_l[2]) 
        n_casa = int(dados_l[3])

        cursor.execute("INSERT INTO Musico VALUES(%s,%d,%d,%d)", (nome,n_regs,num_tel,n_casa))
        connection.commit()

        musico_instance = musico(nome,n_regs,num_tel,n_casa)
        lista_musico.append(musico_instance)

    if table == 'Endereco' : ## endereco
        dados_l = dados.split(",")
        casa = int(dados_l[0]) 
        telefone= int(dados_l[1]) 

        cursor.execute("INSERT INTO Endereco VALUES(%d,%d)", (casa,telefone))
        connection.commit()

        endereco_instance = endereco(casa,telefone)
        lista_endereco.append(endereco_instance)

    if table == 'Banda' : ## banda 
        dados_l = dados.split(",")
        codb = int(dados_l[0]) 
        cod_mus= int(dados_l[1])
        nome = str(dados_l[2])

        cursor.execute("INSERT INTO Banda VALUES(%d,%d,%s)",(codb,cod_mus,nome))
        connection.commit()

        banda_instance = banda(codb,cod_mus,nome)
        lista_banda.append(banda_instance)

    if table == 'Produtor' : ## produtor

        dados_l = dados.split(",")
        cod_mus = int(dados_l[0]) 
        cod_dis = int(dados_l[1]) 
        codp = int(dados_l[3])

        cursor.execute("INSERT INTO Produtor VALUES (%d,%d,%d)",(cod_mus,cod_dis,codp))
        connection.commit()

        produtor_instance = produtor(cod_mus,cod_dis,codp)
        lista_produtor.append(produtor_instance)

    connection.close()

def view(table):
    connection=psycopg2.connect("dbname=gravadora user=postgres password=udesc")
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM " + table)
    rows=cursor.fetchall()
    connection.close()
    return rows

lista_instrumento = instrumento.build(view('Instrumento'))
lista_tocar = view('tocar')
lista_musica = view('Musica')
lista_disco = view('Disco')
lista_musico = view('Musico')
lista_endereco = view('Endereco')
lista_banda = view('Banda')
lista_produtor = view('Produtor')

def separa_por_parametro(lista,campo,valor):
    lista_separada = []
    lista = globals()["lista_"+lista]
    if valor=='':
        return lista
    for x in lista:
        if getattr(x,campo) ==valor:
            lista_separada.append(x)
        return lista_separada

   




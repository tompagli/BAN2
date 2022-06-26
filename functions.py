
from time import strftime
from unittest.util import strclass
import psycopg2
from classes import *

def init():
    lista_instrumento = view(1)
    lista_tocar = view(2)
    lista_musica = view(3)
    lista_disco = view(4)
    lista_musico = view(5)
    lista_endereco = view(6)
    lista_banda = view(7)
    lista_produtor = view(8)

def separa_por_parametro(lista,campo,valor):
    lista_separada = []
    for x in lista:
        if getattr(x,campo) ==valor:
            lista_separada.append(x)
    return lista_separada


def insert(table):
    connection=psycopg2.connect("dbname=gravadora user=postgres password=udesc") ## conexao com o bd
    cursor=connection.cursor() ## sei la eu 
    if table== 1 : ##instrumento
        nome = str(input()) ## input do q entra na tupla
        cod_interno = int(input())
        
        cursor.execute("INSERT INTO Instrumento VALUES(%s,%s)", (nome,cod_interno)) ##injetar os valores na tabela
        connection.commit()
        
        instrumento_instance = instrumento(nome,cod_interno)
        lista_instrumento.append(instrumento_instance)

    if table== 2 : ##tocar
        cod_int = int(input())
        cod_mus = int(input())
        cursor.execute("INSERT INTO tocar VALUES(%s,%s)", (cod_int,cod_mus))
        connection.commit()
    if table== 3 : ##musica
        titulom = str(input())
        autor = str(input())
        cod_mus = int(input())
        cod_dis = int(input())
        cursor.execute("INSERT INTO Musica VALUES(%s,%s,%s,%s)", (titulom,autor,cod_mus,cod_dis))
        connection.commit()
    if table == 4 : ##disco
        titulod = str(input())
        data = strftime(input())
        id = int(input())
        formato = str(input())
        cod_mus = int(input())
        cod_b = int(input())
        cursor.execute("INSERT INTO Disco VALUES(%s,%s,%s,%s,%s,%s)", (titulod,data,id,formato,cod_mus,cod_b))
        connection.commit()
    if table == 5 : ##musico
        nome = str(input())
        n_regs = int(input())
        num_tel = int(input())
        n_casa = int(input())
        cursor.execute("INSERT INTO Musico VALUES(%s,%d,%d,%d)", (nome,n_regs,num_tel,n_casa))
        connection.commit()
    if table == 6 : ## endereco
        casa = int(input())
        telefone = int(input())
        cursor.execute("INSERT INTO Endereco VALUES(%d,%d)", (casa,telefone))
        connection.commit()
    if table == 7 : ## banda 
        codb = int(input())
        cod_mus = int(input())
        nome = str(input())
        cursor.execute("INSERT INTO Banda VALUES(%d,%d,%s)",(codb,cod_mus,nome))
        connection.commit()
    if table == 8 : ## produtor
        cod_mus = int(input())
        cod_dis = int(input())
        codp = int(input())
        cursor.execute("INSERT INTO Produtor VALUES (%d,%d,%d)",(cod_mus,cod_dis,codp))
        connection.commit()
    connection.close()

def view(table):
    connection=psycopg2.connect("dbname=gravadora user=postgres password=udesc")
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM " + table)
    rows=cursor.fetchall()
    connection.close()
    print(rows)
    return rows


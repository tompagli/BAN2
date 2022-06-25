
from time import strftime
from unittest.util import strclass
from classes import *
import psycopg2

def insert(table):
    connection=psycopg2.connect("dbname=gravadora user=postgres password=udesc") ## conexao com o bd
    cursor=connection.cursor() ## sei la eu 
    if table== 1 : ##instrumento
        nome = str(input()) ## input do q entra na tupla
        cod_interno = int(input())
        cursor.execute("INSERT INTO Instrumento VALUES(%s,%s)", (nome,cod_interno)) ##injetar os valores na tabela
        connection.commit()
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

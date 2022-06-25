
from time import strftime
from unittest.util import strclass
import classes
import psycopg2

def insert(table):
    connection=psycopg2.connect("dbname=gravadora user=postgres password=udesc")
    cursor=connection.cursor()
    if table=='1': ##instrumento
        nome = str(input())
        cod_interno = int(input())
        cursor.execute("INSERT INTO Instrumento VALUES(%s,%d)", (nome,cod_interno))
        connection.commit()
    if table=='2': ##tocar
        cod_int = int(input())
        cod_mus = int(input())
        cursor.execute("INSERT INTO tocar VALUES(%d,%d)", (cod_int,cod_mus))
        connection.commit()
    if table=='3': ##musica
        titulom = str(input())
        autor = str(input())
        cod_mus = int(input())
        cod_dis = int(input())
        cursor.execute("INSERT INTO Musica VALUES(%s,%s,%d,%d)", (titulom,autor,cod_mus,cod_dis))
        connection.commit()
    if table == '4': ##disco
        titulod = str(input())
        data = strftime(input())
        id = int(input())
        formato = str(input())
        cod_mus = int(input())
        cod_b = int(input())
        cursor.execute("INSERT INTO Disco VALUES(%s,%d)", (titulod,data,id,formato,cod_mus,cod_b))
        connection.commit()
    if table == '5': ##musico
        nome = str(input())
        n_regs = int(input())
        num_tel = int(input())
        n_casa = int(input())
        cursor.execute("INSERT INTO Musico VALUES(%s,%d,%d,%d)", (nome,n_regs,num_tel,n_casa))
        connection.commit()
    if table == '6' : ## endereco
        casa = int(input())
        telefone = int(input())
        cursor.execute("INSERT INTO Endereco VALUES(%d,%d)", (casa,telefone))
        connection.commit()
    if table == '7' : ## banda 
        codb = int(input())
        cod_mus = int(input())
        nome = str(input())
        cursor.execute("INSERT INTO Banda VALUES(%d,%d,%s)",(codb,cod_mus,nome))
        connection.commit()
    if table == '8' : ## produtor
        cod_mus = int(input())
        cod_dis = int(input())
        codp = int(input())
        cursor.execute("INSERT INTO Produtor VALUES (%d,%d,%d)",(cod_mus,cod_dis,codp))
        connection.commit()
    connection.close()

def view():
    connection=psycopg2.connect("dbname=gravadora user=postgres password=udesc")
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM store")
    rows=cursor.fetchall()
    connection.close()
    return rows
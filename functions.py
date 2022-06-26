
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

def insert(table):
    connection=psycopg2.connect("dbname=gravadora user=postgres password=udesc") ## conexao com o bd
    cursor=connection.cursor() 
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

        tocar_instance = tocar(cod_int,cod_mus)
        lista_tocar.append(tocar_instance)

    if table== 3 : ##musica
        titulom = str(input())
        autor = str(input())
        cod_mus = int(input())
        cod_dis = int(input())

        cursor.execute("INSERT INTO Musica VALUES(%s,%s,%s,%s)", (titulom,autor,cod_mus,cod_dis))
        connection.commit()

        musica_instance = musica(titulom,autor,cod_mus,cod_dis)
        lista_musica.append(musica_instance)

    if table == 4 : ##disco
        titulod = str(input())
        data = strftime(input())
        id = int(input())
        formato = str(input())
        cod_mus = int(input())
        cod_b = int(input())

        cursor.execute("INSERT INTO Disco VALUES(%s,%s,%s,%s,%s,%s)", (titulod,data,id,formato,cod_mus,cod_b))
        connection.commit()

        disco_instance = disco(titulod,data,id,formato,cod_mus,cod_b)
        lista_disco.append(disco_instance)

    if table == 5 : ##musico
        nome = str(input())
        n_regs = int(input())
        num_tel = int(input())
        n_casa = int(input())

        cursor.execute("INSERT INTO Musico VALUES(%s,%d,%d,%d)", (nome,n_regs,num_tel,n_casa))
        connection.commit()

        musico_instance = musico(nome,n_regs,num_tel,n_casa)
        lista_musico.append(musico_instance)

    if table == 6 : ## endereco
        casa = int(input())
        telefone = int(input())

        cursor.execute("INSERT INTO Endereco VALUES(%d,%d)", (casa,telefone))
        connection.commit()

        endereco_instance = endereco(casa,telefone)
        lista_endereco.append(endereco_instance)

    if table == 7 : ## banda 
        codb = int(input())
        cod_mus = int(input())
        nome = str(input())

        cursor.execute("INSERT INTO Banda VALUES(%d,%d,%s)",(codb,cod_mus,nome))
        connection.commit()

        banda_instance = banda(codb,cod_mus,nome)
        lista_banda.append(banda_instance)

    if table == 8 : ## produtor
        cod_mus = int(input())
        cod_dis = int(input())
        codp = int(input())

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

def separa_por_parametro(lista,campo,valor):
    lista_separada = []
    for x in lista:
        if getattr(x,campo) ==valor:
            lista_separada.append(x)
    return lista_separada
   
lista_instrumento = view('Instrumento')
lista_tocar = view('tocar')
lista_musica = view('Musica')
lista_disco = view('Disco')
lista_musico = view('Musico')
lista_endereco = view('Endereco')
lista_banda = view('Banda')
lista_produtor = view('Produtor')

print(lista_instrumento)


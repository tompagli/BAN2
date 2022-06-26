
import datetime
from mailbox import NotEmptyError

class instrumento: 
    def __init__(self,nome,cod_interno):
     self.nome = nome
     self.cod_interno = cod_interno
    def build(lista_tuplas_database):
        lista_ret = []
        for x in lista_tuplas_database:
            lista_ret.append(instrumento(x[0],x[1]))
        return lista_ret
    def __str__(self):
        return self.nome +" | "+ str(self.cod_interno)
    def __repr__(self):
        return self.nome +" | "+ str(self.cod_interno)


class tocar:
    def __init__(self,cod_int,cod_mus):
        self.cod_int = cod_int
        self.cod_mus = cod_mus
    def build(lista_tuplas_database):
        lista_ret = []
        for x in lista_tuplas_database:
            lista_ret.append(tocar(x[0],x[1]))
        return lista_ret


class musica:
    def __init__(self,titulom,autor,cod_mus,cod_dis):
        self.titulom = titulom
        self.autor = autor
        self.cod_mus = cod_mus
        self.cod_dis = cod_dis
    def build(lista_tuplas_database):
        lista_ret = []
        for x in lista_tuplas_database:
            lista_ret.append(musica(x[0],x[1],x[2],x[3]))
        return lista_ret

class disco:
    def __init__(self,titulod,data,id,formato,cod_mus,cod_b):
        self.titulod = titulod
        self.data = data
        self.id = id
        self.formato = formato
        self.cod_mus = cod_mus
        self.cod_b = cod_b
    def build(lista_tuplas_database):
        lista_ret = []
        for x in lista_tuplas_database:
            lista_ret.append(disco(x[0],x[1],x[2],x[3],x[4],x[5]))
        return lista_ret

class musico:
    def __init__(self,nome,n_regs,num_tel,n_casa):
        self.nome = nome
        self.n_regs = n_regs
        self.num_tel = num_tel
        self.n_casa = n_casa

    def build(lista_tuplas_database):
        lista_ret = []
        for x in lista_tuplas_database:
            lista_ret.append(musico(x[0],x[1],x[2],x[3]))
        return lista_ret

class endereco:
    def __init__(self,casa,telefone):
        self.casa = casa
        self.telefone = telefone

    def build(lista_tuplas_database):
        lista_ret = []
        for x in lista_tuplas_database:
            lista_ret.append(endereco(x[0],x[1]))
        return lista_ret

class banda:
    def __init__(self,codb,cod_mus,nome):
        self.codb = codb
        self.cod_mus = cod_mus
        self.nome = nome

    def build(lista_tuplas_database):
        lista_ret = []
        for x in lista_tuplas_database:
            lista_ret.append(banda(x[0],x[1],x[2]))
        return lista_ret

class produtor:
    def __init__(self,codp,cod_mus,cod_dis):
        self.cod_mus = cod_mus
        self.cod_dis = cod_dis
        self.codp = codp

    def build(lista_tuplas_database):
        lista_ret = []
        for x in lista_tuplas_database:
            lista_ret.append(produtor(x[0],x[1],x[2]))
        return lista_ret
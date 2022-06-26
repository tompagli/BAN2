#==========================
#==========================

import datetime
from mailbox import NotEmptyError

class instrumento: 
    def __init__(self,nome,cod_interno):                    ##def da classe
     self.nome = nome
     self.cod_interno = cod_interno
    def build(lista_tuplas_database):                      ##builder para transformar a tupla recebida em lista para uma lista de objetos
        lista_ret = []
        for x in lista_tuplas_database:
            lista_ret.append(instrumento(x[0],x[1]))
        return lista_ret
    def __str__(self):                                       ## str e repr para a representacao de objeto como texto
        return self.nome +" | "+ str(self.cod_interno)
    def __repr__(self):
        return self.nome +" | "+ str(self.cod_interno)

#==========================
#==========================

class tocar:
    def __init__(self,cod_int,cod_mus):                 ##def da classe
        self.cod_int = cod_int
        self.cod_mus = cod_mus
    def build(lista_tuplas_database):                   ##builder para transformar a tupla recebida em lista para uma lista de objetos
        lista_ret = []
        for x in lista_tuplas_database:
            lista_ret.append(tocar(x[0],x[1]))
        return lista_ret
    def __str__(self):                                            ## str e repr para a representacao de objeto como texto
        return str(self.cod_int) +" | "+ str(self.cod_mus)
    def __repr__(self):
        return str(self.cod_int) +" | "+ str(self.cod_mus)

#==========================
#==========================

class musica:
    def __init__(self,titulom,autor,cod_mus,cod_dis):             ##def da classe
        self.titulom = titulom
        self.autor = autor
        self.cod_mus = cod_mus
        self.cod_dis = cod_dis
    def build(lista_tuplas_database):                           ##builder para transformar a tupla recebida em lista para uma lista de objetos
        lista_ret = []
        for x in lista_tuplas_database:
            lista_ret.append(musica(x[0],x[1],x[2],x[3]))
        return lista_ret
    def __str__(self):                                          ## str e repr para a representacao de objeto como texto
        return self.titulom +" | "+ self.autor +" | "+self.cod_mus +" | "+self.cod_dis
    def __repr__(self):
        return self.titulom +" | "+ self.autor +" | "+self.cod_mus +" | "+self.cod_dis

#==========================
#==========================

class disco:
    def __init__(self,titulod,data,id,formato,cod_mus,cod_b):       ##def da classe
        self.titulod = titulod
        self.data = data
        self.id = id
        self.formato = formato
        self.cod_mus = cod_mus
        self.cod_b = cod_b
    def build(lista_tuplas_database):                               ##builder para transformar a tupla recebida em lista para uma lista de objetos
        lista_ret = []
        for x in lista_tuplas_database:
            lista_ret.append(disco(x[0],x[1],x[2],x[3],x[4],x[5]))
        return lista_ret
    def __str__(self):                                              ## str e repr para a representacao de objeto como texto
        return self.titulod +" | "+ self.data +" | "+self.id +" | "+self.formato +" | "+ self.cod_mus +" | "+ self.cod_b
    def __repr__(self):
        return self.titulod +" | "+ self.data +" | "+self.id +" | "+self.formato +" | "+ self.cod_mus +" | "+ self.cod_b

#==========================
#==========================

class musico:
    def __init__(self,nome,n_regs,num_tel,n_casa):                    ##def da classe
        self.nome = nome
        self.n_regs = n_regs
        self.num_tel = num_tel
        self.n_casa = n_casa
    def build(lista_tuplas_database):                               ##builder para transformar a tupla recebida em lista para uma lista de objetos 
        lista_ret = []
        for x in lista_tuplas_database:
            lista_ret.append(musico(x[0],x[1],x[2],x[3]))
        return lista_ret
    def __str__(self):                                              ## str e repr para a representacao de objeto como texto
        return self.nome +" | "+ self.n_regs +" | "+self.num_tel +" | "+self.n_casa
    def __repr__(self):
        return self.nome +" | "+ self.n_regs +" | "+self.num_tel +" | "+self.n_casa

#==========================
#==========================

class endereco:
    def __init__(self,casa,telefone):                               ##def da classe
        self.casa = casa
        self.telefone = telefone

    def build(lista_tuplas_database):                               ##builder para transformar a tupla recebida em lista para uma lista de objetos
        lista_ret = []
        for x in lista_tuplas_database:
            lista_ret.append(endereco(x[0],x[1]))
        return lista_ret

    def __str__(self):                                              ## str e repr para a representacao de objeto como texto
        return self.casa +" | "+ self.telefone
    def __repr__(self):
        return self.casa +" | "+ self.telefone

#==========================
#==========================

class banda:
    def __init__(self,codb,cod_mus,nome):                           ##def da classe
        self.codb = codb
        self.cod_mus = cod_mus
        self.nome = nome

    def build(lista_tuplas_database):                               ##builder para transformar a tupla recebida em lista para uma lista de objetos
        lista_ret = []
        for x in lista_tuplas_database:
            lista_ret.append(banda(x[0],x[1],x[2]))
        return lista_ret
    
    def __str__(self):                                                  ## str e repr para a representacao de objeto como texto
        return self.codb +" | "+ self.cod_mus +" | "+self.nome
    def __repr__(self):
        return self.codb +" | "+ self.cod_mus +" | "+self.nome

#==========================
#==========================

class produtor:                                                                ##def da classe
    def __init__(self,codp,cod_mus,cod_dis):
        self.cod_mus = cod_mus
        self.cod_dis = cod_dis
        self.codp = codp

    def build(lista_tuplas_database):                              ##builder para transformar a tupla recebida em lista para uma lista de objetos
        lista_ret = []
        for x in lista_tuplas_database:
            lista_ret.append(produtor(x[0],x[1],x[2]))
        return lista_ret
    def __str__(self):
        return self.cod_mus +" | "+ self.cod_dis +" | "+self.codp  ## str e repr para a representacao de objeto como texto
    def __repr__(self):
        return self.cod_mus +" | "+ self.cod_dis +" | "+self.codp
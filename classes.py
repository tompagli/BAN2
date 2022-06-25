
import datetime
from mailbox import NotEmptyError

class instrumento: 
    def __init__(self,nome,cod_interno):
     self.nome = nome
     self.cod_interno = cod_interno

class tocar:
    def __init__(self,cod_int,cod_mus):
        self.cod_int = cod_int
        self.cod_mus = cod_mus

class musica:
    def __init__(self,titulom,autor,cod_mus,cod_dis):
        self.titulom = titulom
        self.autor = autor
        self.cod_mus = cod_mus
        self.cod_dis = cod_dis

class disco:
    def __init__(self,titulod,data,id,formato,cod_mus,cod_b):
        self.titulod = titulod
        self.data = data
        self.id = id
        self.formato = formato
        self.cod_mus = cod_mus
        self.cod_b = cod_b


class musico:
    def __init__(self,nome,n_regs,num_tel,n_casa):
        self.nome = nome
        self.n_regs = n_regs
        self.num_tel = num_tel
        self.n_casa = n_casa


class endereco:
    def __init__(self,casa,telefone):
        self.casa = casa
        self.telefone = telefone


class banda:
    def __init__(self,codb,cod_mus,nome):
        self.codb = codb
        self.cod_mus = cod_mus
        self.nome = nome

class produtor:
    def __init__(self,codp,cod_mus,cod_dis):
        self.cod_mus = cod_mus
        self.cod_dis = cod_dis
        self.codp = codp
        
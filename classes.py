
import datetime
from mailbox import NotEmptyError

class instrumento: 
    def __init__(self,nome,cod_interno):
     self.nome = nome
     self.cod_interno = cod_interno
     def __str__(self): return self.nome
lista_instrumento = []

class tocar:
    def __init__(self,cod_int,cod_mus):
        self.cod_int = cod_int
        self.cod_mus = cod_mus
lista_tocar = []

class musica:
    def __init__(self,titulom,autor,cod_mus,cod_dis):
        self.titulom = titulom
        self.autor = autor
        self.cod_mus = cod_mus
        self.cod_dis = cod_dis
lista_musica = []

class disco:
    def __init__(self,titulod,data,id,formato,cod_mus,cod_b):
        self.titulod = titulod
        self.data = data
        self.id = id
        self.formato = formato
        self.cod_mus = cod_mus
        self.cod_b = cod_b
lista_disco = []

class musico:
    def __init__(self,nome,n_regs,num_tel,n_casa):
        self.nome = nome
        self.n_regs = n_regs
        self.num_tel = num_tel
        self.n_casa = n_casa
lista_musico = []

class endereco:
    def __init__(self,casa,telefone):
        self.casa = casa
        self.telefone = telefone
lista_endereco = []

class banda:
    def __init__(self,codb,cod_mus,nome):
        self.codb = codb
        self.cod_mus = cod_mus
        self.nome = nome
lista_banda = []

class produtor:
    def __init__(self,codp,cod_mus,cod_dis):
        self.cod_mus = cod_mus
        self.cod_dis = cod_dis
        self.codp = codp
lista_produtor = []
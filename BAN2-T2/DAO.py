from numpy import vdot
import pymongo
from functions import *

class discoDAO:
    def __init__(self,titulod,data,id,formato,cod_mus,cod_b):       ##def da classe
        self.titulod = titulod
        self.data = data
        self.id = id
        self.formato = formato
        self.cod_mus = cod_mus
        self.cod_b = cod_b

    def viewDisco():
        vd = view('Disco')
        return vd
    
    def viewDiscotitulod():
        vdt = deepview('Disco','titulod')
        return vdt
    
    def viewDiscodata():
        vdt = deepview('Disco','data')
        return vdt

    def viewDiscoformato():
        vdt = deepview('Disco','formato')
        return vdt
    
    def viewDiscocodmus():
        vdt = deepview('Disco','cod_mus')
        return vdt

    def viewDiscocodb():
        vdt = deepview('Disco','cod_b')
        return vdt

class musicoDAO:
    def __init__(self,nome,n_regs,telefone,casa,n_banda,cod_play):                    ##def da classe
        self.nome = nome
        self.n_regs = n_regs
        self.telefone = telefone
        self.casa = casa
        self.n_banda = n_banda
        self.cod_play = cod_play

    def viewMusico():
        vd = view('musico')
        return vd
    
    def viewMusiconome():
        vdt = deepview('musico','nome')
        return vdt
    
    def viewMusiconregs():
        vdt = deepview('musico','n_regs')
        return vdt

    def viewMusicotelefone():
        vdt = deepview('musico','telefone')
        return vdt
    
    def viewMusicocasa():
        vdt = deepview('musico','casa')
        return vdt

    def viewMusiconbanda():
        vdt = deepview('musico','n_banda')
        return vdt
    
    def viewMusicocodplay():
        vdt = deepview('musico','cod_play')
        return vdt

class musicaDAO:
    def __init__(self,titulom,autor,cod_mus,cod_dis):             ##def da classe
        self.titulom = titulom
        self.autor = autor
        self.cod_mus = cod_mus
        self.cod_dis = cod_dis

    def viewMusica():
        vd = view('musica')
        return vd
    
    def viewMusicatitulo():
        vdt = deepview('musica','titulom')
        return vdt

    def viewMusicaautor():
        vdt = deepview('musica','autor')
        return vdt

    def viewMusicacodmus():
        vdt = deepview('musica','cod_mus')
        return vdt
    
    def viewMusicacoddis():
        vdt = deepview('musica','cod)dis')
        return vdt

class instrumento: 
    def __init__(self,nome,cod_interno,cod_play):                    
     self.nome = nome
     self.cod_interno = cod_interno
     self.cod_play = cod_play

    def viewInstrumento():
        vd = view('instrumento')
        return vd

    def viewInstrumentonome():
        vdt = deepview('instrumento','nome')
        return vdt

    def viewInstrumentocodint():
        vdt = deepview('instrumento','cod_interno')
        return vdt
    
    def viewInstrumentocodplay():
        vdt = deepview('instrumento','cod_play')
        return vdt
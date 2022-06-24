
import datetime
from mailbox import NotEmptyError

class disco:
    def __init__(self,titulod,data,id,formato):
        self.titulod = titulod
        self.data = data
        self.id = id
        self.formato = formato


class musico:
    def __init__(self,nome,n_regs,num_tel):
        self.nome = nome
        self.n_regs = n_regs
        self.num_tel = num_tel

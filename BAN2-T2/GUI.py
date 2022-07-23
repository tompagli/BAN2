import tkinter as tk
import tkinter.ttk as ttk


##Menu visualizacao
class MenuView:
    def __init__(self, master=None):
        # build ui
        self.MenuView = tk.Tk() if master is None else tk.Toplevel(master)
        self.MenuView.title("Menu de Consulta Simples")
        self.SimpleView = ttk.Button(self.MenuView)
        self.SimpleView.configure(text="Consulta Simples")
        self.SimpleView.place(anchor="nw", x=400, y=100)
        self.tuplaCombo = ttk.Combobox(self.MenuView)
        self.tuplaCombo.configure(
            exportselection="false",
            justify="center",
            takefocus=False,
            values=('Instrumento','Musico','Musica','Disco'),
        )
        self.tuplaCombo.place(anchor="nw", x=230, y=100)
        self.textoconsultasimples = tk.Text(self.MenuView)
        self.textoconsultasimples.configure(
            autoseparators="false", cursor="arrow", font="TkDefaultFont", height=2
        )
        self.textoconsultasimples.configure(relief="flat", setgrid="false", width=30)
        _text_ = "Seleciona qual tupla e clique na      consulta "
        self.textoconsultasimples.insert("0.0", _text_)
        self.textoconsultasimples.place(anchor="nw", x=210, y=10)
        self.MenuView.configure(height=400, relief="flat", width=600)
        self.MenuView.pack_propagate(0)
        self.retornamainMenu = ttk.Button(self.MenuView)
        self.retornamainMenu.configure(text="Voltar")
        self.retornamainMenu.configure(command=self.quit)
        self.retornamainMenu.place(anchor="nw", x=200, y=300)
        self.ConsultaAvan = ttk.Button(self.MenuView)
        self.ConsultaAvan.configure(text="Consulta Avancada")
        self.ConsultaAvan.configure(command=open_deepview)
        self.ConsultaAvan.place(anchor="nw", x=300, y=300)

        # Main widget
        self.mainwindow = self.MenuView
        
    def run(self):
        self.mainwindow.mainloop()
    def quit(self):
     self.mainwindow.destroy()


import tkinter as tk
import tkinter.ttk as ttk
##menu visualizacao avancada
class MenuViewAvan:
    def __init__(self, master=None) :
        self.MenuViewAvan = tk.Tk() if master is None else tk.Toplevel(master)
        self.MenuViewAvan.title("Menu de Consulta Avancada")
        self.textoConsultaAvan = tk.Text(self.MenuViewAvan)
        self.textoConsultaAvan.configure(
            autoseparators="false", height=2, insertunfocussed="none", width=30
        )
        _text_ = "Selecione a tupla e o campo   que quer consultar"
        self.textoConsultaAvan.insert("0.0", _text_)
        self.textoConsultaAvan.place(anchor="nw", x=200, y=20)
        self.Tupla = ttk.Label(self.MenuViewAvan)
        self.Tupla.configure(text="Tupla")
        self.Tupla.place(anchor="nw", x=300, y=70)
        self.listaTupla = ttk.Combobox(self.MenuViewAvan)
        self.listaTupla.configure(
            exportselection="false",
            justify="center",
            takefocus=False,
            values=('Instrumento','Musico','Musica','Disco'),
        )
        self.listaTupla.place(anchor="nw", x=250, y=90)
        self.Campo = ttk.Label(self.MenuViewAvan)
        self.Campo.configure(text="Campo")
        self.Campo.place(anchor="nw", x=295, y=120)
        self.listaCampo = ttk.Combobox(self.MenuViewAvan)
        self.listaCampo.configure(
            exportselection="false",
            justify="center",
            takefocus=False,
            values=('titulod','data','formato','cod_mus','cod_b','nome','n_regs','cod_interno','telefone','casa','n_banda','cod_play','titulom','autor','cod_dis'),
        )
        self.listaCampo.place(anchor="nw", x=250, y=140)
        self.getAvan = ttk.Button(self.MenuViewAvan)
        self.getAvan.configure(text="Consulta Avancada")
        self.getAvan.place(anchor="nw", x=300, y=180)
        self.retornamainMenu = ttk.Button(self.MenuViewAvan)
        self.retornamainMenu.configure(text="Voltar")
        self.retornamainMenu.configure(command=self.quit)
        self.retornamainMenu.place(anchor="nw", x=255, y=300)
        self.MenuViewAvan.configure(cursor="arrow", height=400, width=600)
        self.MenuViewAvan.pack_propagate(0)
        self.resultConsulta = ttk.Label(self.MenuViewAvan)
        self.resultConsulta.configure(text="resultado")
        self.resultConsulta.place(anchor="nw", x=295, y=230)
        self.mainwindow = self.MenuViewAvan
    def run(self):
        self.mainwindow.mainloop()
    def quit(self):
     self.mainwindow.destroy()

class menuInsere:
    def __init__(self, master=None):
        # build ui
        self.menuInsere = tk.Tk() if master is None else tk.Toplevel(master)
        self.menuInsere.title("Menu de insercao")
        self.textoinsereoq = tk.Text(self.menuInsere)
        self.textoinsereoq.configure(autoseparators="false", height=1, width=30)
        _text_ = "Escolha em qual tupla inserir"
        self.textoinsereoq.insert("0.0", _text_)
        self.textoinsereoq.place(anchor="nw", x=200, y=40)
        self.botaoMenuInstrumento = ttk.Button(self.menuInsere)
        self.botaoMenuInstrumento.configure(text="Instrumento")
        self.botaoMenuInstrumento.configure(command=open_instrumento)
        self.botaoMenuInstrumento.place(anchor="nw", x=295, y=80)
        self.botaoMenuMusico = ttk.Button(self.menuInsere)
        self.botaoMenuMusico.configure(text="Musico")
        self.botaoMenuMusico.configure(command=open_musico)
        self.botaoMenuMusico.place(anchor="nw", x=300, y=120)
        self.botaoMenuMusica = ttk.Button(self.menuInsere)
        self.botaoMenuMusica.configure(text="Musica")
        self.botaoMenuMusica.configure(command=open_musica)
        self.botaoMenuMusica.place(anchor="nw", x=300, y=160)
        self.botaoMenuDisco = ttk.Button(self.menuInsere)
        self.botaoMenuDisco.configure(text="Disco")
        self.botaoMenuDisco.configure(command=open_disco)
        self.botaoMenuDisco.place(anchor="nw", x=300, y=200)
        self.retornamainMenu = ttk.Button(self.menuInsere)
        self.retornamainMenu.configure(text="Voltar")
        self.retornamainMenu.configure(command=self.quit)
        self.retornamainMenu.place(anchor="nw", x=300, y=300)
        self.menuInsere.configure(height=400, width=600)
        self.menuInsere.pack_propagate(0)

        # Main widget
        self.mainwindow = self.menuInsere

    def run(self):
        self.mainwindow.mainloop()
    def quit(self):
     self.mainwindow.destroy()


class MenuInsereDisco:
    def __init__(self, master=None):
        # build ui
        self.MenuInsereDisco = tk.Tk() if master is None else tk.Toplevel(master)
        self.MenuInsereDisco.title("Menu de insercao em disco")
        self.TextoInsere = tk.Text(self.MenuInsereDisco)
        self.TextoInsere.configure(height=3, width=40)
        _text_ = "Insira os dados que vc pretende incluir no banco de dados a partir da tupla"
        self.TextoInsere.insert("0.0", _text_)
        self.TextoInsere.place(anchor="nw", x=150, y=20)
        self.labelDisco = ttk.Label(self.MenuInsereDisco)
        self.labelDisco.configure(compound="top", text="Disco")
        self.labelDisco.place(anchor="nw", x=300, y=80)
        self.labelnome = ttk.Label(self.MenuInsereDisco)
        self.labelnome.configure(text="titulod")
        self.labelnome.place(anchor="nw", x=295, y=100)
        self.entrytitulodisco = ttk.Entry(self.MenuInsereDisco)
        self.entrytitulodisco.place(anchor="nw", x=255, y=120)
        self.labeldata = ttk.Label(self.MenuInsereDisco)
        self.labeldata.configure(text="data")
        self.labeldata.place(anchor="nw", x=300, y=140)
        self.entrydatadisco = ttk.Entry(self.MenuInsereDisco)
        self.entrydatadisco.place(anchor="nw", x=255, y=160)
        self.labelid = ttk.Label(self.MenuInsereDisco)
        self.labelid.configure(text="id")
        self.labelid.place(anchor="nw", x=310, y=180)
        self.entryiddisco = ttk.Entry(self.MenuInsereDisco)
        self.entryiddisco.place(anchor="nw", x=255, y=200)
        self.retornamainMenu = ttk.Button(self.MenuInsereDisco)
        self.retornamainMenu.configure(text="Voltar")
        self.retornamainMenu.configure(command=self.quit)
        self.retornamainMenu.place(anchor="nw", x=350, y=350)
        self.botaoInsereDisco = ttk.Button(self.MenuInsereDisco)
        self.botaoInsereDisco.configure(text="Insere")
        self.botaoInsereDisco.place(anchor="nw", x=200, y=350)
        self.labelformato = ttk.Label(self.MenuInsereDisco)
        self.labelformato.configure(text="formato")
        self.labelformato.place(anchor="nw", x=295, y=220)
        self.entryformatodisco = ttk.Entry(self.MenuInsereDisco)
        self.entryformatodisco.place(anchor="nw", x=255, y=240)
        self.labelcodmus = ttk.Label(self.MenuInsereDisco)
        self.labelcodmus.configure(text="cod_mus")
        self.labelcodmus.place(anchor="nw", x=295, y=260)
        self.entrycodmusdisco = ttk.Entry(self.MenuInsereDisco)
        self.entrycodmusdisco.place(anchor="nw", x=255, y=280)
        self.labelcodb = ttk.Label(self.MenuInsereDisco)
        self.labelcodb.configure(text="cod_b")
        self.labelcodb.place(anchor="nw", x=295, y=300)
        self.entrycodbdisco = ttk.Entry(self.MenuInsereDisco)
        self.entrycodbdisco.place(anchor="nw", x=255, y=320)
        self.MenuInsereDisco.configure(
            cursor="arrow", height=400, takefocus=False, width=600
        )
        self.MenuInsereDisco.pack_propagate(0)

        # Main widget
        self.mainwindow = self.MenuInsereDisco

    def run(self):
        self.mainwindow.mainloop()
    def quit(self):
     self.mainwindow.destroy()


##menu insercao instrumento

class MenuInsereInstrumento:
    def __init__(self, master=None):
        # build ui
        self.MenuInsereInstrumento = tk.Tk() if master is None else tk.Toplevel(master)
        self.MenuInsereInstrumento.title("Menu de Insercao de Instrumento")
        self.TextoInsere = tk.Text(self.MenuInsereInstrumento)
        self.TextoInsere.configure(height=3, width=40)
        _text_ = "Insira os dados que vc pretende incluir no banco de dados a partir da tupla"
        self.TextoInsere.insert("0.0", _text_)
        self.TextoInsere.place(anchor="nw", x=150, y=20)
        self.labelinstrumento = ttk.Label(self.MenuInsereInstrumento)
        self.labelinstrumento.configure(text="Instrumento")
        self.labelinstrumento.place(anchor="nw", x=280, y=90)
        self.labelnome = ttk.Label(self.MenuInsereInstrumento)
        self.labelnome.configure(text="nome")
        self.labelnome.place(anchor="nw", x=300, y=110)
        self.entrynomeinstrumento = ttk.Entry(self.MenuInsereInstrumento)
        self.entrynomeinstrumento.place(anchor="nw", x=255, y=130)
        self.labelcodint = ttk.Label(self.MenuInsereInstrumento)
        self.labelcodint.configure(text="codint")
        self.labelcodint.place(anchor="nw", x=300, y=155)
        self.entrycodintinstrumento = ttk.Entry(self.MenuInsereInstrumento)
        self.entrycodintinstrumento.place(anchor="nw", x=255, y=175)
        self.labelcodplay = ttk.Label(self.MenuInsereInstrumento)
        self.labelcodplay.configure(text="codplay")
        self.labelcodplay.place(anchor="nw", x=300, y=200)
        self.entrycodplayinstrumento = ttk.Entry(self.MenuInsereInstrumento)
        self.entrycodplayinstrumento.place(anchor="nw", x=255, y=220)
        self.retornamainMenu = ttk.Button(self.MenuInsereInstrumento)
        self.retornamainMenu.configure(text="Voltar")
        self.retornamainMenu.configure(command=self.quit)
        self.retornamainMenu.place(anchor="nw", x=350, y=250)
        self.botaoInsereInstrumento = ttk.Button(self.MenuInsereInstrumento)
        self.botaoInsereInstrumento.configure(text="Insere")
        self.botaoInsereInstrumento.place(anchor="nw", x=200, y=250)
        self.MenuInsereInstrumento.configure(
            cursor="arrow", height=400, takefocus=False, width=600
        )
        self.MenuInsereInstrumento.pack_propagate(0)

         
        self.mainwindow = self.MenuInsereInstrumento

    def run(self):
        self.mainwindow.mainloop()
    def quit(self):
     self.mainwindow.destroy()


class MenuInsereMusico:
    def __init__(self, master=None):
        # build ui
        self.MenuInsereMusico = tk.Tk() if master is None else tk.Toplevel(master)
        self.MenuInsereMusico.title("Menu de insercao em musico")
        self.TextoInsere = tk.Text(self.MenuInsereMusico)
        self.TextoInsere.configure(height=3, width=40)
        _text_ = "Insira os dados que vc pretende incluir no banco de dados a partir da tupla"
        self.TextoInsere.insert("0.0", _text_)
        self.TextoInsere.place(anchor="nw", x=150, y=20)
        self.labelMusico = ttk.Label(self.MenuInsereMusico)
        self.labelMusico.configure(compound="top", text="Musico")
        self.labelMusico.place(anchor="nw", x=300, y=80)
        self.labelnome = ttk.Label(self.MenuInsereMusico)
        self.labelnome.configure(text="nome")
        self.labelnome.place(anchor="nw", x=295, y=100)
        self.entrynomemusico = ttk.Entry(self.MenuInsereMusico)
        self.entrynomemusico.place(anchor="nw", x=255, y=120)
        self.labeln_regs = ttk.Label(self.MenuInsereMusico)
        self.labeln_regs.configure(text="n_regs")
        self.labeln_regs.place(anchor="nw", x=300, y=140)
        self.entrynregsmusico = ttk.Entry(self.MenuInsereMusico)
        self.entrynregsmusico.place(anchor="nw", x=255, y=160)
        self.labeltelefone = ttk.Label(self.MenuInsereMusico)
        self.labeltelefone.configure(text="telefone")
        self.labeltelefone.place(anchor="nw", x=290, y=180)
        self.entrytelefonemusico = ttk.Entry(self.MenuInsereMusico)
        self.entrytelefonemusico.place(anchor="nw", x=255, y=200)
        self.retornamainMenu = ttk.Button(self.MenuInsereMusico)
        self.retornamainMenu.configure(text="Voltar")
        self.retornamainMenu.configure(command=self.quit)
        self.retornamainMenu.place(anchor="nw", x=350, y=350)
        self.botaoInsereMusico = ttk.Button(self.MenuInsereMusico)
        self.botaoInsereMusico.configure(text="Insere")
        self.botaoInsereMusico.place(anchor="nw", x=200, y=350)
        self.labelcasa = ttk.Label(self.MenuInsereMusico)
        self.labelcasa.configure(text="casa")
        self.labelcasa.place(anchor="nw", x=295, y=220)
        self.entrycasamusico = ttk.Entry(self.MenuInsereMusico)
        self.entrycasamusico.place(anchor="nw", x=255, y=240)
        self.labelnbanda = ttk.Label(self.MenuInsereMusico)
        self.labelnbanda.configure(text="n_banda")
        self.labelnbanda.place(anchor="nw", x=295, y=260)
        self.entrynbandamusico = ttk.Entry(self.MenuInsereMusico)
        self.entrynbandamusico.place(anchor="nw", x=255, y=280)
        self.labelcodplay = ttk.Label(self.MenuInsereMusico)
        self.labelcodplay.configure(text="cod_play")
        self.labelcodplay.place(anchor="nw", x=295, y=300)
        self.entrycodplaymusico = ttk.Entry(self.MenuInsereMusico)
        self.entrycodplaymusico.place(anchor="nw", x=255, y=320)
        self.MenuInsereMusico.configure(
            cursor="arrow", height=400, takefocus=False, width=600
        )
        self.MenuInsereMusico.pack_propagate(0)

        # Main widget
        self.mainwindow = self.MenuInsereMusico

    def run(self):
        self.mainwindow.mainloop()
    def quit(self):
     self.mainwindow.destroy()

class MenuInsereMusica:
    def __init__(self, master=None):
        # build ui
        self.MenuInsereMusica = tk.Tk() if master is None else tk.Toplevel(master)
        self.MenuInsereMusica.title("Menu de insercao em musica")
        self.TextoInsere = tk.Text(self.MenuInsereMusica)
        self.TextoInsere.configure(height=3, width=40)
        _text_ = "Insira os dados que vc pretende incluir no banco de dados a partir da tupla"
        self.TextoInsere.insert("0.0", _text_)
        self.TextoInsere.place(anchor="nw", x=150, y=20)
        self.labelMusica = ttk.Label(self.MenuInsereMusica)
        self.labelMusica.configure(compound="top", text="Musica")
        self.labelMusica.place(anchor="nw", x=300, y=80)
        self.labeltitulomusica = ttk.Label(self.MenuInsereMusica)
        self.labeltitulomusica.configure(text="titulo")
        self.labeltitulomusica.place(anchor="nw", x=295, y=100)
        self.entrytitulomusica = ttk.Entry(self.MenuInsereMusica)
        self.entrytitulomusica.place(anchor="nw", x=255, y=120)
        self.labelautormusica = ttk.Label(self.MenuInsereMusica)
        self.labelautormusica.configure(text="autor")
        self.labelautormusica.place(anchor="nw", x=300, y=140)
        self.entryautormusica = ttk.Entry(self.MenuInsereMusica)
        self.entryautormusica.place(anchor="nw", x=255, y=160)
        self.labelcodmusmusica = ttk.Label(self.MenuInsereMusica)
        self.labelcodmusmusica.configure(text="cod_mus")
        self.labelcodmusmusica.place(anchor="nw", x=290, y=180)
        self.entrycodmusmusica = ttk.Entry(self.MenuInsereMusica)
        self.entrycodmusmusica.place(anchor="nw", x=255, y=200)
        self.retornamainMenu = ttk.Button(self.MenuInsereMusica)
        self.retornamainMenu.configure(text="Voltar")
        self.retornamainMenu.configure(command=self.quit)
        self.retornamainMenu.place(anchor="nw", x=350, y=350)
        self.botaoInsereMusica = ttk.Button(self.MenuInsereMusica)
        self.botaoInsereMusica.configure(text="Insere")
        self.botaoInsereMusica.place(anchor="nw", x=200, y=350)
        self.labelcod_dis = ttk.Label(self.MenuInsereMusica)
        self.labelcod_dis.configure(text="cod_dis")
        self.labelcod_dis.place(anchor="nw", x=295, y=220)
        self.entrycoddismusica = ttk.Entry(self.MenuInsereMusica)
        self.entrycoddismusica.place(anchor="nw", x=255, y=240)
        self.MenuInsereMusica.configure(
            cursor="arrow", height=400, takefocus=False, width=600
        )
        self.MenuInsereMusica.pack_propagate(0)

        # Main widget
        self.mainwindow = self.MenuInsereMusica

    def run(self):
        self.mainwindow.mainloop()
    def quit(self):
     self.mainwindow.destroy()

def open_view():
     app = MenuView() ##chamada da janela de insercao
     app.run()

def open_deepview():
    app = MenuViewAvan()
    app.run()

def open_insert():
    app = menuInsere()
    app.run()

def open_disco():
    app = MenuInsereDisco()
    app.run()

def open_musico():
    app = MenuInsereMusico()
    app.run()

def open_musica():
    app = MenuInsereMusica()
    app.run()

def open_instrumento():
    app = MenuInsereInstrumento()
    app.run()

class MainMenu:
    def __init__(self, master=None):
        # build ui
        self.mainMenu = tk.Tk() if master is None else tk.Toplevel(master)
        self.mainMenu.title("Menu Inicial")
        self.botaoInsert = ttk.Button(self.mainMenu)
        self.botaoInsert.configure(text="Inserção")
        self.botaoInsert.configure(command=open_insert)
        self.botaoInsert.place(anchor="nw", height=50, width=100, x=150, y=300)
        self.Consulta = ttk.Button(self.mainMenu)
        self.Consulta.configure(text="Consulta")
        self.Consulta.configure(command=open_view)
        self.Consulta.place(anchor="nw", height=50, width=100, x=350, y=300)
        self.welcome = tk.Text(self.mainMenu)
        self.welcome.configure(
            cursor="arrow", font="TkDefaultFont", height=3, insertunfocussed="none"
        )
        self.welcome.configure(
            relief="flat", setgrid="false", takefocus=False, width=50
       )
        _text_ = "Bem vindo ao menu inicial da aplicação de manuseio     em MongoDB!"
        self.welcome.insert("0.0", _text_)
        self.welcome.place(anchor="nw", x=150, y=20)
        self.mainMenu.configure(height=400, width=600)
        self.mainMenu.pack_propagate(0)

       # Main widget
        self.mainwindow = self.mainMenu

    def run(self):
       self.mainwindow.mainloop()


if __name__ == "__main__":
    app = MainMenu()
    app.run() ##

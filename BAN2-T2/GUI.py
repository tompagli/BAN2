## import tkinter as tk
## import tkinter.ttk as ttk


## class MainMenu:
##     def __init__(self, master=None):
        # build ui
##         self.mainMenu = tk.Tk() if master is None else tk.Toplevel(master)
##         self.mainMenu.title("Menu Inicial")
##         self.botaoInsert = ttk.Button(self.mainMenu)
##         self.botaoInsert.configure(text="Inserção")
##         self.botaoInsert.place(anchor="nw", height=50, width=100, x=150, y=300)
##         self.Consulta = ttk.Button(self.mainMenu)
##         self.Consulta.configure(text="Consulta")
##         self.Consulta.place(anchor="nw", height=50, width=100, x=350, y=300)
##         self.welcome = tk.Text(self.mainMenu)
##         self.welcome.configure(
##             cursor="arrow", font="TkDefaultFont", height=3, insertunfocussed="none"
##         )
##         self.welcome.configure(
##             relief="flat", setgrid="false", takefocus=False, width=50
##        )
##         _text_ = "Bem vindo ao menu inicial da aplicação de manuseio     em MongoDB!"
##         self.welcome.insert("0.0", _text_)
##         self.welcome.place(anchor="nw", x=150, y=20)
##         self.mainMenu.configure(height=400, width=600)
##         self.mainMenu.pack_propagate(0)
## 
##        # Main widget
##         self.mainwindow = self.mainMenu

##     def run(self):
##        self.mainwindow.mainloop()
## 
## 
## if __name__ == "__main__":
##     app = MainMenu()
##     app.run() ##

import tkinter as tk
import tkinter.ttk as ttk

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
        self.retornamainMenu.place(anchor="nw", x=255, y=300)
        self.MenuViewAvan.configure(cursor="arrow", height=400, width=600)
        self.MenuViewAvan.pack_propagate(0)
        self.resultConsulta = ttk.Label(self.MenuViewAvan)
        self.resultConsulta.configure(text="resultado")
        self.resultConsulta.place(anchor="nw", x=295, y=230)
        self.mainwindow = self.MenuViewAvan
    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = MenuViewAvan()
    app.run()



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
        self.retornamainMenu.place(anchor="nw", x=200, y=300)
        self.ConsultaAvan = ttk.Button(self.MenuView)
        self.ConsultaAvan.configure(text="Consulta Avancada")
        self.ConsultaAvan.place(anchor="nw", x=300, y=300)

        # Main widget
        self.mainwindow = self.MenuView

    def run(self):
        self.mainwindow.mainloop()




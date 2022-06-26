
import tkinter as tk
import tkinter.ttk as ttk

from functions import insert, separa_por_parametro


def open_insert():
     app = InsertDados()
     app.run()

def open_consulta():
    app = Menu_Select()
    app.run()

def volta_menu():
    app.quit(InsertDados)

class Menu_Select:
    def __init__(self, master=None):
        # build ui
        self.Menu_Select = tk.Tk() if master is None else tk.Toplevel(master)
        self.Menu_Select.title("Consultas Avancadas")
        self.frame1 = ttk.Frame(self.Menu_Select)
        self.text1 = tk.Text(self.frame1)
        self.text1.configure(height=2, width=50)
        _text_ = "Bem vindo ao menu de consultas avançadas, escolha:"
        self.text1.insert("0.0", _text_)
        self.text1.place(anchor="nw", x=40, y=20)
        self.select_table = ttk.Entry(self.frame1)
        self.select_table.place(anchor="nw", x=40, y=200)
        self.tabela = ttk.Label(self.frame1)
        self.tabela.configure(text="Tabela")
        self.tabela.place(anchor="nw", x=80, y=180)
        self.select_campo = ttk.Entry(self.frame1)
        self.select_campo.place(anchor="nw", x=170, y=200)
        self.campo = ttk.Label(self.frame1)
        self.campo.configure(text="Campo")
        self.campo.place(anchor="nw", x=210, y=180)
        self.select_value = ttk.Entry(self.frame1)
        self.select_value.place(anchor="nw", x=299, y=200)
        self.label3 = ttk.Label(self.frame1)
        self.label3.configure(text="Valor")
        self.label3.place(anchor="nw", x=340, y=180)
        self.botao_con_avan = ttk.Button(self.frame1)
        self.botao_con_avan.configure(text="Consulte!",command=self.get_table)
        self.botao_con_avan.place(anchor="nw", x=300, y=250)
        self.frame1.configure(height=480, width=320)
        self.frame1.pack(fill="both", side="top")
        self.frame1.pack_propagate(0)
        self.Menu_Select.configure(height=200, width=200)
        self.Menu_Select.geometry("480x320")

        # Main widget
        self.mainwindow = self.Menu_Select
    
    def get_table(self):
     tables = self.select_table.get()
     campos = self.select_campo.get()
     values = self.select_value.get() 
     consulta_lista = separa_por_parametro(tables,campos,values)
     varwhat = RetornoConsulta(consulta_lista).run()
    def run(self):
        self.mainwindow.mainloop()


## if __name__ == "__main__":
##    app = Menu_Select()
##    app.run()


class InsertDados:
    def __init__(self, master=None):
        # build ui
        self.toplevel2 = tk.Tk() if master is None else tk.Toplevel(master)
        self.toplevel2.title('Insercao nas tabelas')
        self.frame2 = ttk.Frame(self.toplevel2)
        self.label4 = ttk.Label(self.frame2)
        self.label4.configure(text="Inserção: Selecione qual tabela você quer inserir")
        self.label4.place(anchor="nw", x=100, y=50)
        self.table_entry = ttk.Entry(self.frame2)
        self.table_entry.configure(cursor="arrow")
        self.table_entry.place(anchor="nw", x=170, y=75)
        self.label5 = ttk.Label(self.frame2)
        self.label5.configure(
            cursor="arrow", text="Insira os valores a serem adicionados na tabela"
        )
        self.label5.place(anchor="nw", x=100, y=100)
        self.entry_values = ttk.Entry(self.frame2)
        self.entry_values.place(anchor="nw", x=170, y=125)
        self.label6 = ttk.Label(self.frame2)
        self.label6.configure(text="Nao esqueca de separar os valores com virgula")
        self.label6.place(anchor="nw", x=100, y=150)
        self.buttonInsertConfirm = ttk.Button(self.frame2)
        self.buttonInsertConfirm.configure(text="Confirmar",command=self.get_insert)
        self.buttonInsertConfirm.place(anchor="nw", x=300, y=180)
        self.label7 = ttk.Label(self.frame2)
        self.label7.configure(text="Se quiser voltar ao menu inicial")
        self.label7.place(anchor="nw", x=150, y=220)
        self.buttonVoltar = ttk.Button(self.frame2)
        self.buttonVoltar.configure(text="Voltar",command=self.quit)
        self.buttonVoltar.place(anchor="nw", x=300, y=250)
        self.frame2.configure(height=200, width=200)
        self.frame2.pack(expand="true", fill="both", side="top")
        self.toplevel2.configure(height=480, takefocus=False, width=320)
        self.toplevel2.geometry("480x320")
        # Main widget
        self.mainwindow = self.toplevel2
    def get_insert(self):
     tabela = self.table_entry.get()
     valores = self.entry_values.get()
     insert(tabela,valores)
    
    def quit(self):
     self.mainwindow.destroy()

    def run(self):
        self.mainwindow.mainloop()
    
class RetornoConsulta:
    def __init__(self,parametro, master=None):
        # build ui
        self.parametro = parametro
        self.RetornoConsulta = tk.Tk() if master is None else tk.Toplevel(master)
        self.RetornoConsulta.title("Retorno da Consulta")
        self.frameResultadoCons = ttk.Frame(self.RetornoConsulta)
        self.resultadoConsultaLabel = ttk.Label(self.frameResultadoCons)
        self.resultadoConsultaLabel.configure(text="Resultado da consulta")
        self.resultadoConsultaLabel.place(anchor="nw", x=190, y=90)
        #==========================

        x_a=190
        y_a=120
        for x in self.parametro:
            self.resultadoConsultaessabuxa = ttk.Label(self.frameResultadoCons)
            self.resultadoConsultaessabuxa.configure(text=x)
            self.resultadoConsultaessabuxa.place(anchor="nw", x=x_a,y=y_a)
            y_a+=30
        
        #============================

        ##self.resultadoConsultaessabuxa = ttk.Label(self.frameResultadoCons)
        ###self.resultadoConsultaessabuxa.configure(text=self.parametro)
        ###self.resultadoConsultaessabuxa.place(anchor="nw", x=190, y=120)
        self.button4 = ttk.Button(self.frameResultadoCons)
        self.button4.configure(text="Voltar",command=self.quit)
        self.button4.place(anchor="nw", x=300, y=220)
        self.frameResultadoCons.configure(height=200, width=200)
        self.frameResultadoCons.pack(expand="true", fill="both", side="top")
        self.RetornoConsulta.configure(height=200, width=200)
        self.RetornoConsulta.geometry("480x320")

        # Main widget
        self.mainwindow = self.RetornoConsulta
    def quit(self):
     self.mainwindow.destroy()
    def run(self):
        self.mainwindow.mainloop()


## if __name__ == "__main__":
##    app = RetornoConsulta()
##    app.run()

##if __name__ == "__main__":
##   app = InsertDados()
##    app.run()
class MainMenu:
    def __init__(self, master=None):
        # build ui
        self.frameMenuInicial = tk.Tk()##(master, container="false")
        self.frameMenuInicial.title('My Title')
        self.frame1 = tk.Frame(self.frameMenuInicial)
        self.text2 = tk.Text(self.frame1)
        self.text2.configure(
            autoseparators="false", cursor="arrow", exportselection="true", height=4
        )
        self.text2.configure(relief="flat", state="normal", width=40)
        _text_ = "Olá usuário, bem vindo a aplicação de   manipulação de dados SQL,qual opção te  interessa?"
        self.text2.insert("0.0", _text_)
        self.text2.pack(anchor="center", expand="false", pady=20, side="top")
        self.buttonInsert = tk.Button(self.frame1)
        self.SelectInsert = tk.StringVar(value="Inserção")
        self.buttonInsert.configure(text="Inserção", textvariable=self.SelectInsert)
        self.buttonInsert.configure(command=open_insert)
        self.buttonInsert.place(anchor="nw", width=150, x=50, y=160)
        self.buttonConsulta = tk.Button(self.frame1)
        self.buttonConsulta.configure(command=open_consulta)
        self.SelectConsulta = tk.StringVar(value="Consulta")
        self.buttonConsulta.configure(
            takefocus=False, text="Consulta", textvariable=self.SelectConsulta
        )
        self.buttonConsulta.place(anchor="nw", width=150, x=250, y=160)
        self.frame1.configure(cursor="arrow", height=200, width=200)
        self.frame1.place(
            anchor="nw", height=320, relx=0.0, rely=0.0, width=480, x=0, y=0
        )
        self.frameMenuInicial.configure(height=200, relief="flat", takefocus=False, width=200)
        self.frameMenuInicial.geometry("480x320")
        self.frameMenuInicial.title("Database App")

        # Main widget
        self.mainwindow = self.frameMenuInicial

    def run(self):
       self.mainwindow.mainloop()


if __name__ == "__main__":
    app = MainMenu()
    app.run()
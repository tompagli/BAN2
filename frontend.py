
import tkinter as tk

class MainMenu:
    def __init__(self, master=None):
        # build ui
        self.toplevel1 = tk.Toplevel(master, container="false")
        self.frame1 = tk.Frame(self.toplevel1)
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
        self.buttonInsert.place(anchor="nw", width=150, x=50, y=160)
        self.buttonConsulta = tk.Button(self.frame1)
        self.SelectConsulta = tk.StringVar(value="Consulta")
        self.buttonConsulta.configure(
            takefocus=False, text="Consulta", textvariable=self.SelectConsulta
        )
        self.buttonConsulta.place(anchor="nw", width=150, x=250, y=160)
        self.frame1.configure(cursor="based_arrow_up", height=200, width=200)
        self.frame1.place(
            anchor="nw", height=320, relx=0.0, rely=0.0, width=480, x=0, y=0
        )
        self.toplevel1.configure(height=200, relief="flat", takefocus=False, width=200)
        self.toplevel1.geometry("480x320")
        self.toplevel1.title("Database App")

        # Main widget
        self.mainwindow = self.toplevel1

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    app = MainMenu()
    app.run()

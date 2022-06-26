
## Milton Pedro Pagliusi Neto 
## Banco de Dados 2

## Si vis paces, para bellum ##

from pip import main
from classes import *
import psycopg2
from functions import *
from frontend import *


conn = psycopg2.connect("dbname=gravadora user=postgres password=udesc")

if __name__ == "__main__":
    app = MainMenu()
    app.run()

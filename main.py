

from pip import main
from classes import *
import psycopg2
from functions import *
from frontend import *


conn = psycopg2.connect("dbname=gravadora user=postgres password=udesc")


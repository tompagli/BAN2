## arquivo de conexão do MongoDB com a aplicação python

def connect_db():
    from pymongo import MongoClient
    import pymongo

    CONNECTION_STRING = "mongodb://localhost:27017"

    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)
    return client['gravadora']

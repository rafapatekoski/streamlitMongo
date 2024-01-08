from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv, find_dotenv
import os
import streamlit as st
load_dotenv(find_dotenv())
password = os.environ.get("MONGODB_PWD")
uri = f"mongodb+srv://patekoski:{password}@cluster0.isfvbxi.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    st.write("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    st.write(e)

dbs = client.list_database_names()
teste_db = client.escola
collections = teste_db.list_collection_names()
aluno = collections[0]
st.write(collections)
st.write(aluno)

def insert_test_doc():
    collection = teste_db.teste
    st.write(collection)
    test_document = {
        "nome":"Rafal Patekoski",
        "idade":23,
        "profissao":"Cientista de Dados"
    }
    inserted_id = collection.insert_one(test_document).inserted_id
    st.write(inserted_id)
st.button("Inserir",on_click=insert_test_doc)
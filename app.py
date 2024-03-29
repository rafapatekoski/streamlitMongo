from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv, find_dotenv
import os
import streamlit as st
import pandas as pd
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
nome = st.text_input("Digite seu nome: ")
profissao = st.text_input("Digite sua profissão")
nascimento = st.date_input("Data de Nascimento", format="DD/MM/YYYY")
nascimento = str(nascimento)
def insert_test_doc():
    if nome is None or profissao is None or nascimento is None:
        st.error("Preencha os campos corretamente.")
    else:
        collection = teste_db.pandasteste
        st.write(collection)
        test_document = {
            "nome": nome,
            "nascimento":nascimento,
            "profissao":profissao
        }
        inserted_id = collection.insert_one(test_document).inserted_id
        st.write(inserted_id)
st.button("Inserir",on_click=insert_test_doc)
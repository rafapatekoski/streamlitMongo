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
df = pd.read_csv("listapiloto2024.csv", sep=';')
df_editado = st.data_editor(df, num_rows="dynamic")

def editar():
    collection = teste_db.pandasteste
    st.write(collection)
    dados_json = df_editado.to_dict(orient='records')
    collection.delete_many({})
    collection.insert_many(dados_json)
st.button("Editar", on_click=editar)
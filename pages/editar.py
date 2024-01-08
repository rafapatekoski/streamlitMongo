import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
import os
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from time import sleep

if "editar" not in st.session_state:
    print("...")
else:
    del st.session_state["editar"]
    switch_page("app")

load_dotenv(find_dotenv())
password = os.environ.get("MONGODB_PWD")
uri = f"mongodb+srv://patekoski:{password}@cluster0.isfvbxi.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Access the database and collection
teste_db = client.escola
pandasteste = teste_db.pandasteste

# Consulte todos os documentos na coleção
colecaopandateste = pandasteste.find()

# Transforme os documentos em um DataFrame do pandas
df = pd.DataFrame(list(colecaopandateste))

# Remova a coluna '_id' do DataFrame
df = df.drop('_id', axis=1, errors='ignore')

# Use o Streamlit para editar o DataFrame
df_editado = st.data_editor(df, num_rows="dynamic")

# Função para salvar as alterações de volta no MongoDB
def editar():
    # Obtenha os dados editados como uma lista de dicionários
    dados_json = df_editado.to_dict(orient='records')
    
    # Remova '_id' de cada documento, se presente
    for doc in dados_json:
        doc.pop('_id', None)
    
    # Delete all documents in the collection
    pandasteste.delete_many({})
    sleep(1)
    # Insert the edited documents without '_id' back into the collection
    pandasteste.insert_many(dados_json)
    sleep(1)
    st.session_state["editar"] = True

# Botão para chamar a função de edição
st.button("Editar", on_click=editar)
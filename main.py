import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")
col1,empty_col,col2 = st.columns([1.5,0.5,1.5])

with col1:
    st.image("images/photo.png",width=400)

with col2:
    st.title("Rayeh Mohammed Riad")
    content = """
    Salut , C'est Riad ! Je suis un programmeur python , chef de projet Kids learning ,chef de projet TET-GROUPE.
    Je suis diplomé d'un master en informatique spécialité ingénierie des systèmes information à sidi bel abbes.
    J'ai travaillé avec plusieurs partenaires nationnales et étranger tel que Algérie , France ,Grece dans le poste
    Développeur backend pour solution complexe comme scraptcha, dockbanking , Trading bot , WASSLA , E-bank-fr.
    
    """
    st.info(content)
    content2="""
    Ici vous pouvez consultez quelque travail que j'ai déja travailler 
    """
    st.write(content2)

    col3,col4 = st.columns(2)

    df = pd.read_csv("data.csv",sep=";")


    with col3:
        for index,row in df[:10].iterrows():
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/" + row["image"])
            st.write(f"[Source Code]({row['url']})")

    with col4:
        for index,row in df[10:].iterrows():
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/" + row["image"])
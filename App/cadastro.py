#import streamlit as st
import pandas as pd

#st.title('Aplicativo de Cadastro')
df = pd.read_csv('cadastro.scv')
print(df.head())


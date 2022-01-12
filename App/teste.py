import streamlit as st
import pandas as pd
import numpy as np

df1 = pd.DataFrame(
    columns =['Nome'])

my_table = st.table(df1)
btn = st.button('add')

if btn:
    st.text_input("Digite o Nome", key = 'nome')
    df2 = pd.DataFrame([st.session_state.nome],columns =['Nome'])
    my_table.add_rows(df2)

#my_table.add_rows(df2)

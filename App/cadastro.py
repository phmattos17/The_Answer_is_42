import streamlit as st
import pandas as pd

st.title('Aplicativo de Cadastro')
file_path_local = '/Users/Pedro/Desktop/PESSOAL/python_codes/The_Answer_is_42/App/cadastro.csv'
file_path_github = 'https://raw.githubusercontent.com/phmattos17/The_Answer_is_42/main/App/cadastro.csv'

df = pd.read_csv(file_path_local)
st.write(df)

st.sidebar.header('Options')
options_form = st.sidebar.form('options form')
nome = options_form.text_input('Digite o nome')
idade = options_form.text_input('Digite a idade')
add_data = options_form.form_submit_button()

if add_data:
    add_dict = {
        'Nome': nome,
        'Idade': idade
    }
    df = df.append(add_dict, ignore_index = True)
    df.to_csv(file_path_local, index = False)

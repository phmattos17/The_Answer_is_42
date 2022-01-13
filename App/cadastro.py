import streamlit as st
import pandas as pd
import re

st.title('Aplicativo de Cadastro')
file_path_local = '/Users/Pedro/Desktop/PESSOAL/python_codes/The_Answer_is_42/App/cadastro.csv'
file_path_github = 'https://raw.githubusercontent.com/phmattos17/The_Answer_is_42/main/App/cadastro.csv'

df = pd.read_csv(file_path_local)
#st.write(df)

st.sidebar.header('O que você deseja fazer?')
options_buttom = st.sidebar.radio('',(["Página Inicial","Fazer Cadastro", "Atualizar Cadastro",
                "Buscar Cadastro"]))

if options_buttom == "Página Inicial":
    st.write("Teste")

elif options_buttom == "Fazer Cadastro":
    st.title("Teste 2")

elif options_buttom == "Atualizar Cadastro":

#    Usuário irá procurar o cadastro pelo nome e será retornado o
#    dataframe apenas com os valores desejados.
#
#    Posteriormente poderá escolher que campo irá atualizar
#    podendo ser feito em múltiplas colunas, uma de cada vez
#    para evitar erros

    st.title("Atualização de Cadastro")
    nome_update = st.text_input("Digite o Nome:")

    padrao = re.compile(nome_update+'+')
    for nomes in df['Nome'].values:
        if padrao.search(nomes)!=None:
            cadastro_nome = padrao.search(nomes).string
            st.dataframe(df[df['Nome']==cadastro_nome])
            st.write(cadastro_nome)
            st.session_state['cadastro_nome'] = cadastro_nome
            
    option_update = st.multiselect(
    'O que você deseja atualizar?',
    ['Nome', 'Telefone', 'Idade'],
    default = ['Nome'])
    st.write(st.session_state['cadastro_nome'])
    update_start = st.button("Atualizar")
    if update_start:
        st.session_state['update_start'] = 1
        st.write(st.session_state['cadastro_nome'])
        for coluna in option_update:
            coluna_update = st.text_input("Digite o(a) "+str(coluna)+": ")
            mod_start = st.button("Modificar")
            st.session_state['mod_start'] = 1
            if mod_start:
                df.loc[df[coluna]==st.session_state['cadastro_nome'],[coluna]] = coluna_update
#    fim = st.button('Finalizado')
#    if fim:
#        df.to_csv(file_path_local, index = False)
                st.session_state['search_start'] = 0
                st.session_state['update_start'] = 0

else:
    st.title('Busca de Cadastro')
    nome_search = st.text_input("Digite o Nome:")
    search_start = st.button("Procure")

    if search_start:
        padrao = re.compile(nome_search+'+')
        for nomes in df['Nome'].values:
            if padrao.search(nomes)!=None:
                cadastro = padrao.search(nomes).string
                st.dataframe(df[df['Nome']==cadastro])
#   add_dict = {
#       'Nome': nome,
#       'Idade': idade
#   }
#   df = df.append(add_dict, ignore_index = True)
#   df.to_csv(file_path_local, index = False)

import streamlit as st
import numpy as np
import pandas as pd

st.header('Minha Dashboard')
st.text('DASHBOARD')
st.markdown('# Dashboard')
st.caption('Meus dados, tudo actualizado')
st.write('# Olá!', ['Pedro', 'Francisco'])
st.title('Dados Históricos')

df = pd.DataFrame(
     np.random.randn(10, 3),
     columns=['Preço', 'Taxa de desocupação', 'Taxa inadiplencia',])

st.table(df)

st.markdown('### Gráficos')
df = pd.DataFrame(
        np.random.randn(10, 3),
        columns=['Preço', 'Taxa de desocupação', 'Taxa inadiplencia',])
st.line_chart(df)

df = pd.DataFrame(
        np.random.randn(10, 3),
        columns=['Preço', 'Taxa de desocupação', 'Taxa inadiplencia',])
st.bar_chart(df)

if st.button('MEU BOTÃO'):
     st.write('Click')
check = st.checkbox('Aceito')


if check:
     st.write('Marcado')

     opcao = st.radio(
 "Selecione uma opção",
 ('Opção 1', 'Opção 2'))


if opcao == 'Opção 1':
    st.write('1')
else:
    st.write("2")

    option = st.selectbox(
    'Selecione',
    ('Op 1', 'Op 2', 'Op 3'))

st.write('Você selecionou:', opcao)


options = st.multiselect(
     'Cor favorita',
     ['Verde', 'Amarelo', 'Vermelho', 'Azul'],
     ['Vermelho', 'Verde'])


values = st.slider(
'Intervalo',
0.0, 100.0, (25.0, 75.0))


title = st.text_input('Nome', 'Pedro Francisco')
number = st.number_input('Número', int('244945149978'))

date = st.date_input(

 "Digite uma data", )

t = st.time_input(

 "Digite um horário", )
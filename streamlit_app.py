import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.header("Введите id пользователя:")
id = st.number_input('', max_value=278, value=0)
st.write('Текущее id:', id)

hist=pd.DataFrame({
  'id':[11,22,23],
  'title':['Построили школу', 'Открыли парк', 'Планируется открытие спорт центра'],
  'date':['10.09.2021', '12.09.2021', '13.09.2021']})

recomm=pd.DataFrame({
  'id':[110,202],
  'title':['Открыли центр развития детей', 'Открыли спортивный центр'],
  'date':['20.11.2021', '22.11.2021']})

col1, col2 = st.columns(2)

col1.header('History')
col1.write(hist)

col2.header('Recommendations')
col2.write(recomm)

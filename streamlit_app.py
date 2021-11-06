import streamlit as st
import pandas as pd

st.header("Введите id пользователя:")
id = st.number_input('', max_value=278, value=1)
st.write('The current id is ', id)

hist=pd.DataFrame({
  'id':[11,22],
  'title':['Построили школу', 'Открыли парк'],
  'date':['10.09.2021', '12.09.2021']})
st.header("History")
st.write(hist)

recomm=pd.DataFrame({
  'id':[110,202],
  'title':['Открыли центр развития детей', 'Открыли спортивный центр'],
  'date':['20.11.2021', '22.11.2021']})
st.header("Recommendations")
st.write(recomm)

col1, col2 = st.columns(2)

col1.header('Hist')
col1.write(hist)

col2.header('Rec')
col2.write(recomm)

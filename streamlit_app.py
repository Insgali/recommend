import streamlit as st
import os
import pandas as pd

id = st.number_input('Insert a user id')
st.write('The current id is ', id)

hist=pd.DataFrame({
  'id':[11,22],
  'title':['Построили школу', 'Открыли парк'],
  'date':['10.09.2021', '12.09.2021']})
st.header("History")
st.write(hist)

reccom=pd.DataFrame({
  'id':[11,22],
  'title':['Открыли центр развития детей', 'Открыли спортивный центр'],
  'date':['20.11.2021', '22.11.2021']})
st.header("History")
st.write(reccom)

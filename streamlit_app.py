import streamlit as st
import os

st.header("History")
st.header("Recommendations")

id = st.number_input('Insert a user id')
st.write('The current id is ', id)

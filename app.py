import streamlit as st
import pandas as pd

st.write('Welcome To AVD Group')
st.write('Below Fee Structure for Data Engineering')

data = {
            'Course Name': ['MySql', 'Linux', 'Hadoop', 'Python', 'DevOps', 'Azure', 'Pyspark'], 
            'Duration': ['30 days', '15 days', '20 days', '35 days', '35 days', '25 days', '20 days'],
            'Fees': ['8000', '5000', '10000', '10000', '20000', '10000', '7000']
    }
df = pd.DataFrame(data)

st.dataframe(df)
st.write('Total fees = 70000 Rupees')
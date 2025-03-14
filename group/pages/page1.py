import streamlit as st
# from PIL import Image
# import pandas as pd

column1, column2 = st.columns(2)

st.markdown('## this is the first page')
st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

# df = pd.read_excel("/Users/homuhomy/Desktop/work/Training/python/Day2/Hands-on/banking.csv")

# st.dataframe(df)

# with column1:
#     st.bar_chart(df, x="age", y="job")

# with column2:
#     st.line_chart(df, x="education", y="job")



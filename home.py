import streamlit as st
import pandas as pd
from functions import pipeline, get_coldata
import os
import tempfile
import openpyxl


st.header(":green[Excel] Formula Generator",divider="green")
api_key = st.text_input(label="apk key",placeholder="Enter you api key", type="password")
bot = pipeline(api_key=api_key)


if file := st.file_uploader(label="Upload your csv file", type=["csv"]):

    temp_file = tempfile.TemporaryFile(delete=False)
    with open(temp_file.name,"wb") as f:
        f.write(file.getvalue())

    df = pd.read_csv(temp_file.name)


    csv_file = pd.read_csv(temp_file.name)
    col_data = get_coldata(csv_file)

    if "col_data" not in st.session_state:
        st.session_state["col_data"] = col_data

    if "dataframe" not in st.session_state:
        st.session_state["dataframe"] = df

if st.button(label="submit"):
    st.switch_page("pages/chat.py")



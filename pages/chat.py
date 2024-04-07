import streamlit as st
import pandas as pd
from home import bot


dataframe = st.session_state["dataframe"]
col_data = st.session_state["col_data"]
dataf = st.dataframe(dataframe)


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        output = bot.run(data=col_data, request=prompt)
        response = st.write_stream(output)
    st.session_state.messages.append({"role": "assistant", "content": response})


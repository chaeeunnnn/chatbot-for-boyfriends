from openai import OpenAI
import streamlit as st

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/chaeeunnnn/chatbot-for-boyfriends/tree/main)"
    

st.title("❤️‍🔥 Chatbot, but romantic ")
st.caption("💬 A chatbot for boyfriends who are struggling with their girls' hypothetical & silly question attacks, powered by OpenAI LLM")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system" , "content": "You are a romantic conversation helper. You assist guys generate a stupidly romantic answer to their girl friends' silly and hypothetical question."},
                                    {"role": "assistant", "content": "🌹 What silly question did your girlfriend ask most recently? I'll suggest an answer for it. (eg. If I were a worm, would you still love me?)"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)

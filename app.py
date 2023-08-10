import openai 
import secrets
import streamlit as st
from streamlit_chat import message

st.set_page_config(page_title="KH-CHATBOT", page_icon = 'screenshot (2).png')

openai.api_key = st.secrets['key']

st.title("CHATGPT INTEGRATED CHATBOT",anchor="str")
try:
    def generate_response(prompt):
        completions = openai.Completion.create(
            engine = "text-davinci-003",
            prompt = prompt,
            max_tokens = 500,
            n = 1,
            stop = None,
            temperature=0.5,
        )
        message = completions.choices[0].text
        return message 


    if 'generated' not in st.session_state:
        st.session_state['generated'] = []
    if 'past' not in st.session_state:
        st.session_state['past'] = []
    def get_text():
        prompt=st.chat_input(placeholder="send a message",key=str)
        return prompt
    user_input = get_text()
    if user_input:
        output = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(output)
    if st.session_state['generated']:
        for i in range(0, len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True,avatar_style="adventurer",  '_user')
            message(st.session_state["generated"][i])
except:
    message("SERVERS ARE BUSY",is_user=False)       

from dotenv import load_dotenv
load_dotenv()

import streamlit as st

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
)

# ---------------- Page Config ---------------- #
st.set_page_config(
    page_title="AI Personality Chatbot",
    page_icon="🤖",
    layout="wide"
)

# ---------------- CSS ---------------- #
st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#141E30,#243B55);
}

.title{
    text-align:center;
    color:white;
    font-size:45px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:#dddddd;
    font-size:18px;
}

.chat-box{
    border-radius:15px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Title ---------------- #
st.markdown(
    "<div class='title'>🤖 AI Personality Chatbot</div>",
    unsafe_allow_html=True,
)

st.markdown(
    "<div class='subtitle'>Choose an AI personality and start chatting!</div>",
    unsafe_allow_html=True,
)

# ---------------- Model ---------------- #
model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.9,
    max_tokens=300
)

# ---------------- Sidebar ---------------- #
st.sidebar.title("🎭 AI Personality")

choice = st.sidebar.radio(
    "Select AI Mode",
    [
        "😡 Angry",
        "😂 Funny",
        "😢 Sad"
    ]
)

if choice == "😡 Angry":
    mode = "You are an angry AI agent. You respond aggressively and impatiently."

elif choice == "😂 Funny":
    mode = "You are a very funny AI agent. You respond with humor and jokes."

else:
    mode = "You are a very sad AI agent. You respond in a depressed and emotional tone."

# ---------------- Session ---------------- #

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=mode)
    ]

# If mode changes
if st.session_state.messages[0].content != mode:
    st.session_state.messages = [
        SystemMessage(content=mode)
    ]

# ---------------- Display Chat ---------------- #

for msg in st.session_state.messages[1:]:

    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)

    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# ---------------- Chat Input ---------------- #

prompt = st.chat_input("Type your message...")

if prompt:

    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    with st.chat_message("user"):
        st.write(prompt)

    response = model.invoke(st.session_state.messages)

    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

    with st.chat_message("assistant"):
        st.write(response.content)

# ---------------- Sidebar Footer ---------------- #

st.sidebar.markdown("---")

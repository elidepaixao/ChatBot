
import streamlit as st
# Streamlit (st): biblioteca para criar a interface web do chatbot

from openai import OpenAI
# OpenAI: biblioteca para interagir com a API da OpenAI (modelo de IA)

# ============================================================================
# CARREGANDO A API KEY DE FORMA SEGURA
# ============================================================================
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis do arquivo .env

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("⚠️ API Key da OpenAI não encontrada! Configure o arquivo .env")
    st.stop()

modelo_ia = OpenAI(api_key=api_key)


# ============================================================================
# INTERFACE DO USUÁRIO - TÍTULO
# ============================================================================
st.write("# Chatbot com IA")

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

# ============================================================================
# INTERFACE DO USUÁRIO - CAMPO DE ENTRADA
# ============================================================================
texto_usuario = st.chat_input("Digite sua mensagem")

for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

# ============================================================================
# PROCESSAMENTO DA MENSAGEM DO USUÁRIO
# ============================================================================

if texto_usuario:

    st.chat_message("user").write(texto_usuario)

    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)

    # GERAR E EXIBIR RESPOSTA DA IA
    # ------------------------------------------------------------------------
    resposta_ia = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-4o"
    )
    texto_resposta_ia = resposta_ia.choices[0].message.content
    
    st.chat_message("assistant").write(texto_resposta_ia)

    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}

    st.session_state["lista_mensagens"].append(mensagem_ia)






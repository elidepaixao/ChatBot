#Passo a passo do pensamento lógico para resolver o problema:
# titulo
# input do chat
# a cada mensagem que o usuario enviar:
  # mostrar a mensagem que o usuario enviou no chat
  # pegar a pergunta e enviar para a IA responder
  # exibir a resposta da IA no chat

#para construir um chatbot vamos escolher os frameworks necessarios
# Principais ferramentas de criacao de sistemas: Streamlit, Flask, Django, FastAPI

# STREAMLIT -> permite crair o frintend e o backend utilizando apenas python
# IA que vamos utilizar: OpenAI

# instalando o Streamlit e OpenAI: pip install streamlit openai

import streamlit as st

# colocar o titulo do chat:
st.write("# Chatbot com IA") # formatacao do streamlit: markdonw: #[green] # tamanho titulo

#Para colocar o site no ar: abrir o terminal e rodar o comando: streamlit run + nome do arquivo (main.py)
# Urls geradas:
# Local URL: http://localhost:8501
# Network URL: http://172.20.10.5:8501

#aramzenando o input do usuario na variavel texto_usuario
texto_usuario = st.chat_input("Digite sua mensagem")

# proximo passo: a cada mensagem que o usuario enviar, mostrar a mensagem que o usuario enviou no chat
# print(texto_usuario)
# caso o usuario nao envie nada: vamos criar uma condicional if

# if texto_usuario: #so executa o codigo se o usuario enviar algo
    #print(texto_usuario)

#em vez de printar a mensagem do usuario no terminal, vamos exibir no chat:
if texto_usuario:
    st.chat_message("user").write(texto_usuario) 
    #parametros: 
    # Nome(o icone sera a primeira letra do nome)
    # user (icone padrao do usuario), 
    # assistant (icone padrao da IA)

    #resposta da IA:
    resposta_ia = "Voce perguntou: " + texto_usuario
    st.chat_messsage("assistant").write(resposta_ia)

    # a estrutura acima ja funciona, porem a resposta da IA esta fixa e nao guarda o historico do chat
    # para armazenar o historico do chat, vamos trabalhar com listas.




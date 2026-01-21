# ============================================================================
# PLANEJAMENTO INICIAL DO CHATBOT
# ============================================================================
# Objetivo: Criar um chatbot funcional com interface web
# 
# Passos do projeto:
# 1. Exibir um título na página
# 2. Criar um campo de entrada (input) para o usuário digitar mensagens
# 3. Processar cada mensagem enviada pelo usuário:
#    a) Mostrar a mensagem do usuário na tela do chat
#    b) Enviar a mensagem para a IA processar
#    c) Exibir a resposta da IA no chat
# ============================================================================


# ============================================================================
# ESCOLHA DAS FERRAMENTAS
# ============================================================================
# Frameworks web disponíveis em Python: Streamlit, Flask, Django, FastAPI
#
# Framework escolhido: STREAMLIT
# Motivo: Permite criar frontend E backend usando apenas Python
#
# IA escolhida: OpenAI
#
# Comando para instalar as bibliotecas necessárias:
# pip install streamlit openai
# ============================================================================


# ============================================================================
# IMPORTAÇÕES
# ============================================================================
import streamlit as st
# Streamlit (st): biblioteca para criar a interface web do chatbot
# ============================================================================
from openai import OpenAI
# OpenAI: biblioteca para interagir com a API da OpenAI (modelo de IA)

modelo_ia = OpenAI(api_key="")


# ============================================================================
# INTERFACE DO USUÁRIO - TÍTULO
# ============================================================================
st.write("# Chatbot com IA")
# st.write(): função do Streamlit para exibir conteúdo na página
# O símbolo "#" no texto aplica formatação Markdown (título grande)
# ============================================================================

# Apos o passo de gerar e exibir a resposta da IA, adicionar o seguinte bloco:
# explicacao: criar uma lista de mensagens vazia somente se a lista nao existir
# para isso utilizaremos st.session_state, que guarda dados entre interacoes, como os cookies do navegador
# quando o usuario entrar a primeira vez no site, sera verificado se ja exite esse "cookie", eessa lista de mensagens
# se nao existir a lista de mensagens, ela sera criada como uma lista vazia se ja exisitir, nao sera criada.
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

# ============================================================================
# COMO EXECUTAR O PROJETO
# ============================================================================
# Para colocar o site no ar:
# 1. Abrir o terminal
# 2. Executar o comando: streamlit run main.py
#
# URLs geradas após executar:
# - Local URL: http://localhost:8501 (acesso apenas neste computador)
# - Network URL: http://172.20.10.5:8501 (acesso por outros dispositivos na mesma rede)
# ============================================================================


# ============================================================================
# INTERFACE DO USUÁRIO - CAMPO DE ENTRADA
# ============================================================================
texto_usuario = st.chat_input("Digite sua mensagem")
# st.chat_input(): cria uma caixa de texto estilo chat na parte inferior da página
# Retorna o texto digitado pelo usuário quando ele pressiona Enter
# O texto é armazenado na variável "texto_usuario"
# ============================================================================
# Depois de adcionar as mensagens do usuario e da ia em suas respectivas listas, adicionar o seguinte bloco:
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)
# Loop que percorre todas as mensagens armazenadas em st.session_state["lista_mensagens"]

# ============================================================================
# PROCESSAMENTO DA MENSAGEM DO USUÁRIO
# ============================================================================
# Estratégia: usar uma condicional "if" para verificar se o usuário enviou algo
# Motivo: evitar processar quando a variável estiver vazia (None)
# ============================================================================

if texto_usuario:
    # Este bloco só executa se o usuário digitou e enviou uma mensagem
    
    # ------------------------------------------------------------------------
    # EXIBIR MENSAGEM DO USUÁRIO NO CHAT
    # ------------------------------------------------------------------------
    st.chat_message("user").write(texto_usuario)
    # st.chat_message(): cria um balão de mensagem no chat
    # Parâmetros possíveis:
    #   - "user": exibe ícone padrão de usuário
    #   - "assistant": exibe ícone padrão de assistente/IA
    #   - Qualquer texto: exibe a primeira letra como ícone
    # .write(): exibe o conteúdo dentro do balão de mensagem
    # ------------------------------------------------------------------------

    mensagem_usuario = {"role": "user", "content": texto_usuario}
    # criando a estrutura de mensagem do usuario como um dicionario
    st.session_state["lista_mensagens"].append(mensagem_usuario)
    # adicionando a mensagem do usuario na lista de mensagens armazenada em st.session_state
    # ------------------------------------------------------------------------
    # GERAR E EXIBIR RESPOSTA DA IA
    # ------------------------------------------------------------------------
    resposta_ia = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model="gpt-4o"
    )
    texto_resposta_ia = resposta_ia.choices[0].message.content
    # Aqui a resposta é obtida chamando a API da OpenAI com a lista de mensagens como contexto
    #texto_resposta_ia = "Voce perguntou: " + texto_usuario
    # Aqui a resposta é apenas um exemplo fixo (eco da mensagem do usuário)
    # Futuramente, será substituída por uma chamada real à API da OpenAI
    
    st.chat_message("assistant").write(texto_resposta_ia)
    # Exibe a resposta da IA no chat com ícone de assistente

    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
    # criando a estrutura de mensagem da ia como um dicionario
    st.session_state["lista_mensagens"].append(mensagem_ia)
    # adicionando a mensagem da ia na lista de mensagens armazenada em st.session_state





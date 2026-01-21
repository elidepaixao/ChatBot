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


# ============================================================================
# INTERFACE DO USUÁRIO - TÍTULO
# ============================================================================
st.write("# Chatbot com IA")
# st.write(): função do Streamlit para exibir conteúdo na página
# O símbolo "#" no texto aplica formatação Markdown (título grande)
# ============================================================================


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
    
    
    # ------------------------------------------------------------------------
    # GERAR E EXIBIR RESPOSTA DA IA
    # ------------------------------------------------------------------------
    resposta_ia = "Voce perguntou: " + texto_usuario
    # Aqui a resposta é apenas um exemplo fixo (eco da mensagem do usuário)
    # Futuramente, será substituída por uma chamada real à API da OpenAI
    
    st.chat_messsage("assistant").write(resposta_ia)
    # Exibe a resposta da IA no chat com ícone de assistente
    # ------------------------------------------------------------------------
    
    
    # ========================================================================
    # PROBLEMA IDENTIFICADO
    # ========================================================================
    # A estrutura atual funciona, mas tem duas limitações:
    # 1. A resposta da IA está fixa (não é uma resposta real)
    # 2. Não há histórico do chat (mensagens anteriores desaparecem)
    #
    # PRÓXIMO PASSO:
    # Implementar armazenamento de histórico usando listas e dicionários
    # ========================================================================

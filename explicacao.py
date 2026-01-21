# ============================================================================
# CONCEITOS FUNDAMENTAIS: LISTAS E DICIONÁRIOS
# ============================================================================
# Este arquivo explica estruturas de dados essenciais para o chatbot
# ============================================================================


# ============================================================================
# PARTE 1: TRABALHANDO COM LISTAS
# ============================================================================
# Lista: estrutura que armazena múltiplos valores em sequência
# Característica: os itens são ordenados e acessados por índice (posição)
# ============================================================================

nome_lista = ["Pedro", "Fernanda", "Beatriz"]
# Cria uma lista com 3 nomes (strings)

print(nome_lista)
# Exibe toda a lista no terminal

nome_lista.append("Guilherme")
# .append(): método que adiciona um item no FINAL da lista

print(nome_lista)
# Agora a lista tem 4 nomes

print(nome_lista[2])
# Acessa o item na posição 2 (terceiro item, pois a contagem começa do 0)
# Índices: [0]="Pedro", [1]="Fernanda", [2]="Beatriz", [3]="Guilherme"
# ============================================================================


# ============================================================================
# PARTE 2: TRABALHANDO COM DICIONÁRIOS
# ============================================================================
# Dicionário: estrutura que armazena pares de informações {chave: valor}
# Característica: os valores são acessados pela chave, não por posição
# ============================================================================

idades = {"Pedro": 38, "Fernanda": 35, "Beatriz": 40}
# Cria um dicionário onde:
# - Chaves: nomes das pessoas (strings)
# - Valores: idades das pessoas (números inteiros)

# ----------------------------------------------------------------------------
# Acessando valores no dicionário
# ----------------------------------------------------------------------------
idades["Fernanda"]
# Retorna o valor associado à chave "Fernanda" (no caso, 35)

print(idades["Fernanda"])
# Exibe 35 no terminal
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# Adicionando novos pares chave-valor
# ----------------------------------------------------------------------------
idades["Guilherme"] = 30
# Como "Guilherme" não existe no dicionário, um novo par é adicionado
# Resultado: {"Pedro": 38, "Fernanda": 35, "Beatriz": 40, "Guilherme": 30}

print(idades)
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# Atualizando valores existentes
# ----------------------------------------------------------------------------
idades["Pedro"] = 39
# Como "Pedro" já existe, o valor é atualizado de 38 para 39
# Resultado: {"Pedro": 39, "Fernanda": 35, "Beatriz": 40, "Guilherme": 30}

print(idades)
# ============================================================================


# ============================================================================
# PARTE 3: APLICAÇÃO NO CHATBOT - ESTRUTURA DE MENSAGENS
# ============================================================================
# No chatbot, cada mensagem é um dicionário com 2 chaves obrigatórias:
# - "role": identifica QUEM enviou a mensagem
#     * "user" = mensagem enviada pelo usuário
#     * "assistant" = mensagem enviada pela IA
# - "content": o CONTEÚDO da mensagem (texto)
# ============================================================================

mensagem1 = {"role": "assistant", "content": "Olá, tudo bem?"}
# Primeira mensagem: IA cumprimenta o usuário

mensagem2 = {"role": "user", "content": "Olá! Tudo ótimo, e você?"}
# Segunda mensagem: usuário responde ao cumprimento

mensagem3 = {"role": "assistant", "content": "Estou bem também."}
# Terceira mensagem: IA responde novamente

# ----------------------------------------------------------------------------
# Armazenando o histórico completo do chat
# ----------------------------------------------------------------------------
lista_mensagens = [mensagem1, mensagem2, mensagem3]
# Lista que contém todas as mensagens da conversa em ordem cronológica
# Esta estrutura é fundamental para manter o contexto da conversa
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# Adicionando novas mensagens ao histórico
# ----------------------------------------------------------------------------
nova_mensagem = {"role": "user", "content": "Que bom ouvir isso!"}
# Cria uma nova mensagem do usuário

lista_mensagens.append(nova_mensagem)
# Adiciona a nova mensagem ao final do histórico
# Agora lista_mensagens contém 4 mensagens na ordem da conversa
# ============================================================================

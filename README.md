# Chatbot com IA

Um chatbot web simples e funcional construído com **Streamlit** e integrado à **API da OpenAI (GPT-4o)**. O projeto mantém o histórico completo da conversa durante a sessão e oferece uma interface de chat intuitiva diretamente no navegador.

---

## Funcionalidades

- Interface de chat moderna e responsiva
- Integração com modelos GPT da OpenAI (GPT-4o)
- Histórico de conversa mantido durante a sessão
- Carregamento seguro de credenciais via variáveis de ambiente
- Exibição em tempo real das mensagens do usuário e assistente
- Validação de API Key com mensagem de erro amigável

---

## Tecnologias Utilizadas

- **Python 3.8+**
- **Streamlit** — Framework para criação de aplicações web interativas
- **OpenAI Python SDK** — Biblioteca oficial para integração com a API da OpenAI
- **python-dotenv** — Gerenciamento de variáveis de ambiente

---

## Estrutura do Projeto

```
chatbot-ia/
│
├── app.py                 # Código principal do chatbot
├── .env                   # Arquivo com a chave da API (NÃO COMMITAR)
├── .gitignore             # Ignora arquivos sensíveis
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação
```

---

## Instalação e Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/chatbot-ia.git
cd chatbot-ia
```

### 2. Crie um ambiente virtual (recomendado)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure a API Key da OpenAI

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> **IMPORTANTE**: Nunca compartilhe sua chave pública ou faça commit do arquivo `.env` no GitHub!

---

## Como Executar

No terminal, execute:

```bash
streamlit run app.py
```

O aplicativo será iniciado e estará disponível em:

```
http://localhost:8501
```

---

## Como Funciona

### 1. Carregamento Seguro da API Key
```python
load_dotenv()  # Carrega variáveis do arquivo .env
api_key = os.getenv("OPENAI_API_KEY")
```
- Se a chave não for encontrada, o app exibe um erro e interrompe a execução

### 2. Gerenciamento do Histórico de Conversa
```python
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []
```
- Usa `st.session_state` para armazenar mensagens entre recarregamentos da página

### 3. Exibição das Mensagens
```python
for mensagem in st.session_state["lista_mensagens"]:
    st.chat_message(mensagem["role"]).write(mensagem["content"])
```
- Renderiza todo o histórico a cada interação

### 4. Envio e Resposta
```python
resposta_ia = modelo_ia.chat.completions.create(
    messages=st.session_state["lista_mensagens"],
    model="gpt-4o"
)
```
- Envia o histórico completo para a API
- Recebe e exibe a resposta do assistente
- Adiciona ambas as mensagens ao histórico

---

## Dependências (requirements.txt)

```txt
streamlit
openai
python-dotenv
```

---



## Personalizações Possíveis

### Alterar o modelo de IA
No código, troque `gpt-4o` por outro modelo disponível:
```python
model="gpt-3.5-turbo"  # Mais rápido e econômico
model="gpt-4"          # Modelo anterior
```

## Deploy (Opcional)

### Streamlit Community Cloud
1. Faça push do código para o GitHub (sem o `.env`)
2. Acesse [share.streamlit.io](https://share.streamlit.io)
3. Conecte seu repositório
4. Adicione a `OPENAI_API_KEY` nas **Secrets** do Streamlit


## Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.

---

## Autor

Desenvolvido por [Elide] Inspirado no workshop promovido pela Hashtag Programação


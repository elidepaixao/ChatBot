#listas: adicionamos apenas um tipo de informacao

nome_lista = ["Pedro", "Fernanda", "Beatriz"]
print(nome_lista)
nome_lista.append("Guilherme") #adiciona um item no final da lista  
print(nome_lista)
print(nome_lista[2]) #acessar um item da lista (indexacao comeca do 0)

# dicionarios: adicionamos pares de informacoes {chave: valor, chave: valor}

idades = {"Pedro": 38, "Fernanda": 35, "Beatriz": 40}

#para acessar uma informacao do dicionario: dicionario[chave]
idades["Fernanda"]
print(idades["Fernanda"])
idades["Guilherme"] = 30 #adiciona um novo par chave: valor no dicionario
print(idades)
idades["Pedro"] = 39 #atualiza o valor de uma chave existente
print(idades)

#role = quem eh o usuario (user) ou a IA (assistant)
#content = a mensagem enviada pelo usuario ou pela IA
mensagem1 = {"role": "assistant", "content": "Olá, tudo bem?"}
mensagem2 = {"role": "user", "content": "Olá! Tudo ótimo, e você?"}
mensagem3 = {"role": "assistant", "content": "Estou bem também."}

lista_mensagens = [mensagem1, mensagem2, mensagem3]

nova_mensagem = {"role": "user", "content": "Que bom ouvir isso!"}
lista_mensagens.append(nova_mensagem)
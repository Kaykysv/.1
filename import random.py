import random

# Lista de saudações para o assistente responder
saudacoes = ["Olá!", "Oi!", "E aí!", "Oi, tudo bem?"]

# Lista de perguntas e respostas para o assistente responder
perguntas_respostas = {
    "Qual é o seu nome?": "Meu nome é Assistente Virtual.",
    "Como você está?": "Estou bem, obrigado por perguntar!",
    "O que você pode fazer?": "Posso responder perguntas simples e ajudar com informações básicas."
}

# Função para gerar uma resposta do assistente
def responder(pergunta):
    if pergunta in perguntas_respostas:
        return perguntas_respostas[pergunta]
    else:
        return "Desculpe, não entendi a pergunta."

# Função principal do programa
def main():
    print("Olá! Eu sou um assistente virtual. Como posso te ajudar?")
    
    while True:
        pergunta = input("> ")
        
        if pergunta.lower() == "sair":
            print("Até logo!")
            break
        
        if pergunta.endswith("?"):
            print(responder(pergunta))
        else:
            print(random.choice(saudacoes))

# Executa o programa
if __name__ == "__main__":
    main()
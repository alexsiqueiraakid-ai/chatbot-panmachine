from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # PERMITE chamadas do GitHub Pages


def handle_input(user_input):
    if not user_input:
        return "Mensagem vazia."

    user_input = user_input.lower()

    if any(saudacao in user_input for saudacao in ["noite", "dia", "tarde", "ola", "olá", "oi"]):
        return (
            "Olá! Sou o assistente técnico da Panmachine.<br>"
            "Como posso ajudar você com a operação da máquina hoje?"
        )

    elif any(cmd in user_input for cmd in ["referenciar", "zerar ferramenta", "presset", "precetar", "precipitar"]):
        link = "https://www.youtube.com/watch?v=navfeH6Ycvk"
        return f'Assista ao vídeo: <a href="{link}" target="_blank">Clique aqui para Referenciar</a>'

    elif any(cmd in user_input for cmd in ["ponto zero", "zerar a peça", "definir origem"]):
        link = "https://www.youtube.com/watch?v=SFcdutK9iYk"
        return f'Veja como definir a origem: <a href="{link}" target="_blank">Tutorial Ponto Zero</a>'

    elif any(cmd in user_input for cmd in ["programa na memoria", "programa na memória"]):
        return "Tutorial de programa na memória ainda não disponível."

    elif any(cmd in user_input for cmd in ["pendrive", "programa pelo pendrive", "pen drive"]):
        return "Tutorial de execução via pendrive ainda não disponível."

    elif any(cmd in user_input for cmd in ["programa pelo cartao", "cartão"]):
        return "Tutorial de execução via cartão ainda não disponível."

    elif any(cmd in user_input for cmd in ["chamar no bloco", "chamada de bloco"]):
        return "Tutorial de chamada de bloco ainda não disponível."

    elif any(cmd in user_input for cmd in ["parar o programa", "abrir a porta"]):
        return "Tutorial para abrir a porta sem resetar o programa ainda não disponível."

    elif any(cmd in user_input for cmd in ["codigos g", "g code", "códigos g"]):
        return (
            "Aqui estão os principais códigos G:<br>"
            "<b>G00:</b> Posicionamento rápido<br>"
            "<b>G01:</b> Interpolação linear<br>"
            "<b>G02/G03:</b> Interpolação circular<br>"
            "<b>G43:</b> Compensação de comprimento de ferramenta."
        )

    elif any(cmd in user_input for cmd in ["codigos m", "códigos m", "miscelanea", "miscelâneas"]):
        return (
            "Aqui estão os principais códigos M:<br>"
            "<b>M03:</b> Liga o fuso<br>"
            "<b>M05:</b> Desliga o fuso<br>"
            "<b>M06:</b> Troca de ferramenta<br>"
            "<b>M08/M09:</b> Fluido de corte."
        )

    return (
        "Desculpe, não entendi.<br>"
        "Exemplos:<br>"
        "- Quais são os códigos G?<br>"
        "- O que é modo DNC?"
    )


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    response = handle_input(user_input)
    return jsonify({"response": response})


@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "API do chatbot ativa"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

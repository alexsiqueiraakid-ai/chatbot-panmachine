from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def handle_input(user_input):
    user_input = user_input.lower()

    if any(saudacao in user_input for saudacao in ["noite", "dia", "tarde", "ola", "oi"]):
         return ("Olá! Sou o assistente técnico da Panmachine.<br>"
                "Como posso ajudar você com a operação da máquina hoje?")
    
    elif any(cmd in user_input for cmd in ["referenciar", "zerar", "presset", "precetar"]):
        link = "https://www.youtube.com/watch?v=navfeH6Ycvk"
        return f'Assista ao vídeo: <a href="{link}" target="_blank">Clique aqui para Referenciar</a>'

    elif any(cmd in user_input for cmd in ["ponto zero", "zerar a peça", "definir origem"]):
        link = "https://www.youtube.com/watch?v=SFcdutK9iYk"
        return f'Veja como definir a origem: <a href="{link}" target="_blank">Tutorial Ponto Zero</a>'

    elif any(cmd in user_input for cmd in ["programa na memoria"]):
        link = "https://www..............."
        return f'Veja como executar o programa na memória da máquina: <a href="{link}" target="_blank">Tutorial Cartao</a>'

    elif any(cmd in user_input for cmd in ["programa pelo pendrive"]):
        link = "https://www..............."
        return f'Veja como executar o programa via pendrive: <a href="{link}" target="_blank">Tutorial Pendrive</a>'
    
    elif any(cmd in user_input for cmd in ["programa pelo cartao"]):
        link = "https://www..............."
        return f'Veja como executar o programa via cartão: <a href="{link}" target="_blank">Tutorial Cartao</a>'
    
    elif any(cmd in user_input for cmd in ["chamar no bloco", "chamada de bloco", "meio do programa"]):
        link = "https://www..............."
        return f'Veja como fazer chamada de bloco: <a href="{link}" target="_blank">Tutorial Cartao</a>'
    
    elif any(cmd in user_input for cmd in ["parar o programa", "abrir a porta", "sem resetar", "sem resetar o programa"]):
        link = "https://www..............."
        return f'Veja como abrir a porta sem resetar o programa: <a href="{link}" target="_blank">Tutorial Cartao</a>'
    
      # Códigos G e M comuns
    elif "codigo g" in user_input or "códigos g" in user_input:
        return ("Aqui estão os principais códigos G:<br>"
                "<b>G00:</b> Posicionamento rápido<br>"
                "<b>G01:</b> Interpolação linear (avanço programado)<br>"
                "<b>G02/G03:</b> Interpolação circular<br>"
                "<b>G43:</b> Compensação de comprimento de ferramenta.")
    
    
    elif "codigo m" in user_input or "códigos m" in user_input:
        return ("Aqui estão os principais códigos M:<br>"
                "<b>M03:</b> Liga o fuso (sentido horário)<br>"
                "<b>M05:</b> Desliga o fuso<br>"
                "<b>M06:</b> Troca de ferramenta<br>"
                "<b>M08/M09:</b> Liga/Desliga fluido de corte.")
    


    
    elif any(cmd in user_input for cmd in ["dnc" , "mode dnc"]):
        return ("O <b>Modo DNC</b> permite executar programas externos via Cartão CF ou RS232.<br>"
                "Certifique-se de que o parâmetro de canal de entrada está correto.")
         
    elif any(cmd in user_input for cmd in ["edit", "mode edit"]):
        return ("O <b>Modo EDIT</b> é utilizado para criar novos programas ou alterar códigos existentes.<br>"
                "Lembre-se de liberar a chave de proteção de memória antes de editar.")
    
    elif any(cmd in user_input for cmd in ["single block", "block", "single"]):
        return "A função dessa tecla é executar o programa bloco a bloco"
    
    elif any(cmd in user_input for cmd in ["jog", "tecla jog"]):
        return "A função dessa tecla é realizar movimentos no eixos através das teclas X, Y, Z, A e C "
    
    elif any(cmd in user_input for cmd in ["teach", "teach in", "tecla teach"]):
        return "A função dessa tecla é permitir ao operador aproximar manualmente " \
               "o eixo da máquina até uma posição desejada e então salvar essa posição como parte de um bloco de programa"
    
    elif any(cmd in user_input for cmd in ["auto", "tecla auto"]):
        return "A função dessa tecla é executar programas no modo automático"
    
    elif any(cmd in user_input for cmd in ["mda", "tecla mda"]):
        return "A função dessa tecla é executar programas curtos, ligar a rotação, " \
               "fazer um posicionamento dos eixos e até troca de ferramentas"
    
    elif any(cmd in user_input for cmd in ["spindle stop", "stop", "tecla spindle stop"]):
        return "A função dessa tecla é desbilitar a rotação do spindle"
    
    elif any(cmd in user_input for cmd in ["spindle start", "start", "tecla spindle start"]):
        return "A função dessa tecla é habilitar a rotação do spindle"
    
    elif any(cmd in user_input for cmd in ["feed stop", "tecla feed stop"]):
        return "A função dessa tecla é desabilitar o movimento dos eixos"
    
    elif any(cmd in user_input for cmd in ["feed start", "tecla feed start"]):
        return "A função dessa tecla é habilitar o movimento dos eixos"
    
    elif any(cmd in user_input for cmd in ["spindle cw", "tecla spindle cw"]):
        return "A função dessa tecla é ligar o fuso no sentido horário"
    
    elif any(cmd in user_input for cmd in ["spindle ccw", "tecla spindle ccw"]):
        return "A função dessa tecla é ligar o fuso no sentido anti-horário"
    
    elif any(cmd in user_input for cmd in ["mag jog", "tecla mag jog"]):
        return "A função dessa tecla é rotacionar o magazine manualmente"
    
    elif any(cmd in user_input for cmd in ["mag atc", "mag / atc", "tecla mag atc", "atc"]):
        return "A função dessa tecla é rotacionar o braço trocador de ferramentas do magazine"
    
    elif any(cmd in user_input for cmd in ["pocket up/down", "pocket", "tecla pocket", "up/down"]):
        return "A função dessa tecla é subir ou descer o pote de ferramenta do magazine"

    elif any(cmd in user_input for cmd in ["conv rev", "tecla conv rev"]):
        return "A função dessa tecla é ligar o transportador de cavacos no sentido horário"
    
    elif any(cmd in user_input for cmd in ["conv fwd", "tecla conv fwd"]):
        return "A função dessa tecla é ligar o transportador de cavacos no sentido anti-horário"
    
    elif any(cmd in user_input for cmd in ["air blast", "air", "tecla air blast"]):
        return "A função dessa tecla é ligar a refrigeração a AR"
    
    elif any(cmd in user_input for cmd in ["hp coolant on", "hp coolant", "tecla hp coolant on"]):
        return "A função dessa tecla é ligar a refrigeração de alta pressão"
    
    elif any(cmd in user_input for cmd in ["coolant on", "coolant", "tecla coolant on"]):
        return "A função dessa tecla é ligar a refrigeração "
    
    elif any(cmd in user_input for cmd in ["coolant auto", "coolant", "tecla coolant auto"]):
        return "A função dessa tecla é ligar a refrigeração automaticamente quando programa contemplar M8"
    
    elif any(cmd in user_input for cmd in ["chip flush", "chip", "flush", "tecla chip flush"]):
        return "A função dessa tecla é ligar a lavagem de cavacos da carenagem"

    elif any(cmd in user_input for cmd in ["water gun", "water", "gun", "tecla water gun"]):
        return "A função dessa tecla é ligar pistola de lavagem da máquina"
    

    

    

    

    
    

    
   

    
    return "Desculpe, não entendi. Pode repetir?"

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message")
    response = handle_input(user_input)
    return jsonify({'response': response})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
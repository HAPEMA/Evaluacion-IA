import os
from dotenv import load_dotenv
from openai import OpenAI

# Cargar el .env desde la raíz del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

client = OpenAI()

def chat():
    mensajes = [
        {"role": "system", "content": "Eres el asistente virtual de EcoMarket."}
    ]

    print("Chatbot iniciado 🤖 (escribe 'salir' para terminar)\n")

    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "salir":
            print("Chatbot finalizado 👋")
            break

        mensajes.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=mensajes,
                temperature=0.3,
                max_tokens=200
            )

            reply = response.choices[0].message.content
            print("Bot:", reply, "\n")

            mensajes.append({"role": "assistant", "content": reply})
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    chat()

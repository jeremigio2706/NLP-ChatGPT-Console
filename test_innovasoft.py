from openai import OpenAI
import os
api = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api)

def consulta_nlp(texto):
    try:
        # Preparar los mensajes para la API
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": texto}
        ]

        # Petición API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        # Acceso a la respuesta actualizado
        return response.choices[0].message.content
    except Exception as e:
        return str(e)

def main():
    while True:
        print("Escribe 'salir' para terminar la consola.")
        consulta = input("Introduce tu consulta NLP: ")
        if consulta.lower() == 'salir':
            break
        respuesta = consulta_nlp(consulta)
        print("Respuesta:", respuesta)

if __name__ == "__main__":
    main()

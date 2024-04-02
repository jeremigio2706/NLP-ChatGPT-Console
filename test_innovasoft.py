import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def consulta_nlp(texto):
    try:
        # Petición API
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=texto
        )
        # Acceso a la respuesta actualizado
        return response['choices'][0].message
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

from main import engine, Session
from tables import Cliente, Base

from google import genai
from google.genai import types

#to learn GEMINI_API_KEY on dev enviroment
#from dotenv import load_dotenv
#load_dotenv()

def agregar_clientes(nombre: str, correo:str) -> str:
    session = Session()
    cliente = Cliente(name=nombre, email=correo)
    try: 
        session.add(cliente)
        session.flush()
    except Exception:
        session.rollback()

    session.commit()
    return f"usuario: {nombre} añadido con exito"



agregar_clientes_function = {
    "name": "agregar_clientes",
    "description": "Esta funcion permite al cliente registrar su nombre y correo en la base de datos de la empresa",
    "parameters": {
        "type": "object",
        "properties": {
            "nombre": {
                "type": "string",
                "description": "su nombre personal, con el cual se identificará",
            },
            "correo": {
                "type": "string",
                "description": "Correo electronico de contacto",
            },
        },
        "required": ["nombre", "correo"],
    },
}

client = genai.Client()
tools = types.Tool(function_declarations=[agregar_clientes_function])
config = types.GenerateContentConfig(tools=[tools])


chat = client.chats.create(
    model="gemini-3-flash-preview", config=config
)

query = input("Introduce texto:")

while query != "finish":
    response = chat.send_message(query)

    if response.candidates[0].content.parts[0].function_call:
        function_call = response.candidates[0].content.parts[0].function_call
        print(f"Function to call: {function_call.name}")
        print(f"Arguments: {function_call.args}")

        if function_call.name == "agregar_clientes":
            result = agregar_clientes(**function_call.args)
            print(f"Function execution result: {result}")

    else:
        print("No function call found in the response.")
        print(response.text)

    query = input("Introduce texto:")
    
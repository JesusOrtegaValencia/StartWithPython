from google import genai
from dotenv import load_dotenv
from google.genai import types

load_dotenv()

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

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="registrame, me llamo Jesus y mi correo es ov863936@gmail.com",
    config=config,
)

if response.candidates[0].content.parts[0].function_call:
    function_call = response.candidates[0].content.parts[0].function_call
    print(f"Function to call: {function_call.name}")
    print(f"Arguments: {function_call.args}")
    
else:
    print("No function call found in the response.")
    print(response.text)
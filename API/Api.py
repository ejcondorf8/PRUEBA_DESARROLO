from pydantic import BaseModel
import openai as op

op.api_key='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'
op.organization='org-Yo1JN6VlDoZBuPwiLbGxWPgm'

class Model(BaseModel):
    tipo : int

def funcion(frase:int)->list:
    contenido=op.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role':'system','content':'Eres una calculadora factorial'},
            {'role':'user','content':'Calcula el factorial del numero ingresado  y muestre el resultado de tipo entero que se envie en el body y muestra el resultado  y si es un tipo texto  presenta un error'+str(frase)}
        ]


    )
    v1=contenido.choices[0].message.content
    v2=contenido.usage.total_tokens
    return [v1,v2]
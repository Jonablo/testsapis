import os
import openai
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI(
    organization = os.getenv("OPENAI_ORGANIZATION"),
    api_key = os.getenv("OPENAI_API_KEY"),
)

class Document(BaseModel):
    prompt: str = ""


def calcuFact(prompt: str) -> list:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": """Eres una calculadora factorial y das el factorial del numero que se te proporcione, pero cuando sea un texto devolver un "Syntax.error" E.G: Matematicas
             -Es un sistema facil para aprender a multiplicar""",
            },
            {"role": "user", "content": prompt},
        ],
    )
    content = completion.choices[0].message.content
    total_tokens = completion.usage.total_tokens

    print("[TERMINO DE CALCULAR]".center(40, "-"))
    return [content, total_tokens]
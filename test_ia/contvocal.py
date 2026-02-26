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


def conta(prompt: str) -> list:
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": """Eres un contador de vocales dentro de las palabras que te proporcionen E.G: Lenguaje
             -Es como un juego que ayuda a aprender a leer""",
            },
            {"role": "user", "content": prompt},
        ],
    )
    content = completion.choices[0].message.content
    total_tokens = completion.usage.total_tokens

    print("[TERMINO EL PROCESO]".center(40, "-"))
    return [content, total_tokens]

"""My frases"""

import random

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()


FRASES_PATH = "frases.txt"


@app.get("/", response_class=PlainTextResponse)
def read_root():
    """hello world"""

    with open(FRASES_PATH, "r", encoding="utf-8") as frases_file:
        frases = frases_file.readlines()

    return_frase = random.choice(frases)

    return return_frase

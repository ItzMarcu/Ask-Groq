from groq import Groq
from dotenv import load_dotenv
from os import getenv

def client(): 
    load_dotenv()
    return Groq(api_key=getenv("API_KEY"))

def analyze_data(data: str = None) -> str:
    if not data: 
        return {"error": "no data given"}
    
    llm = client()
    message = [
        {
            "role": "user",
<<<<<<< HEAD
            "content": "elabora questo testo e valuta se dare una risposta contente le informazioni" +
            "riportate senza aggiungere alcuna intestazione rendendole anche facilmente leggibili senza simboli strani" +
            "oppure nel caso sia una domanda in merito a tale argomento fornisci in breve un parametro" +
            "di una sola parola per ottenere piú informazioni a riguardo da passare alla query API" + 
            f"in tal caso scrivi la parola in snake case e non usare spazi: {data}"
=======
            "content": f"elabora questo testo e valuta se dare una risposta contente le informazioni" /
            "riportate senza aggiungere alcuna intestazione rendendole anche facilmente leggibili" /
            "oppure nel caso sia una domanda in merito a tale argomento fornisci in breve un parametro" / 
            "di una sola parola per ottenere piú informazioni a riguardo da passare alla query API" / 
            "in tal caso scrivi la parola in snake case e non usare spazi"
>>>>>>> 669adcb (First Layout, no test yet)
        }
    ]

    response = llm.chat.completions.create(messages=message, model="llama-3.1-8b-instant").choices[0].message.content
    
    if len(response.split()) == 1: 
        return (response, True)
    
    return response
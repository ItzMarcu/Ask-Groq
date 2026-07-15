from bs4 import BeautifulSoup
from requests import get, RequestException
from fastapi import HTTPException

def scrape(url: str = None): 
    if not url: 
        return {"errore": "no url given"}
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1"
    }

    try: 
        response = get(url, headers=headers, timeout=15)
        if response.status_code == 200: 
            data = BeautifulSoup(response.text, "html.parser").find(id="mw-content-text").text

            if not data: 
                raise HTTPException(status_code=404, id="data not found")
            
            return data[:10000]
    
    except RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

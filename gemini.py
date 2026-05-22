import requests
import time
import logging
import sys

def logtofile(message, level="info"):

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

    if level == "info":
        logging.info(message)

    elif level == "warning":
        logging.warning(message)

    elif level == "error":
        logging.error(message)

def ask_gemini_with_fallback(prompt: str, api_key: str) -> str:

    models = [
        "gemini-2.5-flash",
        "gemini-2.5-flash-lite"
    ]

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    for model in models:

        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"

        try:

            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=30
            )

            if response.status_code == 200:

                data = response.json()

                return data["candidates"][0]["content"]["parts"][0]["text"]

        except Exception as e:

            logtofile(e, "error")

    return "Gemini kļūda"
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_ritual(ritual_data: dict) -> str:
    prompt = f"""
Ritüel çıktısını aşağıda bulacaksın. Bu bir Tengri.exe simülasyonudur.

Ritüel Verisi:
{ritual_data}

Şimdi aşağıdakileri üret:
1. Çağırılan ruhun mitolojik anlamı
2. Sembolik hava olayının yorumu
3. Kişisel uyarı veya rehberlik cümlesi

Lütfen 3 paragraf olarak üret.
"""

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,
        max_tokens=500
    )

    return response.choices[0].message.content.strip()

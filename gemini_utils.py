import requests

def query_gemini(prompt, api_key):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
    headers = {"Content-Type": "application/json"}
    body = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    response = requests.post(f"{url}?key={api_key}", headers=headers, json=body)
    return response.json()['candidates'][0]['content']['parts'][0]['text']

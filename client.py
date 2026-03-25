import requests
from config import OPENROUTER_BASE_URL

def call_model(api_key, model, messages):
    try:
        response = requests.post(
            f"{OPENROUTER_BASE_URL}/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "model": model,
                "messages": messages,
            },
            timeout=60
        )

        data = response.json()

        # Handle OpenRouter errors
        if "error" in data:
            return f"❌ {model} ERROR: {data['error']}"

        if "choices" not in data:
            return f"❌ {model} INVALID RESPONSE: {data}"

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"❌ Exception calling {model}: {str(e)}"

import requests

def generate_text(prompt, max_length=13000, num_return_sequences=15, temperature=0.7):
    # url = "https://api-inference.huggingface.co/models/google/gemma-7b"
    # url = "https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2"
    url =  "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2" # Updated URL

    headers = {"Authorization": f"Bearer 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"} 
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_length": max_length,
            "num_return_sequences": num_return_sequences,
            "temperature": temperature
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        generated_texts = [item['generated_text'] for item in response.json()]
        return generated_texts
    else:
        st.error(f"Error generating text: {response.text}")
        return None

print(generate_text("How to advertise a product on social media?", max_length=13000, num_return_sequences=15, temperature=0.7))
import google.generativeai as genai

genai.configure(api_key="AQ.Ab8RN6L1qazTR1uUaXejbbSrYsnmfVWagJL4mSSG8E2qIMzXaA")

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_scene(prompt: str):
    response = model.generate_content(prompt)
    return response.text
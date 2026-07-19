import google.generativeai as genai

genai.configure(api_key="API_KEY")

models = [
    "gemini-2.0-flash",
    "gemini-2.0-flash-lite",
    "gemini-flash-latest",
    "gemini-pro-latest",
    "gemini-3-flash-preview",
    "gemini-3.5-flash"
]

for m in models:
    try:
        print(f"\nTesting {m}")

        model = genai.GenerativeModel(m)

        response = model.generate_content("Say Hello")

        print("SUCCESS:", response.text)

    except Exception as e:
        print("FAILED:", e)
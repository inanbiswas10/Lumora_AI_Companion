from src.llm.gemini_provider import Gemini_Provider

provider = Gemini_Provider ()

response = provider.generate_response_function ("Introduce yourself in two sentences.")

print (response)
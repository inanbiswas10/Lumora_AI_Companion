from src.llm.openrouter_provider import OpenRouter_Provider

provider = OpenRouter_Provider ()

response = provider.generate_response_function ("Introduce yourself in two sentences.")

print (response)
from src.llm.groq_provider import Groq_Provider

provider = Groq_Provider ()

response = provider.generate_response_function ("Introduce yourself in two sentences.")

print (response)
from google import genai
from config.api_keys import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

for model in client.models.list ():
    print (model.name)
    print ()
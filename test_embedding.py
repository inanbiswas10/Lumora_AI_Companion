from src.embeddings.embedding_provider import Embedding_Provider

provider = Embedding_Provider ()

embedding = provider.generate_embedding_function ("Tomorrow is my exam.")

print (type (embedding))
print ( len (embedding))
print (embedding [:10])
"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Embedding Provider

Description: Generates vector embeddings for text.

Responsibilities:
    - Convert text into embeddings
    - Hide embedding implementation
    - Support future providers

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

from sentence_transformers import SentenceTransformer


class Embedding_Provider:
    def __init__(self):

        print (f"[Embedding] Loading embedding model !!")
        print ()

        self.model = SentenceTransformer ("all-MiniLM-L6-v2")

        print (f"[Embedding] Model loaded successfully !!")
        print ()

    def generate_embedding_function (self,text):

        return self.model.encode (text).tolist ()
        print ()
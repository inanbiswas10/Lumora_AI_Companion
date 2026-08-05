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
from src.config.settings import Settings


class Embedding_Provider:
    def __init__(self):

        print (f"Loading embedding model !!")
        print ()

        self.model = SentenceTransformer (Settings.EMBEDDING_MODEL)

        print (f"Embedding model loaded successfully !!")
        print ()

    def generate_embedding_function (self,text):

        return self.model.encode (text).tolist ()
        print ()
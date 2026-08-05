"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Embedding Generator

Description: Generates vector embeddings for memories.

Responsibilities:
    - Convert text into embeddings
    - Support future embedding models
    - Provide a unified interface

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

class Embedding_Generator:

    def generate_embedding_function (self,text):

        """
        Placeholder embedding.

        Later this will call a real embedding
        model such as:

        • Gemini Embeddings
        • OpenAI
        • Sentence Transformers

        """

        embedding = []

        for character in text.lower ():

            embedding.append (ord (character)/255)
        return embedding
"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Semantic Retriever

Description: Finds the most semantically relevant memories.

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

from src.embeddings.similarity import Similarity


class Semantic_Retriever:

    def __init__ (self,database,embedding_provider):

        self.database = database
        self.embedding_provider = embedding_provider
        self.similarity = Similarity ()

    def retrieve_relevant_memories_function (self,user_message,top_k = 3):

        query_embedding = self.embedding_provider.generate_embedding_function (user_message)

        memories = self.database.get_all_embeddings_function ()

        scored_memories = []

        for memory_id,memory_text,embedding in memories:

            score = self.similarity.cosine_similarity_function (query_embedding,embedding)

            scored_memories.append ((score, memory_text))

        scored_memories.sort (reverse = True,key = lambda x: x [0])
        return scored_memories [:top_k]
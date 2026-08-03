"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Similarity

Description: Calculates cosine similarity between two embedding vectors.

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

import math

class Similarity:

    def cosine_similarity_function (self,vector1,vector2):

        dot_product = sum (a*b for a,b in zip (vector1,vector2))

        magnitude1 = math.sqrt (sum (a*a for a in vector1))
        magnitude2 = math.sqrt (sum (b*b for b in vector2))

        if magnitude1 == 0 or magnitude2 == 0:
            return 0
        return dot_product / (magnitude1 * magnitude2)
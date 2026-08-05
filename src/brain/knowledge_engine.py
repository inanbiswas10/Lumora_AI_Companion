"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Knowledge Engine

Description: Manages knowledge retrieval inside Lumora. It decides whether knowledge can be answered from local memory, local knowledge or should be delegated to the language model.

Responsibilities:
    - Search local knowledge
    - Store knowledge
    - Retrieve knowledge
    - Support future web search
    - Support future document retrieval
    - Support future RAG pipeline

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

class Knowledge_Engine:

    def __init__ (self):

        self.knowledge_base = {

            "python":
                "Python is a high-level, interpreted programming language.",

            "artificial intelligence":
                "Artificial Intelligence enables machines to perform tasks that normally require human intelligence.",

            "machine learning":
                "Machine Learning is a branch of AI that learns patterns from data.",

            "deep learning":
                "Deep Learning uses neural networks with multiple layers.",

            "lumora":
                "Lumora is an intelligent AI Companion being developed by Inan Biswas."

        }

    # --------------------------------------------------------

    def search_local_knowledge_function (

        self,

        query

    ):

        query = query.lower ()

        for key, value in self.knowledge_base.items ():

            if key in query:

                return value

        return None

    # --------------------------------------------------------

    def add_knowledge_function (

        self,

        topic,

        information

    ):

        self.knowledge_base [topic.lower ()] = information

    # --------------------------------------------------------

    def get_all_topics_function (self):

        return sorted (self.knowledge_base.keys ())

    # --------------------------------------------------------

    def build_knowledge_prompt_function (

        self,

        user_message

    ):

        knowledge = self.search_local_knowledge_function (
            user_message
        )

        if knowledge:

            return f"""

Relevant Knowledge

{knowledge}

"""

        return ""
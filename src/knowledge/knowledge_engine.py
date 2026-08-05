"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Knowledge Engine

Description: Maintains structured knowledge about the user and the world.

Responsibilities:
    - Store relationships
    - Retrieve related facts
    - Build a simple knowledge graph
    - Support future reasoning

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

class Knowledge_Engine:

    def __init__ (self):

        self.knowledge = {}

    # ---------------------------------------------------------

    def add_fact_function (
        self,
        subject,
        relation,
        object_value
    ):

        if subject not in self.knowledge:

            self.knowledge [subject] = []

        self.knowledge [subject].append (

            {
                "relation": relation,
                "object": object_value
            }

        )

    # ---------------------------------------------------------

    def get_facts_function (
        self,
        subject
    ):

        return self.knowledge.get (subject,[])

    # ---------------------------------------------------------

    def get_all_knowledge_function (self):

        return self.knowledge
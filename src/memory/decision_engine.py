"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Memory Decision Engine

Description: Determines how Lumora should process every incoming user message.

Responsibilities:
    - Decide whether to store memories
    - Decide whether semantic search is needed
    - Decide whether episodic memory is needed
    - Decide memory priority

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""
class Memory_Decision_Engine:

    def analyze_function (self,message,importance):
        decision = {

            "store_memory": False,
            "create_episode": False,
            "retrieve_semantic": False,
            "retrieve_recent": True
        }
        if (importance >= 7):
             decision ["store_memory"] = True
             decision["retrieve_semantic"] = True
        keywords = [

            "exam",
            "birthday",
            "interview",
            "job",
            "graduation",
            "marriage",
            "trip",
            "hospital",
            "promotion"
        ]
        message_lower = message.lower ()
        for word in keywords:
            if word in message_lower:
                decision ["create_episode"] = True
                break
        return decision
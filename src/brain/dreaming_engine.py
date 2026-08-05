"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Dreaming Engine

Description: Performs offline memory consolidation by reviewing stored memories,identifying important experiences and preparing them for long-term retention.

Responsibilities:
    - Consolidate memories
    - Strengthen important memories
    - Detect similar memories
    - Generate insights
    - Prepare future autonomous learning

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""
class Dreaming_Engine:

    def __init__ (self,database):

        self.database = database

    # --------------------------------------------------------

    def consolidate_memories_function (self):

        memories = self.database.get_conversation_memories_function ()

        if not memories:

            return []

        consolidated = []

        seen = set ()

        for memory in memories:

            key = memory.lower ().strip ()

            if key not in seen:

                seen.add (key)

                consolidated.append (memory)

        return consolidated

    # --------------------------------------------------------

    def detect_similar_memories_function (self):

        memories = self.database.get_conversation_memories_function ()

        similar = []

        for i in range (len (memories)):

            for j in range (i + 1,len (memories)):

                words_a = set (memories [i].lower ().split ())

                words_b = set (memories [j].lower ().split ())

                overlap = words_a.intersection (words_b)

                if len (overlap) >= 3:

                    similar.append (

                        (memories [i],memories [j])

                    )

        return similar

    # --------------------------------------------------------

    def build_dream_report_function (self):

        report = {

            "total_memories": len (
                self.database.get_conversation_memories_function ()
            ),

            "unique_memories": len (
                self.consolidate_memories_function ()
            ),

            "similar_pairs": len (
                self.detect_similar_memories_function ()
            )
        }
        return report
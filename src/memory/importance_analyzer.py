"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Importance Analyzer

Description: Assigns an importance score to memories before they are stored.

Responsibilities:
    - Analyze memory importance
    - Return a score from 1 to 10

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""
class Importance_Analyzer:
    def calculate_importance_function (self,memory):
        memory = memory.lower ()

        important_keywords = [

            "birthday",
            "birth",
            "name",
            "university",
            "college",
            "school",
            "job",
            "work",
            "career",
            "goal",
            "dream",
            "family",
            "mother",
            "father",
            "sister",
            "brother"
        ]
        for keyword in important_keywords:
            if keyword in memory:
                return 9

        medium_keywords = [

            "favorite",
            "favourite",
            "hobby",
            "interest",
            "music",
            "movie",
            "football",
            "cricket"

        ]
        for keyword in medium_keywords:
            if keyword in memory:
                return 7
            return 3

        
"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Relationship Manager

Description: Stores and manages information about people in the user's life.

Responsibilities:
    - Store relationships
    - Retrieve relationships
    - Search people
    - Prepare future relationship graphs

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

class Relationship_Manager:

    def __init__ (self,database):

        self.database = database

    # ---------------------------------------------------------
    # Detect relationship information
    # ---------------------------------------------------------

    def detect_relationship_function (self,user_message):

        message = user_message.lower ()

        relationship_keywords = {

            "mother": [
                "my mother",
                "my mom",
                "my mum"
            ],

            "father": [
                "my father",
                "my dad"
            ],

            "brother": [
                "my brother"
            ],

            "sister": [
                "my sister"
            ],

            "friend": [
                "my friend"
            ],

            "best friend": [
                "my best friend"
            ],

            "girlfriend": [
                "my girlfriend"
            ],

            "boyfriend": [
                "my boyfriend"
            ],

            "teacher": [
                "my teacher",
                "my professor"
            ],

            "classmate": [
                "my classmate"
            ]
        }
        for relationship,patterns in relationship_keywords.items ():

            for pattern in patterns:

                if pattern in message:

                    return relationship

        return None

    # ---------------------------------------------------------
    # Store relationship
    # ---------------------------------------------------------

    def store_relationship_function (

        self,

        name,

        relationship,

        notes = ""

    ):

        self.database.save_relationship_function (

            name,

            relationship,

            notes

        )

    # ---------------------------------------------------------
    # Retrieve all relationships
    # ---------------------------------------------------------

    def retrieve_relationships_function (self):

        return self.database.get_relationships_function ()

    # ---------------------------------------------------------
    # Search person
    # ---------------------------------------------------------

    def search_person_function (

        self,

        name

    ):

        relationships = self.retrieve_relationships_function ()

        for person in relationships:

            if person ["name"].lower() == name.lower ():

                return person

        return None

    # ---------------------------------------------------------
    # Build relationship summary
    # ---------------------------------------------------------

    def build_summary_function (self):

        relationships = self.retrieve_relationships_function ()

        if not relationships:

            return "No relationships stored."

        summary = []

        for person in relationships:

            summary.append (

                f"{person ['name']} ({person ['relationship']})"

            )
        return "\n".join (summary)
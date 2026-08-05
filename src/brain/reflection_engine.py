"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Reflection Engine

Description: Allows Lumora to periodically reflect on conversations and discover long-term knowledge about the user.

Responsibilities:
    - Analyze conversation history
    - Identify recurring topics
    - Discover user interests
    - Discover user goals
    - Prepare summaries
    - Support future self-learning

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""
from collections import Counter

class Reflection_Engine:

    def __init__ (self,database):

        self.database = database

    def generate_reflection_function (self):

        conversations = (
            self.database
            .get_all_messages_function ()
        )

        if not conversations:

            return {
                "summary": "No conversations available.",
                "top_topics": [],
                "conversation_count": 0
            }

        words = []

        ignored_words = {

            "the",
            "is",
            "are",
            "am",
            "was",
            "were",
            "i",
            "you",
            "he",
            "she",
            "it",
            "we",
            "they",
            "a",
            "an",
            "to",
            "of",
            "in",
            "on",
            "for",
            "my",
            "your",
            "our",
            "this",
            "that",
            "and",
            "or",
            "but",
            "with",
            "have",
            "has",
            "had"

        }
        for speaker,message,timestamp in conversations:

            for word in message.lower ().split ():

                cleaned = (
                    word.strip (".,!?;:'\"()[]{}")
                )

                if len (cleaned) < 3:
                    continue

                if cleaned in ignored_words:
                    continue

                words.append (cleaned)

        counter = Counter(words)

        top_topics = [

            topic

            for topic,count

            in counter.most_common (10)
        ]

        summary = (
            f"I have analyzed "
            f"{len (conversations)} conversation(s). "
            f"The most discussed topics are: "
            f"{', '.join (top_topics)}."
        )

        return {

            "summary": summary,

            "top_topics": top_topics,

            "conversation_count": len(conversations)
        }
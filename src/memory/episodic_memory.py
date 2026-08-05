"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Episodic Memory

Description: Stores and retrieves important life events experienced by the user.

Responsibilities:
    - Detect important events
    - Store life experiences
    - Retrieve recent events
    - Support future timeline generation

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

class Episodic_Memory:

    def __init__ (self,database):

        self.database = database

    # ---------------------------------------------------------
    # Detect whether a message describes an important event
    # ---------------------------------------------------------

    def detect_episode_function (self,user_message):

        message = user_message.lower()

        event_keywords = [

            "completed",
            "finished",
            "started",
            "joined",
            "won",
            "lost",
            "graduated",
            "received",
            "built",
            "created",
            "published",
            "launched",
            "internship",
            "hackathon",
            "project"
        ]
        for keyword in event_keywords:

            if keyword in message:

                return True

        return False

    # ---------------------------------------------------------
    # Store an episode
    # ---------------------------------------------------------

    def store_episode_function (

        self,

        event,

        emotion = "neutral",

        importance = 0.75,

        event_date = None

    ):

        self.database.save_episode_function (

            event = event,

            emotion = emotion,

            importance = importance,

            event_date = event_date
        )

    # ---------------------------------------------------------
    # Retrieve recent episodes
    # ---------------------------------------------------------

    def retrieve_recent_episodes_function (

        self,

        limit = 5

    ):

        return self.database.get_recent_episodes_function (limit)

    # ---------------------------------------------------------
    # Build episode summary
    # ---------------------------------------------------------

    def build_episode_summary_function (

        self,

        limit=5

    ):

        episodes = self.retrieve_recent_episodes_function (limit)

        if not episodes:

            return "No important life events stored."

        summary = []

        for event,emotion, importance, event_date in episodes:

            line = f"• {event}"

            if event_date:

                line += f" ({event_date})"

            line += f" | Emotion: {emotion}"

            summary.append (line)

        return "\n".join (summary)
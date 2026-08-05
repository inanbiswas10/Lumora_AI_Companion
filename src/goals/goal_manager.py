"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Goal Manager

Description: Tracks the user's long-term goals and allows Lumora to monitor progress.

Responsibilities:
    - Detect goals from conversation
    - Store goals
    - Update goal status
    - Retrieve active goals

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""


class Goal_Manager:

    def __init__ (self,database):

        self.database = database

        self.goal_patterns = [

            "i want to",
            "my goal is",
            "i will",
            "i'm going to",
            "i plan to",
            "i dream of",
            "my ambition is"
        ]

    # ---------------------------------------------------------

    def detect_goal_function (self,user_message):

        message = user_message.lower ()

        for pattern in self.goal_patterns:

            if pattern in message:

                return user_message.strip ()

        return None

    # ---------------------------------------------------------

    def process_goal_function (self,user_message):

        goal = self.detect_goal_function (user_message)

        if goal is None:
            return

        self.database.save_goal_function (
            goal = goal,
            status = "Active"
        )

    # ---------------------------------------------------------

    def get_active_goals_function (self):

        return self.database.get_active_goals_function ()
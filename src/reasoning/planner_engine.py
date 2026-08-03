"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Planner Engine

Description: Creates an internal response strategy before Lumora replies.

Responsibilities:
    - Decide the response goal
    - Decide whether to ask follow-up questions
    - Decide whether to create reminders
    - Decide future conversation actions

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""
class Planner_Engine:

    def create_plan_function (self,user_message,emotion,decision):

        plan = {

            "goal": "respond",
            "ask_follow_up": False,
            "create_reminder": False
        }
        if emotion in ["sad","anxious","stressed"]:
            plan ["goal"] = "support"
            plan ["ask_follow_up"] = True

        if decision ["create_episode"]:
            plan["create_reminder"] = True
        return plan
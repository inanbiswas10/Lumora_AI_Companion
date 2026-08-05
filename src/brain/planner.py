"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Planner

Description: Creates and manages user goals and action plans.

Responsibilities:
    - Detect goals
    - Break goals into steps
    - Track progress
    - Suggest next actions
    - Prepare for future scheduling

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""


class Planner:

    def __init__ (self):

        self.goal_keywords = [

            "want to",
            "would like to",
            "my goal is",
            "i plan to",
            "i am planning to",
            "i'm planning to",
            "i need to",
            "i wish to",
            "i hope to"
        ]


    def detect_goal_function (
        self,
        user_message
    ):

        message = user_message.lower ().strip ()

        for keyword in self.goal_keywords:

            if keyword in message:

                goal = message.split (keyword,1)[1].strip ()

                if goal:

                    return goal
        return None


    def create_plan_function (
        self,
        goal
    ):

        goal = goal.lower ()

        # -------------------------------------------------
        # AI / Machine Learning
        # -------------------------------------------------

        if "ai" in goal or "artificial intelligence" in goal:

            return [

                "Learn Python thoroughly",

                "Master Data Structures & Algorithms",

                "Study Machine Learning",

                "Study Deep Learning",

                "Build AI Projects",

                "Practice MLOps",

                "Prepare for AI interviews"

            ]

        # -------------------------------------------------
        # Software Engineering
        # -------------------------------------------------

        if "software engineer" in goal:

            return [

                "Master DSA",

                "Learn System Design",

                "Build Full Stack Projects",

                "Learn Git & GitHub",

                "Practice Coding Interviews",

                "Apply for internships"

            ]

        # -------------------------------------------------
        # Data Science
        # -------------------------------------------------

        if "data scientist" in goal:

            return [

                "Learn Python",

                "Learn Statistics",

                "Learn SQL",

                "Learn Machine Learning",

                "Practice Data Analysis",

                "Build Portfolio Projects"

            ]

        # -------------------------------------------------
        # Generic Goal
        # -------------------------------------------------

        return [

            "Understand the goal",

            "Research the topic",

            "Create a learning roadmap",

            "Practice consistently",

            "Review progress weekly"

        ]


    def suggest_next_step_function (
        self,
        completed_steps,
        plan
    ):

        if completed_steps >= len (plan):

            return "Congratulations !! Goal completed successfully."

        return plan [completed_steps]


    def build_goal_summary_function (
        self,
        goal
    ):

        plan = self.create_plan_function (goal)

        summary = {

            "goal": goal,

            "total_steps": len (plan),

            "steps": plan
        }
        return summary
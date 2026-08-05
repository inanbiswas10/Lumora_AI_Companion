"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Learning Engine

Description: Allows Lumora to continuously learn from conversations, user feedback and interaction patterns.

Responsibilities:
    - Learn user preferences
    - Learn from corrections
    - Track frequently discussed topics
    - Store learned knowledge
    - Build personalized behaviour
    - Prepare future reinforcement learning

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

class Learning_Engine:

    def __init__ (self):

        self.user_preferences = {}

        self.topic_counter = {}

        self.user_feedback = []

    # --------------------------------------------------------

    def learn_preference_function (

        self,

        key,

        value

    ):

        self.user_preferences [key] = value

    # --------------------------------------------------------

    def get_preference_function (

        self,

        key

    ):

        return self.user_preferences.get (key)

    # --------------------------------------------------------

    def record_topic_function (

        self,

        topic

    ):

        topic = topic.lower ()

        if topic not in self.topic_counter:

            self.topic_counter [topic] = 0

        self.topic_counter [topic] += 1

    # --------------------------------------------------------

    def get_top_topics_function (

        self,

        limit = 10

    ):

        return sorted (

            self.topic_counter.items (),

            key = lambda item: item [1],

            reverse = True

        )[:limit]

    # --------------------------------------------------------

    def learn_from_feedback_function (

        self,

        feedback

    ):

        self.user_feedback.append (feedback)

    # --------------------------------------------------------

    def get_feedback_history_function (self):

        return self.user_feedback

    # --------------------------------------------------------

    def build_learning_prompt_function (self):

        prompt = "Learned User Preferences\n\n"

        if not self.user_preferences:

            prompt += "None\n"

        else:

            for key,value in self.user_preferences.items ():

                prompt += f"{key} : {value}\n"

        prompt += "\nFrequently Discussed Topics\n\n"

        topics = self.get_top_topics_function ()

        if not topics:

            prompt += "None\n"

        else:

            for topic,count in topics:

                prompt += f"{topic} ({count})\n"

        return prompt
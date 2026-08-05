"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Prompt Builder

Description: Builds the complete prompt sent to the language model.

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""


class Prompt_Builder:

    def __init__ (self,personality_engine):

        self.personality_engine = personality_engine

    def build_prompt_function (
        self,
        user_message,
        context
    ):

        system_prompt = (
            self.personality_engine
            .build_system_prompt_function ()
        )

        profile = context.get ("profile",{})

        memories = context.get ("memories",[])

        recent_messages = context.get (
            "recent_messages",
            []
        )

        episodes = context.get (
            "episodes",
            []
        )

        emotion = context.get (
            "emotion",
            "neutral"
        )

        profile_text = ""

        if profile:

            for key,value in profile.items ():

                profile_text += f"{key}: {value}\n"

        else:

            profile_text = "No stored profile."

        memory_text = ""

        if memories:

            for memory in memories:

                if isinstance (memory,tuple):

                    memory_text += f"- {memory [1]}\n"

                else:

                    memory_text += f"- {memory}\n"

        else:

            memory_text = "No relevant memories."

        conversation_text = ""

        if recent_messages:

            for speaker,message in recent_messages:

                conversation_text += (
                    f"{speaker}: {message}\n"
                )

        else:

            conversation_text = "No previous conversation."

        episode_text = ""

        if episodes:

            for event in episodes:

                episode_text += (
                    f"- {event}\n"
                )

        else:

            episode_text = "No episodes stored."

        prompt = f"""
{system_prompt}

==================================================
KNOWN USER PROFILE
==================================================

{profile_text}

==================================================
RELEVANT LONG-TERM MEMORIES
==================================================

{memory_text}

==================================================
RECENT CONVERSATION
==================================================

{conversation_text}

==================================================
RECENT EPISODES
==================================================

{episode_text}

==================================================
CURRENT EMOTION
==================================================

{emotion}

==================================================
IMPORTANT RULES
==================================================

Only use memories that appear above.

Never claim to remember something that is
not provided in the context.

If information is unknown,
say you don't know instead of inventing it.

Stay consistent with previous conversations.

==================================================
CURRENT USER MESSAGE
==================================================

{user_message}

==================================================

Respond naturally as Lumora.
"""

        return prompt
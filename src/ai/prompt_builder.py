"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Prompt Builder

Description: Builds the complete prompt that is sent to the language model.

Responsibilities:
    - Combine personality
    - Combine user profile
    - Combine memories
    - Combine recent conversation
    - Combine emotion
    - Add current message

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

        recent_messages = context.get ("recent_messages",[])

        emotion = context.get ("emotion","neutral")

        # ---------- Format User Profile ----------

        if profile:

            profile_text = "\n".join (
                f"{key}: {value}"
                for key,value in profile.items ()
            )

        else:

            profile_text = "No user profile available."

        # ---------- Format Memories ----------

        if memories:

            memory_text = "\n".join (memories)

        else:

            memory_text = "No relevant memories."

        # ---------- Format Recent Conversation ----------

        if recent_messages:

            conversation_text = "\n".join (
                f"{speaker}: {message}"
                for speaker,message in recent_messages
            )

        else:

            conversation_text = "No previous conversation."

        prompt = f"""
{system_prompt}

================================================

USER PROFILE

{profile_text}

================================================

RELEVANT MEMORIES

{memory_text}

================================================

RECENT CONVERSATION

{conversation_text}

================================================

CURRENT USER EMOTION

{emotion}

================================================

CURRENT USER MESSAGE

{user_message}

================================================

Instructions:

- Reply naturally as Lumora.
- Remember the user's profile and memories.
- Keep responses warm, intelligent and supportive.
- Never repeat the entire prompt.
- Respond conversationally.

Lumora:
"""

        return prompt
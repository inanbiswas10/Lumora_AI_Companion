"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Prompt Builder

Description: Builds the complete prompt sent to the language model.

Responsibilities:
    - Add Lumora's personality
    - Add user profile
    - Add relevant memories
    - Add recent conversation
    - Add emotion
    - Add episodic memories
    - Add current user message

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""


class Prompt_Builder:

    def __init__ (self,personality_engine):

        self.personality_engine = personality_engine

    # ---------------------------------------------------------

    def build_prompt_function (
        self,
        user_message,
        context
    ):

        system_prompt = (
            self.personality_engine
            .build_system_prompt_function ()
        )

        profile = context.get (
            "profile",
            {}
        )

        memories = context.get (
            "memories",
            []
        )

        recent_messages = context.get (
            "recent_messages",
            []
        )

        emotion = context.get (
            "emotion",
            "neutral"
        )

        confidence = context.get (
            "confidence",
            0.0
        )

        episodes = context.get (
            "episodes",
            []
        )

        # -------------------------------------------------
        # User Profile
        # -------------------------------------------------

        profile_text = ""

        if profile:

            for key,value in profile.items ():

                profile_text += (
                    f"{key}: {value}\n"
                )

        else:

            profile_text = "No profile information available."

        # -------------------------------------------------
        # Relevant Memories
        # -------------------------------------------------

        memory_text = ""

        if memories:

            for memory in memories:

                memory_text += f"- {memory}\n"

        else:

            memory_text = "No relevant memories."

        # -------------------------------------------------
        # Recent Conversation
        # -------------------------------------------------

        conversation_text = ""

        if recent_messages:

            for speaker, message in recent_messages:

                conversation_text += (
                    f"{speaker}: {message}\n"
                )

        else:

            conversation_text = (
                "No recent conversation."
            )

        # -------------------------------------------------
        # Episodes
        # -------------------------------------------------

        episode_text = ""

        if episodes:

            for event,emotion_name,importance, date in episodes:

                episode_text += (
                    f"- {event} "
                    f"(Emotion: {emotion_name}, "
                    f"Importance: {importance})\n"
                )

        else:

            episode_text = "No episodic memories."

        # -------------------------------------------------
        # Final Prompt
        # -------------------------------------------------

        prompt = f"""
{system_prompt}

==========================================================
USER PROFILE
==========================================================

{profile_text}

==========================================================
RELEVANT MEMORIES
==========================================================

{memory_text}

==========================================================
RECENT CONVERSATION
==========================================================

{conversation_text}

==========================================================
RECENT EPISODES
==========================================================

{episode_text}

==========================================================
CURRENT EMOTION
==========================================================

Emotion: {emotion}
Confidence: {confidence}

==========================================================
CURRENT USER MESSAGE
==========================================================

{user_message}

==========================================================

Instructions:

- Respond as Lumora.
- Speak naturally.
- Use previous memories whenever relevant.
- Be emotionally intelligent.
- Never sound robotic.
- Keep the conversation engaging.
- If the user is sad, comfort them.
- If the user is excited, celebrate with them.
- Remember you are building a lifelong friendship.

Response:
"""

        return prompt
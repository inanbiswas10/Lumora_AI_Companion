"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Prompt Builder

Description: Builds the complete prompt that is sent to the Large Language Model.

Responsibilities:
    - Add Lumora personality
    - Add known user information
    - Add recent conversation
    - Add detected emotion
    - Add current user message

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

class Prompt_Builder:

    def build_prompt_function (self,user_profile,conversation_history,relevant_memories,emotion,user_message):

        prompt = """
You are Lumora AI.

You are an advanced AI companion created by Inan Biswas.

Your personality:
- Friendly
- Intelligent
- Professional
- Calm
- Supportive
- Honest

Always:
- Speak naturally.
- Give clear answers.
- Be encouraging.
- Never mention you are an LLM unless asked.
- Remember your name is Lumora.

"""

        # ----------------------------
        # User Profile
        # ----------------------------

        prompt += "\nKnown information about the user:\n"

        if user_profile:
            for key,value in user_profile.items ():
              label = key.replace ("_"," ").title ()
              prompt += f" - {label}: {value}\n"
        else:
            prompt += " - No information available.\n"

        # ----------------------------
        # Conversation History
        # ----------------------------

        prompt += "\nRecent Conversation:\n\n"

        if conversation_history:
            for speaker,message in conversation_history:
                prompt += f"{speaker}: {message}\n"
        else:
            prompt += "No previous conversation.\n"

        # ----------------------------
        # Relevant Memories
        # ----------------------------

        prompt += "\nRelevant Memories:\n\n"

        if relevant_memories:
            for memory in relevant_memories:
                prompt += f" - {memory}\n"

        else:
            prompt += "No relevant memories found.\n"

        # ----------------------------
        # Emotion
        # ----------------------------

        prompt += f"\nDetected Emotion: {emotion}\n"

        # ----------------------------
        # Current Message
        # ----------------------------

        prompt += f"\nCurrent User Message:\n{user_message}\n\n"
        prompt += "Lumora:"
        return prompt
"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Context Manager

Description: Collects every piece of information required before Lumora generates a response.

Responsibilities:
    - Retrieve user profile
    - Retrieve recent conversations
    - Retrieve semantic memories
    - Retrieve episodic memories
    - Retrieve learned preferences
    - Retrieve relationships
    - Retrieve knowledge
    - Detect emotions

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

class Context_Manager:

    def __init__ (
        self,
        database,
        memory_manager,
        emotion_detector,
        knowledge_engine = None,
        learning_engine = None,
        relationship_manager = None,
        personality_evolution = None
    ):

        self.database = database
        self.memory_manager = memory_manager
        self.emotion_detector = emotion_detector

        self.knowledge_engine = knowledge_engine
        self.learning_engine = learning_engine
        self.relationship_manager = relationship_manager
        self.personality_evolution = personality_evolution

    # ---------------------------------------------------------

    def build_context_function (self,user_message):

        # ---------------- Emotion ----------------

        emotion = self.emotion_detector.detect_emotion_function (user_message)

        confidence = 1.0

        # ---------------- User Profile ----------------

        profile = self.database.get_all_user_profile_function ()

        # ---------------- Recent Conversation ----------------

        recent_messages = (
            self.database.get_recent_messages_function (10)
        )

        # ---------------- Relevant Memories ----------------

        memories = (
            self.memory_manager.retrieve_relevant_memories_function (
                user_message
            )
        )

        # ---------------- Episodic Memory ----------------

        episodes = (
            self.database.get_recent_episodes_function ()
        )

        # ---------------- Knowledge ----------------

        knowledge = ""

        if self.knowledge_engine:

            knowledge = (
                self.knowledge_engine.retrieve_knowledge_function (
                    user_message
                )
            )

        # ---------------- Learned Preferences ----------------

        learned_preferences = {}

        if self.learning_engine:

            learned_preferences = (
                self.learning_engine.user_preferences
            )

        # ---------------- Relationships ----------------

        relationships = []

        if self.relationship_manager:

            try:

                relationships = (
                    self.relationship_manager
                    .get_all_relationships_function ()
                )

            except AttributeError:

                relationships = []

        # ---------------- Personality ----------------

        personality_state = {}

        if self.personality_evolution:

            try:

                personality_state = (
                    self.personality_evolution
                    .get_current_personality_function ()
                )

            except AttributeError:

                personality_state = {}

        # ---------------- Return Complete Context ----------------

        return {

            "emotion": emotion,

            "confidence": confidence,

            "profile": profile,

            "recent_messages": recent_messages,

            "memories": memories,

            "episodes": episodes,

            "knowledge": knowledge,

            "learned_preferences": learned_preferences,

            "relationships": relationships,

            "personality_state": personality_state
        }
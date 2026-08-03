"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Conversation Pipeline

Description: Coordinates the complete processing flow of a user message.

Responsibilities:
    - Detect emotion
    - Extract memories
    - Calculate importance
    - Make memory decisions
    - Retrieve memories
    - Build context for the LLM

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""
class Conversation_Pipeline:

    def __init__ (self,emotion_detector,memory_extractor,importance_analyzer,memory_decision_engine,semantic_retriever):

        self.emotion_detector = emotion_detector
        self.memory_extractor = memory_extractor
        self.importance_analyzer = importance_analyzer
        self.memory_decision_engine = memory_decision_engine
        self.semantic_retriever = semantic_retriever

    def process_message_function (self,user_message):
        emotion = self.emotion_detector.detect_emotion_function (user_message)
        memory = self.memory_extractor.extract_information_function (user_message)
        importance = self.importance_analyzer.calculate_importance_function (user_message)
        decision = self.memory_decision_engine.analyze_function (user_message,importance)
        return {

            "emotion": emotion,
            "memory": memory,
            "importance": importance,
            "decision": decision
        }
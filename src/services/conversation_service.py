"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Conversation Service

Description: Handles the business logic for processing user conversations.

Responsibilities:
    - Coordinate memory extraction
    - Coordinate memory recall
    - Generate AI responses
    - Save conversation history

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""
from src.ai.summarizer import Conversation_Summarizer
from src.ai.emotion_detector import Emotion_Detector
from src.llm.groq_provider import Groq_Provider
from src.utils.response_formatter import Response_Formatter
from src.prompt.prompt_builder import Prompt_Builder

class Conversation_Service:
    
    # Handles conversation processing.

    def __init__ (self,database,ai_engine,memory_extractor,memory_recall,semantic_memory,conversation_memory,memory_retriever):

      self.database = database
      self.ai_engine = ai_engine
      self.memory_extractor = memory_extractor
      self.memory_recall = memory_recall
      self.semantic_memory = semantic_memory
      self.conversation_memory = conversation_memory
      self.memory_retriever = memory_retriever
      self.summarizer = Conversation_Summarizer ()
      self.emotion_detector = Emotion_Detector ()
      self.prompt_builder = Prompt_Builder ()
      self.groq_provider = Groq_Provider ()
      self.response_formatter = Response_Formatter ()

    def process_message_function (self,user_message):
        
      # Process a user message and return Lumora's response.

      friendly_labels = {

          "name":"your name",
          "favorite_colour":"your favourite colour",
          "university":"your university",
          "workplace":"your workplace",
          "hobby":"your hobby",
          "interest":"your interest"
      }
      # Save the user's message
      self.database.save_message_function ("User",user_message)
      if self.conversation_memory.should_store_function (user_message):
          self.database.save_conversation_memory_function (user_message)
          print (f"[Memory] Conversation saved.")

      # -----------------------------
      # Memory Extraction
      # -----------------------------
      memory = self.memory_extractor.extract_information_function (user_message)
      if memory:
        key,value = memory
        self.database.save_user_profile_function (key,value)
        label = friendly_labels.get (key,key.replace ("_"," "))

        response = f"Thank you so much for telling me !! I will remember."
        self.database.save_message_function ("Lumora", response)

        return response
      # -----------------------------
      # Memory Recall
      # -----------------------------
      recall_key = self.memory_recall.recall_information_function (user_message)

      if recall_key:

        value = self.database.get_user_profile_function (recall_key)

        label = friendly_labels.get (recall_key,recall_key.replace ("_"," "))

        if value:
            response = f"Your {label} is {value}."
        else:
            response = f"I don't know {label} yet."

        self.database.save_message_function ("Lumora",response)
        return response

      history_queries = [

          "what did we talk about",
          "show conversation history",
          "show history",
          "conversation history",
          "recent conversation"
      ]
      if user_message.lower ().strip () in history_queries:
          
          history = self.database.get_recent_messages_function ()

          if not history:
              return "We haven't talked yet."

          response = "Here are our recent conversations:\n\n"
          print ()
          for sender,message in history:
            response += f"{sender}: {message}\n"
            print ()
          return response

      summary_queries = [

          "summarize our conversation",
          "summarize our last conversation",
          "conversation summary",
          "summary"
      ]  
      if user_message.lower ().strip () in summary_queries:

         history = self.database.get_recent_messages_function ()
         return self.summarizer.summarize_function (history)

      user_profile = {}

      profile_keys = [
          "name",
          "favorite_colour",
          "university",
          "workplace",
          "hobby",
          "interest"
      ]
      for key in profile_keys:
          value = self.database.get_user_profile_function (key)
          if value:
              user_profile [key] = value

      emotion = self.emotion_detector.detect_emotion_function (user_message)
    #   print (f"[Emotion] Detected Emotion: {emotion}")
    #   print ()

      # -----------------------------
      # AI Engine
      # -----------------------------
      conversation_history = self.database.get_recent_messages_function (limit = 10)
      relevant_memories = self.memory_retriever.retrieve_memories_function ()
      prompt = self.prompt_builder.build_prompt_function (user_profile = user_profile,conversation_history = conversation_history,relevant_memories = relevant_memories,emotion = emotion,user_message = user_message)
      response = self.groq_provider.generate_response_function (prompt)
      response = self.response_formatter.format_response_function (response)
      self.database.save_message_function ("Lumora",response)
      return response
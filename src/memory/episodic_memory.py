"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Episodic Memory

Description: Stores important life events and experiences shared by the user.

Responsibilities:
    - Store experiences
    - Retrieve experiences
    - Support future reflections

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""
class Episodic_Memory:
    def __init__ (self,database):
        self.database = database

    def store_episode_function (self,event,emotion,importance,event_date):
       self.database.save_episode_function (event,emotion,importance,event_date)

    def retrieve_recent_episodes_function (self):
       return self.database.get_recent_episodes_function ()
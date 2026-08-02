"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: LLM Provider

Description: Acts as the communication layer between Lumora AI and external language models.

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

class LLM_Provider:
    
    # Base interface for all language models.

    def generate_response_function (self,prompt):
        raise NotImplementedError ("Subclasses must implement generate_response_function () !!")
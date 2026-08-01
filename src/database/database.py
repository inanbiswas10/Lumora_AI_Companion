"""
=========================================================================
                            Lumora AI
-------------------------------------------------------------------------

Module: Database Manager

Description: This module manages all database-related operations.

Responsibilities:
    - Store conversation history
    - Save user preferences
    - Manage persistent data
    - Handle database connections

Author: Inan Biswas
Project: Lumora AI
=========================================================================
"""

import sqlite3
from pathlib import Path
from datetime import datetime

class Database_Manager:

    # Handles all database operations for Lumora AI.

    def __init__ (self):

        # Initialize the database connection.

        database_path = Path ("data")/"lumora.db"

        self.connection = sqlite3.connect (database_path)

        self.cursor = self.connection.cursor ()

        print (f"[Database] Database connected successfully !!")
        print ()

    def create_tables_function (self):

        # Create all required database tables.
        
        self.cursor.execute ("""
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            speaker TEXT NOT NULL,
            message TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)

        self.connection.commit ()

        print (f"[Database] Tables created successfully !!")
        print ()

    def save_message_function (self,speaker:str,message:str):

        #Save a conversation message to the database.

        current_time = datetime.now ().strftime ("%Y-%m-%d %H:%M:%S")

        self.cursor.execute (
        """
        INSERT INTO conversations (speaker,message,timestamp)
        VALUES (?,?,?)
        """,
        (speaker,message,current_time)
    )

        self.connection.commit ()

        print (f"[Database] Message saved ({speaker}) !!")
        print ()

    def close (self):

        # Close the database connection.

        self.connection.close ()

        print (f"[Database] Database connection closed !!")
        print ()

    
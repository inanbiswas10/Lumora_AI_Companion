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
import json
from pathlib import Path
from datetime import datetime

class Database_Manager:

    def save_embedding_function (self,memory_id,embedding):

        timestamp = datetime.now ().strftime ("%Y-%m-%d %H:%M:%S")

        query = """
            INSERT INTO memory_embeddings
            (memory_id, embedding, created_at)

            VALUES (?, ?, ?)
        """

        embedding_json = json.dumps (embedding)

        self.cursor.execute (query,(memory_id,embedding_json,timestamp)
        )
        self.connection.commit ()

    def get_embedding_function (self,memory_id):
        import json

        query = """
            SELECT embedding
            FROM memory_embeddings
            WHERE memory_id = ?
        """
        self.cursor.execute (query,(memory_id,))
        row = self.cursor.fetchone ()

        if row:
            return json.loads (row [0])
        return None


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
        self.cursor.execute ("""
        CREATE TABLE IF NOT EXISTS user_profile (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            key TEXT UNIQUE NOT NULL,

            value TEXT NOT NULL

        )
        """)
        self.cursor.execute ("""
        CREATE TABLE IF NOT EXISTS conversation_memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            memory TEXT NOT NULL,
            importance INTEGER DEFAULT 5,
            created_at TEXT NOT NULL
        )
        """)
        self.cursor.execute ("""
        CREATE TABLE IF NOT EXISTS memory_embeddings (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        memory_id INTEGER NOT NULL,

        embedding TEXT NOT NULL,

        created_at TEXT NOT NULL,

        FOREIGN KEY (memory_id)
            REFERENCES conversation_memories(id)
        )
        """)

        self.cursor.execute ("""
        CREATE TABLE IF NOT EXISTS episodes (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            event TEXT NOT NULL,

            emotion TEXT NOT NULL,

            importance REAL NOT NULL,

            event_date TEXT,

            created_at TEXT NOT NULL
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

        # print (f"[Database] Message saved ({speaker}) !!")
        # print ()

    def get_all_messages_function (self):

        # Retrieve all stored conversations from the database.

        self.cursor.execute ("""
        SELECT speaker,message,timestamp
        FROM conversations
        ORDER BY id ASC
    """)

        return self.cursor.fetchall ()

    def save_user_profile_function (self,key,value):

        # Save or update a user profile entry.

        self.cursor.execute (
            """
            INSERT OR REPLACE INTO user_profile (key,value)
            VALUES (?,?)
           """,
           (key,value)
        ) 
        self.connection.commit ()

    def get_user_profile_function (self,key):

        # Retrieve a user profile value using its key.

        self.cursor.execute (
            """
            SELECT value
            FROM user_profile
            WHERE key = ?
            """,
            (key,)
        )
        result = self.cursor.fetchone ()

        if result:
            return result [0]
        return None

    def get_recent_messages_function (self,limit = 10):
        
        # Retrieve the most recent conversation messages.

        query = """
            SELECT speaker,message
            FROM conversations
            ORDER BY id DESC
            LIMIT ?
        """
        self.cursor.execute (query,(limit,))
        rows = self.cursor.fetchall ()
        rows.reverse ()
        return rows

    def get_all_user_profile_function (self):

        """
        Returns the complete user profile
        as a dictionary.
        """

        self.cursor.execute ("""

            SELECT key,value
            FROM user_profile

        """)
        rows = self.cursor.fetchall ()
        profile = {}
        for key,value in rows:
            profile [key] = value
        return profile

    def save_conversation_memory_function (self,memory,importance = 5):
        timestamp = datetime.now ().strftime ("%Y-%m-%d %H:%M:%S")

        query = """
        INSERT INTO conversation_memories
        (memory,importance,created_at)

            VALUES (?,?,?)
        """

        self.cursor.execute (query,(memory,importance,timestamp))
        self.connection.commit ()
        return self.cursor.lastrowid

    def get_conversation_memories_function (self):

        query = """
            SELECT memory
            FROM conversation_memories
            ORDER BY id DESC
        """

        self.cursor.execute (query)

        rows = self.cursor.fetchall ()

        return [row [0] for row in rows]

    def get_all_embeddings_function (self):

        query = """
            SELECT
                conversation_memories.id,
                conversation_memories.memory,
                memory_embeddings.embedding

            FROM conversation_memories
            JOIN memory_embeddings
            ON conversation_memories.id = memory_embeddings.memory_id
        """
        self.cursor.execute (query)
        import json
        rows = self.cursor.fetchall ()

        return [
            (
                 row [0],          # memory id
                 row [1],          # memory text
                 json.loads (row[2])
            )
            for row in rows
        ]

    def save_episode_function (self,event,emotion,importance,event_date):

        created_at = datetime.now ().strftime ("%Y-%m-%d %H:%M:%S")
        self.cursor.execute (
            """
            INSERT INTO episodes
            (event,emotion,importance,event_date,created_at)

            VALUES (?,?,?,?,?)
            """,
            (
                event,
                emotion,
                importance,
                event_date,
                created_at
            )
        )
        self.connection.commit ()

    def get_recent_episodes_function (self,limit = 10):

        self.cursor.execute (
            """
            SELECT
                event,
                emotion,
                importance,
                event_date

            FROM episodes
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,)
        )
        return self.cursor.fetchall ()
    
        self.database.save_episode_function (event = "Completed AI assignment",emotion = "happy",importance = 0.92,event_date = "2026-08-03")
        episodes = self.database.get_recent_episodes_function ()
        print (f"{episodes}")

    def close (self):

        # Close the database connection.

        self.connection.close ()

        print (f"[Database] Database connection closed !!")
        print ()

    
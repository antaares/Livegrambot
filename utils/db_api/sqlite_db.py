import sqlite3
from datetime import datetime

class Database:
    _now = datetime.now()
    base_date = _now.strftime("%Y-%m-%d")
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)
        

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        # connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
            id int primary key NOT NULL,
            Name varchar(255) NOT NULL
            );
"""
        self.execute(sql, commit=True)

    def create_messages_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Messages(
            chat_id int NOT NULL,
            message_id int NOT NULL,
            push_date datetime NOT NULL
        );
        """
        self.execute(sql, commit=True)
    
    def create_table_banned_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS BannedUsers (
            id int primary key NOT NULL
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())


    def add_user(self, id: int, name: str):
        sql = """
        INSERT or IGNORE INTO Users(id, Name) VALUES(?, ?)
        """
        self.execute(sql, parameters=(id, name,), commit=True)

    def add_message(self, chat_id: int, message_id: int, push_date: str):
        sql = """
        INSERT INTO Messages(chat_id, message_id, push_date) VALUES(?, ?, ?)
        """
        self.execute(sql, parameters=(chat_id, message_id, push_date), commit=True)
    

    def get_message_chat_id(self, message_id: int):
        sql = """
        SELECT chat_id FROM Messages WHERE message_id = ?
        """
        return self.execute(sql, parameters=(message_id,), fetchone=True)[0]
    
    def add_banned_user(self, id: int):
        sql = """
        INSERT or IGNORE INTO BannedUsers(id) VALUES(?)
        """
        self.execute(sql, parameters=(id,), commit=True)
    
    def is_banned_user(self, id: int):
        sql = """
        SELECT id FROM BannedUsers WHERE id = ?
        """
        return self.execute(sql, parameters=(id,), fetchone=True) is not None
    
    def remove_banned_user(self, id: int):
        sql = """
        DELETE FROM BannedUsers WHERE id = ?
        """
        self.execute(sql, parameters=(id,), commit=True)
    
    def delete_old_messages(self):
        import datetime
        prev = datetime.datetime.today() - datetime.timedelta(days=15)
        prev_date = prev.strftime("%Y-%m-%d")
        sql = """
        DELETE FROM Messages WHERE push_date BETWEEN ? and ?
        """
        # print("Deleting old messages")
        self.execute(sql, parameters=(self.base_date, prev_date,), commit=True)
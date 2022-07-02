import sqlite3
import atexit

from user import *

class DatabaseAccess:
    # singleton pattern creation
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseAccess, cls).__new__(cls)
            cls._instance._init()
            atexit.register(cls._instance._exit)
        return cls._instance

    # singleton initialiser
    def _init(self):
        self._db_connection = sqlite3.connect('./data/user.db')
        self._db_cursor = self._db_connection.cursor()
        self._user = None

    # singleton destructor
    def _exit(self):
        self._db_cursor.close()
        self._db_connection.close()

    def create_account(self, username, password):
        # return types:
        # 0 = everything ok
        # -1 = problem with username
        # -2 = problem with password
        # -3 = already logged in

        if self._user is not None:
            return -3

        # check if username or password have atleast
        # one charecter
        if len(username) < 1:
            return -1
        elif len(password) < 1:
            return -2
        
        # check if account already exists
        if (len(self._db_cursor.execute(f'''
        SELECT user_id
        FROM Users
        WHERE username ="{username}"
        ''').fetchall()) != 0):
            return -1
        
        # create user object
        self._user = User(username, password)

        # create user record
        self._db_cursor.execute(f'''
        INSERT INTO Users(username, user_salt, password_hash, user_text)
        VALUES("{self._user.username}", "{self._user.user_salt}", "{self._user.password_hash}", "{self._user.user_text}")
        ''')
        self._db_connection.commit()

        return 0
    
    def log_in(self, username, password):
        # return types:
        # 0 = everything ok
        # -1 = problem with username
        # -2 = problem with password
        # -3 = already logged in

        if self._user is not None:
            return -3

        # check if username or password have atleast
        # one charecter
        if len(username) < 1:
            return -1
        elif len(password) < 1:
            return -2

        # check if this account doesn't exist
        user_data = self._db_cursor.execute(f'''
        SELECT password_hash, user_salt, user_text
        FROM Users
        WHERE username ="{username}"
        ''').fetchall()
        if (len(user_data) == 0):
            return -1

        # re-create user object
        self._user = User(username, password, user_data[0][1], user_data[0][2])

        # check if password hashes match
        if self._user.password_hash != user_data[0][0]:
            self._user = None
            return -2

        return 0

    def log_out(self):
        # return types:
        # 0 = everything ok
        # -1 = not logged in to begin with

        if self._user is None:
            return -1
        
        self._user = None
        return 0

    def delete_account(self):
        # return types:
        # 0 = everything ok
        # -1 = not logged in to begin with

        # login check
        if self._user is None:
            return -1

        # delete account from database
        self._db_cursor.execute(f'''
        DELETE FROM Users
        WHERE username = "{self._user.username}"
        ''')
        self._db_connection.commit()

        # log out one last time
        self.log_out()

        return 0
        
    def write_text_changes(self, new_user_text):
        # return types:
        # 0 = everything ok
        # -1 = not logged in

        # login check
        if self._user is None:
            return -1

        # set user text
        self._user.set_user_text(new_user_text)

        # update database
        self._db_cursor.execute(f'''
        UPDATE Users
        SET user_text = "{self._user.user_text}"
        WHERE username = "{self._user.username}"
        ''')
        self._db_connection.commit()

        return 0

    def read_plaintext(self):
        # return types:
        # text = everything ok
        # -1 = not logged

        # login check
        if self._user is None:
            return -1

        return self._user.get_user_text()
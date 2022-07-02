import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
from hashlib import sha256

class User:
    def __init__(self, username, password, user_salt=None, user_text=None):
        self.username = username
        
        self.password = password
        
        if user_salt is None:
            self.user_salt = base64.urlsafe_b64encode(os.urandom(16)).decode()
        else:
            self.user_salt = user_salt
        
        self.password_hash = sha256((self.user_salt+password).encode()).hexdigest()
        
        # derrive key
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=base64.urlsafe_b64decode(self.user_salt.encode()),
            iterations=100000,
            backend=default_backend()
        )
        self._key = base64.urlsafe_b64encode(kdf.derive(self.password.encode()))

        if user_text is None:
            self.set_user_text("")
        else:
            self.user_text = user_text
    
    # set new encrypted text from unencrypted text
    def set_user_text(self, user_text):
        # encrypt text
        fernet = Fernet(self._key)
        self.user_text = fernet.encrypt(user_text.encode()).decode()

    # get unencrypted text from current encrypted text
    def get_user_text(self):
        # decrypt text
        fernet = Fernet(self._key)
        return_text = fernet.decrypt(self.user_text.encode()).decode()

        return return_text


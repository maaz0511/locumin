# utils/encryption.py
from cryptography.fernet import Fernet
from flask import current_app

class Encryptor:
    @staticmethod
    def encrypt(data: str) -> str:
        if not data:
            return ''
        f = Fernet(current_app.config['ENCRYPTION_KEY'])
        return f.encrypt(data.encode()).decode()

    @staticmethod
    def decrypt(token: str) -> str:
        if not token:
            return ''
        f = Fernet(current_app.config['ENCRYPTION_KEY'])
        return f.decrypt(token.encode()).decode()
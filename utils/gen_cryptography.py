from cryptography.fernet import Fernet

from . import text


def generate_hashed_pword():
    raw_string = text.build_string()
    key = Fernet.generate_key()
    return encrypt(key, raw_string)


def encrypt(key, raw_string):
    plaintext = raw_string.encode()
    f = Fernet(key)
    hashed_string = f.encrypt(plaintext)
    return key, hashed_string


def decrypt(key, hashed_string):
    f = Fernet(key)
    plaintext = f.decrypt(hashed_string)
    raw_string = plaintext.decode()
    return raw_string

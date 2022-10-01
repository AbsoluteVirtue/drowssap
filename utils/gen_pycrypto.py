import binascii
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util import Counter
from Crypto import Random

import text

_key_bytes = 32


def generate_hashed_pword():
    raw_string = text.build_string()
    salt = Random.new().read(8)
    key = PBKDF2(raw_string, salt, _key_bytes)
    return encrypt(key, raw_string)


def encrypt(key, raw_string):
    assert len(key) == _key_bytes

    iv = Random.new().read(AES.block_size)

    iv_int = int(binascii.hexlify(iv), 16)

    ctr = Counter.new(AES.block_size * 8, initial_value=iv_int)

    aes = AES.new(key, AES.MODE_CTR, counter=ctr)

    hashed = aes.encrypt(raw_string)
    return iv, hashed


def decrypt(key, iv, hashed_string):
    assert len(key) == _key_bytes

    iv_int = int(iv.encode('hex'), 16)
    ctr = Counter.new(AES.block_size * 8, initial_value=iv_int)

    aes = AES.new(key, AES.MODE_CTR, counter=ctr)

    plaintext = aes.decrypt(hashed_string)
    return plaintext

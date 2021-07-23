from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from enrocrypt.hashing import Hashing
from enrocrypt.encryption import Encryption
from enrocrypt.error import KeyError

def generate_key(words:str,salt:bytes,bits:int = 32):
    '''`words` take the sentence of which you want to make the key of
    `salt` takes the salt you wnat to add in the key
    `bits` takes how many bits your key should be
    Note: higher the bit value, bigger the encrypted data
    Warning: Some Functions Only Support 128, 192, 256 bit key and some only do 256 bits
    Note: The `bits` value can't be bigger than 32 as in `cryptography` module bit are:
    * 256 bits = 32 bits
    * 192 bits = 24 bits
    * 128 bits = 16 bits'''
    bit = [16,24,32]
    if bits not in bit:
        raise KeyError(bits=bits)
    obj = Hashing()
    shared_key = obj.SHA256(words)
    drived_key = HKDF(
        algorithm=SHA256(),
        length=bits,
        salt=salt,
        info=b'salted key'
    ).derive(shared_key)
    return drived_key
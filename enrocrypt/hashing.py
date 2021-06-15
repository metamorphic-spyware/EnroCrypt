from enrocrypt.basic import seperator
import hashlib, base64, uuid
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends.interfaces import HashBackend
def Standard_Multi_Hash(Data:str):
    '''Inreversable Salted Hash Function Don't Use If U Want To Get The Content Back'''
    a = hashlib.sha256(); a.update(bytes(Data.encode())); b = []
    base = hashlib.sha512()
    md = hashlib.md5()
    b.append(str(a.digest()).split("'")[1])
    b[0] = str(base64.urlsafe_b64encode(bytes(b[0].encode()))).split("'")[1]
    base.update(bytes(b[0].encode()))
    md.update(base.digest())
    b[0]=str(base64.urlsafe_b64encode(base64.standard_b64encode(md.digest()))).split("'")[1]
    salt = ['H', 'c', 'D', 'L', 'b', 'M', 'S', 'a', 'N', 'q', 'K', 'j', 'V', 'd', 'O', 'W', 'x']
    c = (b[0].split("G"))or(b[0].split("g"))or(b[0].split("v"))or(b[0].split("x")); d=[]; e=[]
    for i in range(len(c)): a = salt[i]; b = c[i]; c[i] = b+a
    for i in range(len(c)):
        try: d.append(c[i+1])
        except: d.append(c[0])
        e.append(''.join(d))
        return(bytes(str(e[0]).encode()))

def _Salt(data):
    salt = []
    salt.append(str(hashlib.sha256(uuid.uuid4().bytes).digest()).split("'")[1])
    salt.append(str(data).split("'")[1])
    salt.append(str(hashlib.sha256(uuid.uuid4().bytes).digest()).split("'")[1])
    return bytes(''.join(salt).encode())
    
def SHA256(data:str):
    sha = hashlib.sha256(bytes(data.encode()))
    hash = sha.digest()
    return _Salt(hash)

def SHA512(data:str):
    sha = hashlib.sha512(bytes(data.encode()))
    hash = str(sha.digest())
    return _Salt(hash)

def SHA244(data:str):
    sha = hashlib.sha224(bytes(data.encode()))
    hash = str(sha.digest())
    return _Salt(hash)

def MD5(data:str):
    sha = hashlib.md5(bytes(data.encode()))
    hash = str(sha.digest())
    return _Salt(hash)

def SHA384(data:str):
    sha = hashlib.sha384(bytes(data.encode()))
    hash = str(sha.digest())
    return _Salt(hash)

def BLAKE2(data:bytes):
    a = hashes.Hash(hashes.BLAKE2s(32))
    a.update(data)
    return _Salt(a.finalize())
    
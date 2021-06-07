from enrocrypt.basic import seperator

def Standard_Multi_Hash(Data:str):
    '''Inreversable Salted Hash Function Don't Use If U Want To Get The Content Back'''
    import hashlib, base64
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

def _Salt(data:bytes):
    data_list = seperator(data)
    salt = ['xd\\','bb\\','xdd\\','0eh\\','9a\\','0fnb\\','s5g\\','d8r\\','0fg\\','m4f\\']
    for i in data_list:
        try:
            data_list.pop(len(i))
        except:
            data_list[0] = data_list[1]
    for i in salt:
        data_list.insert(len(i),i)
    data = ''.join(data_list)
    return data

def Standard_SHA256(data:str):
    import hashlib
    sha = hashlib.sha256(bytes(data.encode()))
    hash = str(sha.digest())
    return _Salt(hash)

def Standard_SHA512(data:str):
    import hashlib
    sha = hashlib.sha512(bytes(data.encode()))
    hash = str(sha.digest())
    return _Salt(hash)

def Standard_SHA244(data:str):
    import hashlib
    sha = hashlib.sha224(bytes(data.encode()))
    hash = str(sha.digest())
    return _Salt(hash)

def Standard_MD5(data:str):
    import hashlib
    sha = hashlib.md5(bytes(data.encode()))
    hash = str(sha.digest())
    return _Salt(hash)

def Standard_SHA384(data:str):
    import hashlib
    sha = hashlib.sha384(bytes(data.encode()))
    hash = str(sha.digest())
    return _Salt(hash)

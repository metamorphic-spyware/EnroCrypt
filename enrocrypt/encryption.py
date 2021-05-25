from .error import Error
def _Keyencryption(key:bytes):
    import base64
    bases = base64.standard_b64encode(key)
    baseu = base64.urlsafe_b64encode(bases)
    return baseu
def _Keydecryption(key:bytes):
    import base64
    bases = base64.standard_b64decode(key)
    baseu = base64.urlsafe_b64decode(bases)
    return baseu
def _dataencryption(data:bytes):
    import base64
    bases = base64.standard_b64encode(data)
    baseu = base64.urlsafe_b64encode(bases)
    return baseu
def _datadecryption(data:bytes):
    import base64
    baseu = base64.urlsafe_b64decode(data)
    bases = base64.standard_b64decode(baseu)
    return bases
def _BaseEncryption(text:bytes):
    from cryptography.fernet import Fernet
    key = Fernet.generate_key()
    f = Fernet(key)
    e = f.encrypt(text)
    return [key,e]
def _BaseDecryption(key:bytes,text:bytes):
    from cryptography.fernet import Fernet
    f = Fernet(key)
    e = f.decrypt(text)
    return e

def Encrypt(Data:bytes):
    basee = _BaseEncryption(Data)
    e_data = _dataencryption(basee[1])
    e_key = _Keyencryption(basee[0])
    final = []
    final.append('Key →');final.append(e_key);final.append('Encrypted Data →');final.append(e_data)
    return final
def Decrypt(Key:bytes,Encrypted_Data:bytes):
    d_key = _Keydecryption(Key)      
    d_data = _datadecryption(Encrypted_Data)
    based = _BaseDecryption(d_key,d_data)
    return based
def Decrypt_List(Data:list):
    '''Takes The List Returned By Encrypt Function "AS IS" Without Modification'''
    if 'Key →' and 'Encrypted Data →' not in Data:
        Error.ModifiedError()
    if len(Data) != 4:
        Error.ListIndexError()
    Key = Data[1]
    e_Data = Data[3]
    d_key = _Keydecryption(Key)      
    d_data = _datadecryption(e_Data)
    based = _BaseDecryption(d_key,d_data)
    return based
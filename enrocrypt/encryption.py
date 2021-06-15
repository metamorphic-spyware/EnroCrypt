from enrocrypt.error import *
from enrocrypt.basic import Password_Creator
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
def _Keyencryption(key:bytes):
    bases = base64.standard_b64encode(key)
    baseu = base64.urlsafe_b64encode(bases)
    return baseu

def _Keydecryption(key:bytes):
    bases = base64.standard_b64decode(key)
    baseu = base64.urlsafe_b64decode(bases)
    return baseu

def _dataencryption(data:bytes):
    bases = base64.standard_b64encode(data)
    baseu = base64.urlsafe_b64encode(bases)
    return baseu

def _datadecryption(data:bytes):
    baseu = base64.urlsafe_b64decode(data)
    bases = base64.standard_b64decode(baseu)
    return bases

def _BaseEncryption(text:bytes):
    key = Fernet.generate_key()
    f = Fernet(key)
    e = f.encrypt(text)
    return [key,e]

def _BaseDecryption(key:bytes,text:bytes):
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
        ModifiedError()
    if len(Data) != 4:
        ListIndexError()
    Key = Data[1]
    e_Data = Data[3]
    d_key = _Keydecryption(Key)      
    d_data = _datadecryption(e_Data)
    based = _BaseDecryption(d_key,d_data)
    return based

def FileEncryption(Path:str,KeyFilePath:str):
    '''Make Sure The Path You Give Has "\\" insted of just "\". KeyFilePath Takes the path where you have to keep the key for the encrypted file, Path Takes the path of the file which has to be encrypted
    Note: You Can Use The Key File To Store Multiple Keys But The Keys Must Not Be of The Same File Else You Will Get A Invalid Key Error'''
    file1 = open(Path,'r')
    data = (file1.read()).encode()
    with open(Path,'w') as file:
        e_file = Encrypt(bytes(data))
        key = str(e_file[1])
        e_data = str(e_file[3])
        file.write(e_data)
        if KeyFilePath is not None:
            with open(KeyFilePath,'a') as keyf:
                keyf.write(Path+':'+';'+':'+';')
                keyf.write(key)
                keyf.write('\n')
        if KeyFilePath is None:
            NoKeyFile()
    file1.close()
    
def FileDecryption(Path:str,KeyFilePath:str):
    '''Path: The Path Of The Encrypted File
    KeyFilePath: Path Of That key File Where The Decryption Key Is Stored For The File '''
    import ast
    file1 = open(Path,'r')
    if KeyFilePath is not None:
        with open(KeyFilePath,'r') as keyf:
            e_data = ast.literal_eval(file1.read())
            alls = keyf.read()
            splited =alls.split('\n')
            for char,i in enumerate(splited):
                a = i.split(':;:;')
                if a[char] == Path:
                    key = ast.literal_eval(a[char+1])
                    break
        n_data = str(Decrypt(key,e_data).decode())
        file2 = open(Path,'w')
        file2.write(n_data)

    if KeyFilePath is None:
        NoKeyFile()
def  _Base_Auth_Encryption(data:bytes,optd:bytes = None):
    password = Password_Creator()
    key = ChaCha20Poly1305.generate_key()
    encryptor = ChaCha20Poly1305(key)
    ed = encryptor.encrypt(password,data,optd)
    print([key,password,ed])
    return [key,password,ed]

def Auth_Encryption(data:bytes,optd:bytes = None):
    '''You Can't Choose Your Passwords For Security Reasons.
    data: The Data You Wnat To Encrypt.
    optd: Optional Data You Wnat To Give.
    We Recommend You Give The optd.'''
    basee = _Base_Auth_Encryption(data,optd)
    key = _Keyencryption(basee[0])
    password = _Keyencryption(basee[1])
    encd = _dataencryption(basee[2])
    final = []
    final.append('Key →');final.append(key);final.append('Password →');final.append(password);final.append('Encrypted Data →');final.append(encd);final.append('Optional Data →');final.append(optd)
    return final
def Auth_Decryption(key:bytes,password:bytes,data:bytes,optd:bytes = None):
    Key = _Keydecryption(key)
    Password = _Keydecryption(password)
    Data = _datadecryption(data)
    decryptor = ChaCha20Poly1305(Key)
    value = decryptor.decrypt(Password,Data,optd)
    return value
    
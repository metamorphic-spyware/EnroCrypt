from enrocrypt.error import Error
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
def FileEncryption(Path:str,KeyFilePath:str):
    '''Make Sure The Path You Give Has "\\" insted of just "\". KeyFilePath Takes the path where you have to keep the key for the encrypted file, Path Takes the path of the file which has to be encrypted
    Note: You Can Use The Key File To Store Multiple Keys But The Keys Must Not Be of The Same File Else You Will Get A Wrong Key Error'''
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
            Error.NoKeyFile()
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
        Error.NoKeyFile()
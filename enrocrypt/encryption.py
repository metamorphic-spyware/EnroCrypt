from enrocrypt.error import *
from enrocrypt.basic import Basic
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from cryptography.hazmat.primitives.ciphers.aead import AESGCM, AESCCM

class Encryption():
    __obj = Basic()
    def __str__(self) -> str:
        return "This Class Contains All The Encryption Functions Of EnroCrypt"
    def __Keyencryption(self,key:bytes):
        bases = base64.standard_b64encode(key)
        baseu = base64.urlsafe_b64encode(bases)
        return baseu

    def __Keydecryption(self,key:bytes):
        bases = base64.standard_b64decode(key)
        baseu = base64.urlsafe_b64decode(bases)
        return baseu

    def __dataencryption(self,data:bytes):
        bases = base64.standard_b64encode(data)
        baseu = base64.urlsafe_b64encode(bases)
        return baseu

    def __datadecryption(self,data:bytes):
        baseu = base64.urlsafe_b64decode(data)
        bases = base64.standard_b64decode(baseu)
        return bases

    def __BaseEncryption(self,text:bytes,Key:bytes = None):
        if Key == None:
            key = Fernet.generate_key()
            f = Fernet(key)
            e = f.encrypt(text)
            return [key,e]
        if Key is not None:
            f = Fernet(Key)
            e = f.encrypt(text)
            return [Key,e]

    def __BaseDecryption(self,key:bytes,text:bytes):
        f = Fernet(key)
        e = f.decrypt(text)
        return e

    def Encrypt(self,Data:bytes,Key:bytes = None):
        basee = self.__BaseEncryption(Data,Key=Key)
        e_data = self.__dataencryption(basee[1])
        e_key = self.__Keyencryption(basee[0])
        final = []
        final.append('Key →');final.append(e_key);final.append('Encrypted Data →');final.append(e_data)
        return final

    def Decrypt(self,Key:bytes,Encrypted_Data:bytes):
        d_key = self.__Keydecryption(Key)      
        d_data = self.__datadecryption(Encrypted_Data)
        based = self.__BaseDecryption(d_key,d_data)
        return based

    def Decrypt_List(self,Data:list):
        '''Takes The List Returned By Encrypt Function "AS IS" Without Modification'''
        if 'Key →' and 'Encrypted Data →' not in Data:
            ModifiedError()
        if len(Data) != 4:
            ListIndexError()
        Key = Data[1]
        e_Data = Data[3]
        d_key = self.__Keydecryption(Key)      
        d_data = self.__datadecryption(e_Data)
        based = self.__BaseDecryption(d_key,d_data)
        return based

    def FileEncryption(self,Path:str,KeyFilePath:str,Func = None,opd:str = None):
        '''Make Sure The Path You Give Has "\\" insted of just "\". KeyFilePath Takes the path where you have to keep the key for the encrypted file, Path Takes the path of the file which has to be encrypted
        Note: You Can Use The Key File To Store Multiple Keys But The Keys Must Not Be of The Same File Else You Will Get A Invalid Key Error'''
        file1 = open(Path,'r')
        data = (file1.read()).encode()
        if Func == None:
            with open(Path,'w') as file:
                e_file = self.Encrypt(bytes(data))
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
        if Func is not None:
            with open(Path,'w') as file:
                if opd is not None:
                    e_file = Func(bytes(data),bytes(opd.encode()))
                e_file = Func(bytes(data))
                key = str(e_file[1])
                password = str(e_file[3])
                e_data = str(e_file[5])
                file.write(e_data)
                if KeyFilePath is not None:
                    with open(KeyFilePath,'a') as keyf:
                        keyf.write(Path+':'+';'+':'+';')
                        keyf.write(key)
                        keyf.write(':;:;')
                        keyf.write(password)
                        keyf.write('\n')
                        if opd is not None:
                            keyf.write(opd)
                            keyf.write('\n')
                if KeyFilePath is None:
                    NoKeyFile()
            file1.close()
        
    def FileDecryption(self,Path:str,KeyFilePath:str,Func = None,opd:str = None):
        '''Path: The Path Of The Encrypted File
        KeyFilePath: Path Of That key File Where The Decryption Key Is Stored For The File '''
        import ast
        file1 = open(Path,'r')
        if Func == None:
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
                n_data = str(self.Decrypt(key,e_data).decode())
                file2 = open(Path,'w')
                file2.write(n_data)
        if Func is not None:
            with open(KeyFilePath,'r') as keyf:
                alls = keyf.read()
                splited =alls.split('\n')
                for char,i in enumerate(splited):
                    a = i.split(':;:;')
                    if a[char] == Path:
                        key = ast.literal_eval(a[char+1])
                        password = ast.literal_eval(a[char+2])
                        break
            n_data = str(Func(key,password,ast.literal_eval(file1.read()),opd).decode())
            file2 = open(Path,'w')
            file2.write(n_data)
        if KeyFilePath is None:
            NoKeyFile()
    def  __Base_Auth_Encryption(self,data:bytes,optd:bytes = None,Key:bytes = None):
        password = self.__obj.Password_Creator()
        if Key == None:
            key = ChaCha20Poly1305.generate_key()
            encryptor = ChaCha20Poly1305(key)
            ed = encryptor.encrypt(password,data,optd)
            return [key,password,ed]
        if Key is not None:
            encryptor = ChaCha20Poly1305(Key)
            ed = encryptor.encrypt(password,data,optd)
            return [Key,password,ed]
    def __Base_AESCCM(self,data:bytes,optd:bytes = None,Key:bytes = None):
        password = self.__obj.Password_Creator()
        if Key == None:
            key = AESCCM.generate_key(256)
            encryptor = AESCCM(key)
            ed = encryptor.encrypt(password,data,optd)
            return [key,password,ed]
        if Key is not None:
            encryptor = AESCCM(Key)
            ed = encryptor.encrypt(password,data,optd)
            return [Key,password,ed]
    def __Base_AESGCM(self,data:bytes,optd:bytes = None,Key:bytes = None):
        password = self.__obj.Password_Creator()
        if Key == None:
            key = AESGCM.generate_key(256)
            encryptor = AESGCM(key)
            ed = encryptor.encrypt(password,data,optd)
            return [key,password,ed]
        if Key is not None:
            encryptor = AESGCM(Key)
            ed = encryptor.encrypt(password,data,optd)
            return [Key,password,ed]
    def Auth_Encryption(self,data:bytes,optd:bytes = None,Key:bytes = None):
        '''You Can't Choose Your Passwords For Security Reasons.
        data: The Data You Wnat To Encrypt.
        optd: Optional Data You Wnat To Give.
        We Recommend You Give The optd.'''
        basee = self.__Base_Auth_Encryption(data,optd,Key=Key)
        key = self.__Keyencryption(basee[0])
        password = self.__Keyencryption(basee[1])
        encd = self.__dataencryption(basee[2])
        final = []
        final.append('Key →');final.append(key);final.append('Password →');final.append(password);final.append('Encrypted Data →');final.append(encd);final.append('Optional Data →');final.append(optd)
        return final
    def Auth_Decryption(self,key:bytes,password:bytes,data:bytes,optd:bytes = None):
        Key = self.__Keydecryption(key)
        Password = self.__Keydecryption(password)
        Data = self.__datadecryption(data)
        decryptor = ChaCha20Poly1305(Key)
        value = decryptor.decrypt(Password,Data,optd)
        return value
    def AESCCM(self,data:bytes,optd:bytes = None,Key:bytes = None):
        basee = self.__Base_AESCCM(data,optd,Key=Key)
        key = self.__Keyencryption(basee[0])
        password = self.__Keyencryption(basee[1])
        encd = self.__dataencryption(basee[2])
        final = []
        final.append('Key →');final.append(key);final.append('Password →');final.append(password);final.append('Encrypted Data →');final.append(encd);final.append('Optional Data →');final.append(optd)
        return final
    def AESCCM_Decryption(self,key:bytes,password:bytes,data:bytes,optd:bytes = None):
        Key = self.__Keydecryption(key)
        Password = self.__Keydecryption(password)
        Data = self.__datadecryption(data)
        decryptor = AESCCM(Key)
        value = decryptor.decrypt(Password,Data,optd)
        return value
    def AESGCM(self,data:bytes,optd:bytes = None,Key:bytes = None):
        basee = self.__Base_AESGCM(data,optd,Key=Key)
        key = self.__Keyencryption(basee[0])
        password = self.__Keyencryption(basee[1])
        encd = self.__dataencryption(basee[2])
        final = []
        final.append('Key →');final.append(key);final.append('Password →');final.append(password);final.append('Encrypted Data →');final.append(encd);final.append('Optional Data →');final.append(optd)
        return final
    def AESGCM_Decryption(self,key:bytes,password:bytes,data:bytes,optd:bytes = None):
        Key = self.__Keydecryption(key)
        Password = self.__Keydecryption(password)
        Data = self.__datadecryption(data)
        decryptor = AESGCM(Key)
        value = decryptor.decrypt(Password,Data,optd)
        return value
        
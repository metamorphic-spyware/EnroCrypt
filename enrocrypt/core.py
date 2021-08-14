from typing import Any
from enrocrypt.hashing import Hashing
from enrocrypt.encryption import Encryption
from enrocrypt.basic import Basic

class Core(Hashing,Encryption,Basic):
    '''Given Below Is The Syntax To Set Configurations For This Class. This Must Be Used As Is(Just Change The File Path)

    config = {
    'configs':{
        'salt_file':"The Path Of The File Where Your Salt Is Stored"
        }
    }'''
    def __init__(self) -> None:
        self.salt = ''
    def set_config(self,*args: Any):
        configs = (args[0]['configs']['salt_file'])
        value = self.__Set_Salt(configs)
        return value
    def __str__(self) -> str:
        return "The Base Class Of EnroCrypt"
    def __Set_Salt(self,salt:list):
        try:
            with open(salt,'r') as f:
                salts = f.read()
            self.salt = bytes(salts.encode())
            return True
        except FileNotFoundError:
            return Warning("No Salt File Found At The Given Location Using Random Salt")
        else:
            return False
    def get_hash_object(self):
        hashing = Hashing()
        hashing(bytes(self.salt.encode()))
        return hashing

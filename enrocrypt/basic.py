from enrocrypt import error
import uuid, os

class Basic():
    def __str__(self) -> str:
        return "This Class Has All the Basic Functions Of EnroCrypt"
    def seperator(self,data: str):
        '''Takes a String and Returns a List of the Characters. All Elements of the List are str. The List is Iterable.'''
        strData = str(data) # To avoid errors
        listString = list(strData)
        return listString

    def hexdigest(self,data:bytes):
        '''Returns A Wrong Hex Value. Must Only Be Used With Hashing Functions As The Hex Data Is Hard To Retrive'''
        to_ascii = self.seperator(data)
        in_ascii = []
        in_str_ascii = []
        for i in to_ascii:
            in_ascii.append(ord(i))
        for i in in_ascii:
            in_str_ascii.append(str(i))
        to_hex = int(''.join(in_str_ascii))
        in_hex = hex(to_hex)
        return in_hex

    def Hex(self,data):
        '''Gives The Correct Value With Each Group Of Letter(s) Representing A Character
        When Decoded Gives Integer. The Returned Value Will Have One More Layer Of Abstruction'''
        to_ascii = self.seperator(data)
        in_ascii = []
        in_hex = []
        for i in to_ascii:
            in_ascii.append(ord(i))
        for i in in_ascii:
            in_hex.append(hex(i))
        return in_hex
    def to_str(self,data):
        '''Takes The List Returned By Hex Function'''
        if type(data) != type([]):
            error.List()
        in_int = []
        in_ascii = []
        in_str = []
        for i,_ in enumerate(data):
            in_int.append(data[i])
        for i,_ in enumerate(in_int):
            in_ascii.append(int(in_int[i],16))
        for i,_ in enumerate(in_ascii):
            in_str.append(chr(in_ascii[i]))
        return(in_str)

    def Sign(self,sign:str):
        '''A Hint Of Upcomming Updates'''
        return uuid.uuid5(uuid.uuid4(),sign)
    def Password_Creator(self):
        '''This Password Generator Is For The Function Auth_Encryption. NOT for Generating Account Passwords'''
        return os.urandom(12)

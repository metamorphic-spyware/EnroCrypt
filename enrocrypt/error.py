class Error():
    def ModifiedError():
        raise ValueError('The List Provided To The Function Is Modified')
    def ListIndexError():
        raise IndexError('Returned List Must Only Have 4 Elements')
    def NoKeyFile():
        raise ValueError('No Path For The Key File was Provided')
    def WrongKey():
        from cryptography.fernet import InvalidToken
        raise InvalidToken('The Key Provided Is Not Correct')


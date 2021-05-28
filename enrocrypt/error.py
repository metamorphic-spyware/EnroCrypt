class ModifiedError(Exception):
    def __init__(self):
        self.msg = 'The List Provided To The Function Is Modified'
        super().__init__(self.msg)
class ListIndexError(Exception):
    def __init__(self):
        self.msg = 'Returned List Must Only Have 4 Elements'
        super().__init__(self.msg)
class NoKeyFile(Exception):
    def __init__(self):
        self.msg = 'No Path For The Key File was Provided'
        super().__init__(self.msg)

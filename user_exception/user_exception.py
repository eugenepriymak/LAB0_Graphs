class UserException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg


class UserError(UserException):
    def __init__(self, msg):
        msg = "ERROR: " + msg
        super().__init__(msg)
        self.msg = msg

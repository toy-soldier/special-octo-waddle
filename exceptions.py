class IsEmptyException(Exception):

    def __init__(self, message: str):
        super().__init__(message)


class IsFullException(Exception):

    def __init__(self, message: str):
        super().__init__(message)


class IllegalArgumentException(Exception):

    def __init__(self, message: str):
        super().__init__(message)

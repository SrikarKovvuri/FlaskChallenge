class NotFoundError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class ForbiddenError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Unauthorized(Exception):
    def __init__(self, msg):
        super().__init__(msg)


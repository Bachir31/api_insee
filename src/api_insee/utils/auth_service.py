
class AuthService():

    token = None

    def __init__(self, token = None):
        self.token = token


class MockAuth(AuthService):

    def __init__(self):
        self.token = "mocked-api-key"

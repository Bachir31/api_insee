

class AuthExeption(Exception):

    token: str = None

    def __init__(self, token):
        self.token = token

    def invalidkeyAndSecret(self):
        self.message = "Invalid consumer key or secret. token : %s" % self.token

        return self

    def unauthorized(self, reason=False):
        self.message = "Api connection unauthorized. token : %s" % self.token

        if reason:
            self.message += "\n %s" % (reason)

        return self

    def __str__(self):
        return self.message

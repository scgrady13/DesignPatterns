class ExternalAuth:
    def authenticate(self, email, password):
        # Simulate external authentication
        if email == "user@example.com" and password == "password":
            return True
        return False


class AuthAdapter:
    def __init__(self, external_auth):
        self.external_auth = external_auth

    def login(self, username, password):
        # Convert username to email format
        email = f"{username}@example.com"
        return self.external_auth.authenticate(email, password)


class AuthSystem:
    def __init__(self, auth_adapter):
        self.auth_adapter = auth_adapter

    def login(self, username, password):
        return self.auth_adapter.login(username, password)


if __name__ == "__main__":
    external_auth = ExternalAuth()
    auth_adapter = AuthAdapter(external_auth)
    auth_system = AuthSystem(auth_adapter)

    result = auth_system.login("user", "password")
    print(f"Login success: {result}")  # Output: Login success: True

    result = auth_system.login("user", "wrong_password")
    print(f"Login success: {result}")  # Output: Login success: False

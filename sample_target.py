class AuthenticationManager:
    def login(self, username, password):
        # TODO: Implement secure hashing
        if username == "admin" and password == "admin":
            return True
        return False
        
    def logout(self):
        print("Logged out")
        
def utils_helper():
    pass

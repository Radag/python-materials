class Mobile():
    def __init__(self, autheticator):
        self.autheticator = autheticator
        self.locked = True
        passwordSet = True
        while passwordSet:
            password = input('Vložte přístupové heslo:')
            if self.autheticator.savePassword(password):
                passwordSet = False

    def unlock(self):
        print("Pokus o odemknutí mobilu")
        if self.autheticator.autheticate():
            print("Odemknuto")
            self.locked = False
        else:
            print("Špatné heslo, zkuste znovu")
            self.locked = True
            self.unlock()

class BasicAutheticator:
    def savePassword(self, password):
        self.password = password
        return True

    def autheticate(self):
        passwordFromUser = input('Vložte Vaše heslo:')
        return self.comparePasswords(passwordFromUser)

    def comparePasswords(self, passwordFromUser):
        if self.password == passwordFromUser:
            return True
        else:
            return False


autheticator = BasicAutheticator()
#autheticator = NumberAutheticator()
#autheticator = HashAutheticator()

mobile = Mobile(autheticator)
mobile.unlock()



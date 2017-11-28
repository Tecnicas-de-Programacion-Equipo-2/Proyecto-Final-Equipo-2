import json

class Passwords:
    __passwords = []

    @classmethod
    def __save_password(cls):
        cls.__rfids = []
        try:
            passwords_file = open('passwords.json', 'r+')
            passwords = json.load(passwords_file)
        except FileNotFoundError:
            print('Error r+ testfile')
        else:
            for password in passwords:
                cls.__passwords.append(password['password'])

            passwords_file.close()

    @classmethod
    def transfer_passwords(cls):
        Passwords.__save_password()
        return cls.__passwords

    def new_tag(self, new_password):
        new_tag={}
        new_tag['type'] = 'card'
        new_tag['password'] = new_password

class PasswordValidation:

    @staticmethod
    def validation(validate):
        passwords = Passwords.transfer_passwords()
        print(passwords)
        for password in passwords:
            if password == validate: return True
        return False
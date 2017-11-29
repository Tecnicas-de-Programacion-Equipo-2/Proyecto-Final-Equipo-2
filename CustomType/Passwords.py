from CustomType.passwords_hide import Passwords
import json

class ChangePasswords:

    @staticmethod
    def validation(validate):
        # try:
        #     passwords_file = open('keys.json', 'r+')
        #     passwords = json.load(passwords_file)
        # except FileNotFoundError:
        #     print('Error W testfile')
        # else:
        #     for password in passwords:
        #         print(password)
        #         if password['password'] == validate:
        #             return True
        #     return False
        #     passwords_file.close()

        for password in Passwords.keys:
            if password['password'] == validate:
                return True
        return False

    @staticmethod
    def new_card(new_password):
        Passwords.keys.append(new_password)

    @staticmethod
    def change_passwords(new_password):
        Passwords.keys[0]['password'] = new_password
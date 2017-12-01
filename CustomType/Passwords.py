import json

class ChangePasswords:

    @staticmethod
    def validation(validate):
        try:
            passwords_file = open('..\CustomType\keys.json', 'r+')
            passwords = json.load(passwords_file)
        except FileNotFoundError :
            print('Error W testfile')
        else:
            for password in passwords:
                if password['password'] == validate:
                    return True
            passwords_file.close()
            return False

    @staticmethod
    def new_card(new_password):
        try:
            passwords_file = open('..\CustomType\keys.json', 'r+')
            json_data = json.load(passwords_file)
        except FileNotFoundError :
            print('Error W testfile')
        else:
            json_data.append(new_password)
        finally:
            password_json_format = json.dumps(json_data, indent=2)
            passwords_file.seek(0, 0)
            passwords_file.write(password_json_format)
            passwords_file.close()

    @staticmethod
    def change_passwords(new_password):
        try:
            passwords_file = open('..\CustomType\keys.json', 'r+')
        except FileNotFoundError:
            print('Error W testfile')
        else:
            json_data = json.load(passwords_file)
            json_data[0]['password'] = new_password
            passwords_file.seek(0,0)
            json_data_format = json.dumps(json_data, indent=2)
            passwords_file.write(json_data_format)
            passwords_file.close()
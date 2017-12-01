import json

class JsonManager():

    @staticmethod
    def open_json_file(file_name):
        try:
            with open(file_name + '.json', 'r') as infile:
                data = json.load(infile)
        except Exception:
            return None
        return data
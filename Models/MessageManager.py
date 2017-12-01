from twilio.rest import Client
from Models.JsonManager import JsonManager

class MessageManager():

    class Constants:
        env_file = "Env/env"

    def __init__(self):
        env_variables = JsonManager.open_json_file(self.Constants.env_file)
        if env_variables is None:
            return

        account_sid = env_variables.get("account_sid", None)
        auth_token = env_variables.get("auth_token", None)
        self.__twilio_phone = env_variables.get("twilio_phone", None)

        self.__client = Client(account_sid, auth_token)

    def send_message(self, phone, message):
        self.__client.messages.create(to = phone, from_= self.__twilio_phone, body = message)
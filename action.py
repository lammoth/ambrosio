from actions import *

class Action:

    def __init__(self, message):
        pass

    def help(self):
        response = "You can ask for:\ncredentials <machine/domain>"
        return response 

    def get_action(self, message):
        if str(message.split(" ")[0]) == "credentials":
            self.credentials_action = credentials.Credentials()
            self.credentials_action.search_credential(message.replace(str(message.split(" ")[0]), ""))
        else:
            return self.help()



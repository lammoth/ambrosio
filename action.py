from ambrosio.actions import credentials

class Action(object):

    def __init__(self, message):
        pass

    def help(self, message=None):
        response = "You can ask for:\ncredentials <machine/domain>" if not message else message
        return response 

    def get_action(self, message):
        if str(message.split(" ")[0]) == "credentials":
            self.credentials_action = credentials.Credentials()
	    return self.credentials_action.kdb.get_passwords(message.replace(str(message.split(" ")[0]), ""))
        else:
            return self.help()



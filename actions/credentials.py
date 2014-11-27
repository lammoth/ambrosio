from ...action import Action
from utils.kdb import KDB

class Credentials(Action):

    def __init__(self):
        self.kdb = KDB()
        self.kdb.get_passwords()

    def search_credential(self, credential):
        self.kdb.get_password(credential)

import pexpect
import time

KP_PASSWORD = ""
PATH = ".kdb"

class KDB(object):

    def __init__(self, password=None, path=None):
        self.password = password if password else KP_PASSWORD
        self.path = path if path else PATH
        self.credentials = []

    def get_passwords(self, credential):
        self.kdb_cmd = pexpect.spawnu("kp -d %s list" % self.path)
        time.sleep(1)
        self.kdb_cmd.sendline(self.password)
        for pass_line in self.kdb_cmd:
            self.credentials.append(pass_line.split('|'))
        return self.get_password(credential)

    def get_password(self, key):
        matches = []
        for pwd in self.credentials:
            try:
                if key in pwd[1] or key in pwd[3]:
		    matches.append("%s / %s" % (pwd[4].lstrip().rstrip(), pwd[5].lstrip().rstrip()))
            except:
                pass
        return matches

if __name__ == "__main__":
    kdb = KDB()
    kdb.get_passwords()




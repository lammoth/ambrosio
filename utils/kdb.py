import pexpect
import time

KP_PASSWORD = "XXXX"
PATH = "/mnt/dev_dir/Claves.kdbx"

class KDB:

    def __init__(self, password=None, path=None):
        self.password = password if password else KP_PASSWORD
        self.path = path if path else PATH
        self.credentials = []

    def get_passwords(self):
        print "kp -d %s list" % self.path
        self.kdb_cmd = pexpect.spawnu("kp -d %s list" % self.path)
        time.sleep(0.1)
        self.kdb_cmd.sendline(self.password)
        for pass_line in self.kdb_cmd:
            self.credentials.append(pass_line)

    def get_password(self, key):
        matching = [idx for idx, pwd in self.credentials if key in pwd]
        print matching


if __name__ == "__main__":
    kdb = KDB()
    kdb.get_passwords()




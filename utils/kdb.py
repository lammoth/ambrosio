#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Ambrosio: A XMPP bot to serve us
    Copyright (C) 2014  Francisco Hidalgo
    This file is part of Ambrosio.

    See the file LICENSE for copying permission.
"""

import pexpect
import time

# KeePass master key
KP_PASSWORD = ""

# KeePass file path
PATH = ".kdb"

class KDB(object):

    """
    A class to support a KeePass format.

    This class helps you to extract a keepass credentials
    based in a string to search.
    """

    def __init__(self, password=None, path=None):

        """
        Returns available actions.

        Arguments:
            password -- A password to decode the KeePass file.
            path -- A path to the KeePass file.
        """
        self.password = password if password else KP_PASSWORD
        self.path = path if path else PATH
        self.credentials = []

    def get_passwords(self, credential):
        """
        Get the passwords availbales in the KeePass file.

        Arguments:
            credential -- A value to search in the passwords list.
        """
        self.kdb_cmd = pexpect.spawnu("kp -d %s list" % self.path)
        # Quit this
        # TODO: implements a pexpect TIMEOUT
        time.sleep(1)
        self.kdb_cmd.sendline(self.password)
        for pass_line in self.kdb_cmd:
            self.credentials.append(pass_line.split('|'))
        return self.get_password(credential)

    def get_password(self, key):
        """
        Get the password searched

        Arguments:
            key -- A value to search in the passwords list.
        """
        matches = []
        for pwd in self.credentials:
            try:
                if key in pwd[1] or key in pwd[3]:
		    matches.append("%s / %s" % \
                (pwd[4].lstrip().rstrip(), pwd[5].lstrip().rstrip())
            )
        except Exception as e:
                print e

        return matches

if __name__ == "__main__":
    kdb = KDB()
    kdb.get_passwords()

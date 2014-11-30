#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Ambrosio: A XMPP bot to serve us
    Copyright (C) 2014  Francisco Hidalgo
    This file is part of Ambrosio.

    See the file LICENSE for copying permission.
"""

from ambrosio.utils.kdb import *

class Credentials(object):

    """
    A class to add a credential service.

    To get the credentials, we use a KeePass format,
    if you want implement a new credential, implement
    a conditional to support them
    """

    def __init__(self):
        """
        Initializes a keepass syste, to get the credentials.

        The utilities are located in the utils directory,
        if you want add a new utility, add it in this directory.
        """
        self.kdb = KDB()

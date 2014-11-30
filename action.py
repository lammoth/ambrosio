#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Ambrosio: A XMPP bot to serve us
    Copyright (C) 2014  Francisco Hidalgo
    This file is part of Ambrosio.

    See the file LICENSE for copying permission.
"""

from ambrosio.actions import credentials

class Action(object):

    """
    A class to support Ambrosio basic actions.
    """

    def __init__(self, message):
        """
        Nothing to do here.
        """
        pass

    def help(self, message=None):
        """
        Returns available actions.

        Arguments:
            message -- A string to show as help command response.
        """
        return "You can ask for:\ncredentials <machine/domain>" \
            if not message else message

    def get_action(self, message):
        """
        Select the correct action.

        In the actions directory resides the available actions.
        If you want implements some action, locate your action in actions
        directory and add the conditional to support it

        Arguments:
            message -- A message to process in the selected action.
        """

        # To choose credentials action
        if str(message.split(" ")[0]) == "credentials":
            self.credentials_action = credentials.Credentials()
    	    return self.credentials_action.kdb.get_passwords(
                message.replace(str(message.split(" ")[0]), "")
            )
        # If action is not available, show help message
        else:
            return self.help()

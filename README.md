ambrosio
========

A XMPP bot to serve us

Ambrosio treats to serve us in the common daily tasks.

To install it, you need (On Debian based systems):

<pre>
sudo apt-get install ejabberd
pip isntall pexpect
pip isntall sleekxmpp
pip isntall keepassx
</pre>
In order to use keepassx, we make some changes in order to work with it.
Once you installed keepassx, follow the next steps:
<pre>
$ vim .../lib/python2.7/site-packages/keepassx/main.py
<br />
# Add Username and Password columns
t = PrettyTable(['Title', 'Uuid', 'GroupName', 'Username', 'Password'])
<br />
# Add username and password in order to show
t.add_row([entry.title, entry.uuid, entry.group.group_name, entry.username, entry.password])
<br />
# Hide title, username, url and notes only show password field
default_fields = ['password']
</pre>

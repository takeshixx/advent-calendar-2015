from twisted.internet import protocol, reactor

SANTA = """Login: santa                             Name: Santa Claus
Directory: /home/santa                   Shell: /bin/sh
On since Wed Dec  1 00:01 (CET) on pts/0 from 37.191.167.63
New mail received Wed Dec  2 03:01 2015 (CET)
     Unread since Tue Dec  1 03:33 2015 (CET)
Mail forwarded to: santa@adversec.com
Project: XMAS!
Plan:
* Get Christmas presents
* Find Rudolph
* Eggnog
* Jingle the bells
* Feed cat
Public key:
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwQe1QKPSkRrIx0DhQQCL
QmBvTI5ZBWU0XP246p0mqYDOPjaVxd1nSaSUaSE9jHK/j3iv2WfQ+BDA2MjTCv/s
Afi6nN84OK68B32k+Ybia3T6rLpgCTZ6l1h0M553yGXSxQBtAt33/3z/ywhh6hYH
uxmqxva4VB8y90sIxp3XtC9wTPi9FNtkHYT84DcdckEJkmLMxp+XScYU0y/Ojbnm
bFLqFh1EuEow+AnZzOJGfnSZw4a7ymCO2UpZsbVMR+HE1tqwjXw/zPILCul3pWSn
aWMCCN0ig0Q962Bihx1uyjCIHjQp25Rm+kreD4xMyoo2JGvSKI2Vhs1PjSa5a5In
rwIDAQAB
-----END PUBLIC KEY-----"""

ROOT = """Login: root                             Name: Charlie Root
Directory: /root                        Shell: /bin/sh
Last login Wed Sep 17 04:57 (CET) on pts/7 from null.adversec.com
No Mail.
No Plan."""

RUDOLPH = """Login: rud0lph                          Name: Rudolph Naso Rosso
Directory: /home/shed                   Shell: /bin/sh
No Mail.
No Plan."""

NOBODY = """Login: nobody                           Name: Unprivileged user
Directory: /nonexistent                 Shell: /usr/sbin/nologin
No Mail.
No Plan."""

OPERATOR = """Login: operator                         Name: System &
Directory: /                            Shell: /usr/sbin/nologin
No Mail.
No Plan."""

ALLUSERS = [ SANTA, ROOT, RUDOLPH, NOBODY, OPERATOR ]

class FingerProtocol(protocol.Protocol):
    def dataReceived(self, data):
        data = data.strip()
        if not data:
            self.transport.loseConnection()
            return

        if data == 'root':
            self.writeLn(ROOT)
        elif data == 'santa':
            self.writeLn(SANTA)
        elif data == 'rud0lph':
            self.writeLn(RUDOLPH)
        elif data == 'nobody':
            self.writeLn(NOBODY)
        elif data == 'operator':
            self.writeLn(OPERATOR)
        elif data == 'user':
            self.writeLn('\n\n'.join(ALLUSERS))
        else:
            for bad in ['\'', '"', '|', ';', '\\', '/', '!']:
                if bad in data:
                    self.writeLn('XMAS-IDS v12 JUST DISCOVERED SOME BAD CHRISTMAS VIBES! XMAS-CERT HAS BEEN NOTIFIED...')
                    self.writeLn('YOU MADE SANTA MAD :(')
                    self.transport.loseConnection()
                    return

            self.writeLn('finger: {}: no such user'.format(data))

        self.transport.loseConnection()

    def writeLn(self, data):
        self.transport.write('{}\n'.format(data))


class FingerFactory(protocol.Factory):

    def buildProtocol(self, addr):
        return FingerProtocol()


if __name__ == '__main__':
    reactor.listenTCP(3, FingerFactory())
    reactor.listenTCP(3, FingerFactory(), interface='fcff:17:40::13')
    reactor.run()

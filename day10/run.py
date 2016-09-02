# -*- coding: utf-8 -*-
from OpenSSL import SSL
from twisted.internet import ssl, reactor, protocol
from twisted.web import server, resource
from twisted.protocols import basic
import re

CA_CERT = '/usr/local/srv/certs/chain.pem'
DH_PARAMS = '/usr/local/srv/day10/dh.pem'
SERVER_KEY = '/usr/local/srv/certs/privkey.pem'
SERVER_CERT = '/usr/local/srv/certs/cert.pem'

CHRE = re.compile(r"christmas", re.IGNORECASE)

ART = """                  .!,            .!,
                 ~ 6 ~          ~ 6 ~
            .    ' i `  .-^-.   ' i `
          _.|,_   | |  / .-. \   | |
           '|`   .|_|.| (-` ) | .|_|.
           / \ ___)_(_|__`-'__|__)_(______
          /`,o\)_______________________o_(
         /_* ~_\[___]___[___]___[___[_[\`-.
         / o .'\[_]___[___]___[___]_[___)`-)
        /_,~' *_\_]                 [_[(  (
        /`. *  *\_]                 [___\ _\\
       /   `~. o \]      ;( ( ;     [_[_]`-'
      /_ *    `~,_\    (( )( ;(;    [___]
      /   o  *  ~'\   /\ /\ /\ /\   [_[_]
     / *    .~~'  o\  ||_||_||_||   [___]
    /_,.~~'`    *  _\_||_||_||_||___[_[_]_
    /`~..  o        \:::::::::::::::::::::\\
   / *   `'~..   *   \:::::::::::::::::::::\\
  /_     o    ``~~.,,_\=========\_/========='
  /  *      *     ..~'\         _|_ .-_--.
 /*    o   _..~~`'*   o\           ( (_)  )
 `-.__.~'`'   *   ___.-'            `----'
       ":-------:"
    hjw  \_____/"""

class HTTPProtocol(basic.LineReceiver):

    def __init__(self):
        self.lines = []

    def lineReceived(self, line):
        self.lines.append(line)
        if not line:
            self.sendResponse()

    def sendResponse(self):
        client = self.transport.getPeer()
        print(client)
        crt = self.transport.getPeerCertificate()

        if crt:
            issuer = crt.get_issuer().get_components()
            subject = crt.get_subject().get_components()

            print(issuer)
            print(subject)
            print('--')

            # [('O', 'Christmas Inc'), ('CN', 'ChristmasTrust MiraculousServer Standard Validation CA')]
            cn = [_[1] for _ in subject if _[0] == 'CN'][0]

        self.sendLine('HTTP/1.1 2412 OK')
        self.sendLine('')

        if crt:
            if CHRE.findall(cn):
                body = 'Welcome Christmas Inc. Employee "{}"!'.format(cn)
                body += '\r\n\r\n'
                body += 'Happy 10th of December, comrad!'
                body += '\r\n\r\n'
                body += ART
            else:
                body = '"{}" is not a Christmas Inc. employee! XMAS-CERT is watching you...'.format(cn)
        else:
            body = 'No client certificate found...'

        body += '\r\n'
        self.transport.write(body)
        self.transport.loseConnection()


class HTTPFactory(protocol.ServerFactory):

    def buildProtocol(self, addr):
        return HTTPProtocol()


def verifyCallback(connection, x509, errnum, errdepth, ok):
    #print('issuer: {}'.format(x509.get_issuer()))
    #print('subject: {}'.format(x509.get_subject()))
    #print('pubkey: {}'.format(x509.get_pubkey()))
    return True


if __name__ == '__main__':
    factory = HTTPFactory()
    myContextFactory = ssl.DefaultOpenSSLContextFactory(SERVER_KEY, SERVER_CERT, sslmethod=SSL.TLSv1_2_METHOD)

    ctx = myContextFactory.getContext()
    ctx.set_verify(SSL.VERIFY_PEER, verifyCallback)
    ctx.set_verify_depth(0)
    ctx.load_verify_locations(CA_CERT)
    ctx.load_tmp_dh(DH_PARAMS)
    ctx.set_cipher_list('ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:RSA+AESGCM:RSA+AES:!3DES:!aNULL:!MD5')

    reactor.listenSSL(10, factory, myContextFactory)
    reactor.listenSSL(10, factory, myContextFactory, interface='fcff:17:40::13')
    reactor.run()

from twisted.internet import reactor, protocol
from twisted.protocols import wire

class DiscardProtocol(wire.Discard):
    pass


class DiscardFactory(protocol.Factory):

    def buildProtocol(self, addr):
        return DiscardProtocol()


if __name__ == '__main__':
    reactor.listenTCP(9, DiscardFactory())
    reactor.listenTCP(9, DiscardFactory(), interface='fcff:17:40::13')
    reactor.run()

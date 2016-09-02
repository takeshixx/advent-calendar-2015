from twisted.internet import reactor, protocol
from twisted.protocols import wire
import time

class DaytimeProtocol(wire.Daytime):

    def connectionMade(self):
        self.transport.write(time.asctime(time.localtime(time.time())) + '\r\n')
        self.transport.loseConnection()


class DaytimeFactory(protocol.Factory):

    def buildProtocol(self, addr):
        return DaytimeProtocol()


if __name__ == '__main__':
    reactor.listenTCP(13, DaytimeFactory())
    reactor.listenTCP(13, DaytimeFactory(), interface='fcff:17:40::13')
    reactor.run()

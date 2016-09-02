from twisted.internet import reactor, protocol
from twisted.protocols import wire
import random

class ChargenProtocol(wire.Chargen):

    def resumeProducing(self):
        noise = ' '.join(' ' for x in range(random.randint(10,20)))
        noise += '*'
        noise += ' '.join(' ' for x in range(random.randint(10,20)))
        self.transport.write(noise)

class ChargenFactory(protocol.Factory):

    def buildProtocol(self, addr):
        return ChargenProtocol()

if __name__ == '__main__':
    reactor.listenTCP(19, ChargenFactory())
    reactor.listenTCP(19, ChargenFactory(), interface='fcff:17:40::13')
    reactor.run()

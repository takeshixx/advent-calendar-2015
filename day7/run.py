from twisted.internet import reactor, protocol
from twisted.protocols import wire
import random

class EchoProtocol(wire.Echo):

    def dataReceived(self, data):
        data = data.strip()

        if not data:
            return

        dice = random.randint(1,10)

        if dice is 1:
            self.transport.write('Ho ho ho, {}\r\n'.format(data))
        elif dice is 2:
            self.transport.write('{} - for the sake of Christmas!\r\n'.format(data))
        elif dice is 3:
            self.transport.write('{} and Merry Christmas!\r\n'.format(data))
        elif dice is 4:
            self.transport.write('{}\r\n'.format(data[::-1]))
        elif dice is 5:
            self.transport.write('In the name of Santa: {}\r\n'.format(data))
        elif dice is 6:
            self.transport.write('rabble rabble rabble....\r\n')
        elif dice is 7:
            self.transport.write('May your Christmas be filled with lots of happiness, peace and love... ooh and lots of {}\r\n'.format(data))
        elif dice is 8:
            self.transport.write('May your home be filled with Christmas songs and some {}\r\n'.format(data))
        elif dice is 9:
            self.transport.write('Giving and receiving love is the only guarantee of having a truly Merry Christmas. Alternatively, eggnog will do the job...\r\n')
        else:
            self.transport.write('Dude, give Santa a break!\r\n')


class EchoFactory(protocol.Factory):

    def buildProtocol(self, addr):
        return EchoProtocol()


if __name__ == '__main__':
    reactor.listenTCP(7, EchoFactory())
    reactor.listenTCP(7, EchoFactory(), interface='fcff:17:40::13')
    reactor.run()

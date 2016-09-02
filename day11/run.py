from twisted.internet import protocol, reactor
import datetime
import random

SANTA = 'santa                  pts/0       Nov  30 23:57 (82.4.61.157)'
RUDOLPH = 'rud0lph                pts/6       {} ({})'

ELVES = [
    'elf_twinklebells       pts/{}      {} ({})',
    'elf_silversleigh       pts/{}      {} ({})',
    'elf_trufflebuns        pts/{}      {} ({})',
    'elf_stripycane         pts/{}      {} ({})',
    'elf_toffeepudding      pts/{}      {} ({})',
    'elf_gingernuts         pts/{}      {} ({})',
    'elf_wintertree         pts/{}      {} ({})',
    'elf_truffeltoes        pts/{}      {} ({})',
    'elf_hollyberry         pts/{}      {} ({})',
    'elf_jollytrifle        pts/{}      {} ({})',
    'elf_iciclebaubles      pts/{}      {} ({})',
    'elf_sparklespice       pts/{}      {} ({})'
]

def get_time():
    t = datetime.datetime.now() - datetime.timedelta(seconds=random.randint(47, 360))
    return t.strftime('%b  %d %H:%M')

def get_ip():
    return '.'.join(map(str, (random.randint(0, 255) for _ in range(4))))



class SystatProtocol(protocol.Protocol):

    def connectionMade(self):
        resp = SANTA
        resp += '\r\n'

        if random.randint(1, 5) is 1:
            resp += RUDOLPH.format(get_time(), get_ip())
            resp += '\r\n'

        active_elf_count = random.randint(3, len(ELVES))
        active_elves = set()

        while len(active_elves) < active_elf_count:
            active_elves.add(random.randint(0, len(ELVES)-1))

        elf_pts = set()

        while len(elf_pts) < active_elf_count:
            elf_pts.add(random.randint(11, 39))

        for elf in active_elves:
            resp += ELVES[elf].format(elf_pts.pop(), get_time(), get_ip())
            resp += '\r\n'

        self.transport.write(resp)
        self.transport.loseConnection()


class SystatFactory(protocol.Factory):

    def buildProtocol(self, addr):
        return SystatProtocol()


if __name__ == '__main__':
    reactor.listenTCP(11, SystatFactory())
    reactor.listenTCP(11, SystatFactory(), interface='fcff:17:40::13')
    reactor.run()

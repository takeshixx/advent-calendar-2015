from twisted.internet import protocol, reactor

bell = """                                              zeeeeee
                         ..$$$$              $       $$$.
                      .$F""   ^N            $           "b
                   .@**         b.         $ .$          '$
                  .$$$$.         3        @ 4$ .$$      4$$r
                  $$$$$$$br 'k   ^u      z  @e$$*"   zP*" 4F
                 $^F$9$$$$3N ^r L $     4F.$$$     J$$    4F
                d   F'$$e  ^3eFN^$4.    db$$"eeeF$$"@$    4F
               4 x$$ ''$$     *L@$$$   $J$$$$     $rJL $  $"
               4 $    e"F      '$$$$$$$$$$"       $$$$F$ 4$
               'u$ b$L4@F        $$$ $  *$$.     :$$d$$$$$$
                $4L$$$$$$         3$ *   'L$     $$$$$$$$$
                94$$$$$$$r         $ee   d$$eeee$$$$$F$$#
                'd$$$$$$$$N.......$$$$$$$$. $ $...$$$$$
                 ^$$$$$$$$$$$$$$$$"$"$$$$F"c $$$$$$$ "$c
                   #*$$$$$****be$ 4$$$$'$$$$ 4$$$$$$$b$"$*eeec
                   @$$    4$$$$$$ '$$F   "$$ J$$$$ $$$        $$$$$$$$$$
       zee****$$$$*"    zee$$$$$$$ 3Nr   z$"e$$$$$$ed**"    d$ "  e*#
     J$k.       $$$L..     ..$$&$*$..#$$$" @F $$L..$$$%   4$  ..u$
   4$"$$$$$$.    d$$$$    ^"9$$"   ^$$$$$$$F    ^""$$N     "N "9$
 .$" .$$$$$$$$.    $$$u...d*#   .d**"   ^  "**u.      **... ** . *.
.E   "*"$$#$$$$4. ""$$$""     $"            4""$       ^**$$$$$$$$$$
*******F  .ee********       .d# .    ^     ."  " *e
       L d$                 $           $   . $    $
       $$"                 @ e       r '  ^ " e z e4b
       $F                 d           '     %'. .% $4L
                         d        @ 'r 4   r W?%$4'b@$r
                         P  ^ #" "   P.     $^ z" r.$Jb
                         L              $$-    " d34 $$
                        $^        4    d.e.re$bzd$J@ b.k
                       zF   '$ *~'  * '$'" # *$$% $$$JL$
                      :$                        d$  $$$d3
                     z#         zeeeeeeeeeeeeee$b*r'' P $$u
                    d     d$$$$$$$$$$$ 3$$$$$$$$$$$$$$ k  $r
                   P$e@$$$$$$$$$$$$$$$c $$$$$$$$$$$$$$$$$be$e
                 J$$$$$$$$$$$$$$$$$$$$$ J$$$$$$$$$$$$$$$$$$$bb
               4$$$$$$$$$$$$$$$$$$$$$$" ""$$$$$$$$$$$$$$$$$$$$$b
               $$$$$$$$$$$$$$$$$$$$$"   "  $$$$$$$$$$$$$$$$$F*$$L
               $$$$$$$$$$$$$$$$$$$$$      $F$$$$$$$$$$$$$$$$$F$$$
               $$$$$$$$$$$$$$$$$$$$$.  e  #x$$$$$$$$$$$$$$$$$"$$F
                $$$$$$$$$$$$$$$$$$$$$$...u$$$$$$$$$$$$$$$$$$$@$$
                 ^"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
                    "*$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.**"
                       ""**$$$$$$$$$$$$$$$$$$$$$$$$$$**""
                                ***************#
"""

class AdventProtocol(protocol.Protocol):

    def connectionMade(self):
	print('Got connection from: {}'.format(self.transport.getPeer()))
        self.writeLn(bell)
        self.writeLn('YOU HAVE JUST OPENED THE FIRST DAY OF YOUR ADVENT CALENDAR!')
        self.writeLn('HAVE A NICE DAY!')
        self.transport.loseConnection()

    def dataReceived(self, incoming):
        pass

    def writeLn(self, data):
        self.transport.write('{}\n'.format(data))


class AdventFactory(protocol.Factory):

    def buildProtocol(self, addr):
        return AdventProtocol()

if __name__ == '__main__':
    reactor.listenTCP(1, AdventFactory())
    reactor.listenTCP(1, AdventFactory(), interface='fcff:17:40::13')
    reactor.run()

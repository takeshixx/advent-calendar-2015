from twisted.web import server, resource
from twisted.internet import reactor

HTTP_HEADER_SERVER = 'Santa Web v24.12'
HTTP_HEADER_XMAS = 'Ho ho ho, merry x-max!'
HTTP_HEADER_DATE = '24 Dec 2015, way ahead of ya'
HTTP_HEADER_TYPE = 'text/html;maybe something else...'

class Simple(resource.Resource):
    isLeaf = True
    def render(self, request):
        request.setHeader('Server', HTTP_HEADER_SERVER)
        request.setHeader('X-X-Mas', HTTP_HEADER_XMAS)
        request.setHeader('Date', HTTP_HEADER_DATE)
        request.setHeader('Content-Type', HTTP_HEADER_TYPE)
        return """<!DOCTYPE html>
<html>
    <head>
        <style text="text/css">
            .content {
                width: 100%;
                height: 100%;
            }
            .content img {
                width: 100%;
                height: 90%;
            }
        </style>
    </head>

    <body>
        <div class="content">
            <img src="http://fs5.directupload.net/images/151212/8fzcjv5t.jpg" alt="day12" />
            <h1>HAPPY 12TH OF DECEMBER!</h2>
        </div>
    </body>
</html>"""

if __name__ == '__main__':
    site = server.Site(Simple())
    reactor.listenTCP(12, site)
    reactor.listenTCP(12, site, interface='fcff:17:40::13')
    reactor.run()

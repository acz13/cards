import tornado.ioloop
import tornado.web
from main import *

application = tornado.web.Application([
    (r"/", WSHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
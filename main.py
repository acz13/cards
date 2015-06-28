import tornado.ioloop
import tornado.web


class WSHandler(tornado.websocket.WebSocketHandler):

    def open(self):
        self.id = uuid.uuid4()
        external_storage[self.id] = {'id':self.id}
        print ('new connection')
        self.write_message("Hello World")

    def on_message(self, message):
        #Some message parsing here
        if message.type == 'set_group':
           external_storage[self.id]['group'] = message.group
        print ('message received %s' % message)

    def on_close(self):
        external_storage.pop(self.id)
        print ('closed connection')


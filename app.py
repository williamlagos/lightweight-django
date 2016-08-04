#!/usr/bin/env python

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.wsgi
import logging,sys,os
from helloworld.wsgi import application as myapp_wsgi

logging.basicConfig(filename='tornado.log',level=logging.DEBUG)

# Javascript Usage:
# var ws = new WebSocket('ws://localhost:8000/ws');
# ws.onopen = function(event){ console.log('socket open'); }
# ws.onclose = function(event){ console.log('socket closed'); }
# ws.onerror = function(error){ console.log('error:', err); }
# ws.onmessage = function(event){ console.log('message:', event.data); }
# # ... wait for connection to open
# ws.send('hello world')


class MyAppWebSocket(tornado.websocket.WebSocketHandler):
    # Simple Websocket echo handler. This could be extended to
    # use Redis PubSub to broadcast updates to clients.

    clients = set()

    def check_origin(self,origin):
        return True

    def open(self):
        logging.info('Client connected')
        MyAppWebSocket.clients.add(self)

    def on_message(self, message):
        logging.log(logging.DEBUG,'Received message %s' % (message))
        MyAppWebSocket.broadcast(message)

    def on_close(self):
        logging.info('Client disconnected')
        if self in MyAppWebSocket.clients:
            MyAppWebSocket.clients.remove(self)

    @classmethod
    def broadcast(cls, message):
        for client in cls.clients:
            client.write_message(message)


application = tornado.web.Application([
    (r'/ws', MyAppWebSocket),
    (r'/(.*)', tornado.web.FallbackHandler, dict(
        fallback=tornado.wsgi.WSGIContainer(myapp_wsgi)
    )),
], debug=True)

if __name__ == '__main__':
    try:
        application.listen(int(os.environ.get("PORT",8000)))
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt: sys.exit(0)

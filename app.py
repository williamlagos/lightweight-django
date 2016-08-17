#!/usr/bin/env python
""" Application handler for WebSockets and Django using Tornado Web Server """

import os
import sys
import logging
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.wsgi
from helloworld.wsgi import application as myapp_wsgi

logging.basicConfig(filename='tornado.log', level=logging.DEBUG)

# Javascript Usage:
# var ws = new WebSocket('ws://localhost:8000/ws');
# ws.onopen = function(event){ console.log('socket open'); }
# ws.onclose = function(event){ console.log('socket closed'); }
# ws.onerror = function(error){ console.log('error:', err); }
# ws.onmessage = function(event){ console.log('message:', event.data); }
# # ... wait for connection to open
# ws.send('hello world')

class MyAppWebSocket(tornado.websocket.WebSocketHandler):
    """
    Simple Websocket echo handler. This could be extended to
    use Redis PubSub to broadcast updates to clients.
    """

    clients = set()

    def data_received(self, chunk):
        """ Data received method """
        pass

    def check_origin(self, origin):
        """ WebSocket Check Origin method """
        return True

    def open(self):
        """ WebSocket Open method """
        logging.info('Client connected')
        MyAppWebSocket.clients.add(self)

    def on_message(self, message):
        """ WebSocket On Message method """
        logging.debug('Received message %s', message)
        MyAppWebSocket.broadcast(message)

    def on_close(self):
        """ WebSocket On Close method """
        logging.info('Client disconnected')
        if self in MyAppWebSocket.clients:
            MyAppWebSocket.clients.remove(self)

    @classmethod
    def broadcast(cls, message):
        """ WebSocket Broadcast method """
        for client in cls.clients:
            client.write_message(message)

def start():
    """ Main application function """
    application = tornado.web.Application([
        (r'/ws', MyAppWebSocket),
        (r'/(.*)', tornado.web.FallbackHandler, dict(
            fallback=tornado.wsgi.WSGIContainer(myapp_wsgi)
        )),
    ], debug=True)
    application.listen(int(os.environ.get("PORT", 8000)))
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    try:
        start()
    except KeyboardInterrupt:
        sys.exit(0)

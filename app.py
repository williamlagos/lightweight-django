#!/usr/bin/env python
""" Application handler for WebSockets and Django using Tornado Web Server """

import time
import signal
import logging
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.wsgi
from kombi.wsgi import application as myapp_wsgi
from tornado.options import define, parse_command_line, options

# logging.basicConfig(filename='tornado.log', level=logging.DEBUG)

define('debug', default=False, type=bool, help='Run in debug mode')
define('port', default=8000, type=int, help='Server port')
define('allowed_hosts', default='localhost:8000', multiple=True,
       help='Allowed hosts for cross domain connections')

class AuctionWebSocket(tornado.websocket.WebSocketHandler):
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

def shutdown(server):
    """ Exit function for server """
    loop = tornado.ioloop.IOLoop.instance()
    logging.info('Stopping server.')
    server.stop()
    def finalize():
        """ Stops the main loop and logs for exit """
        loop.stop()
        logging.info('Stopped.')
    loop.add_timeout(time.time() + 1.5, finalize)

def start():
    """ Main application function """
    parse_command_line()
    application = tornado.web.Application([
        (r'/ws', AuctionWebSocket),
        (r'/(.*)', tornado.web.FallbackHandler, dict(
            fallback=tornado.wsgi.WSGIContainer(myapp_wsgi)
        )),
    ], debug=options.debug)
    server = tornado.httpserver.HTTPServer(application)
    server.listen(options.port)
    signal.signal(signal.SIGINT, lambda sig, frame: shutdown(server))
    logging.info('Starting server on localhost:%s', options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    start()

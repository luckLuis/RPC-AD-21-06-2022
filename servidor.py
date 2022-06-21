from xmlrpc.server import SimpleXMLRPCServer

import logging
import os

logging.basicConfig(level=logging.INFO)

server=SimpleXMLRPCServer(
    ('localhost', 9000),
    logRequests=True
)

def list_contents(dir_name):
    logging.info('list_contents(%s)', dir_name)
    return os.listdir(dir_name)

def add(number1, number2):
    return number1 + number2

server.register_function(list_contents)
server.register_function(add)

try: 
    print('presione ctrl+c para salir')
    server.serve_forever()
except KeyboardInterrupt:
    print('saliendo')



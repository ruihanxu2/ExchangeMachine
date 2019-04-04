import socket
import socketserver
from threading import Thread
from socketserver import ThreadingTCPServer, TCPServer
from tables import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from transaction import transact
from creation import create
import xml.etree.ElementTree as et

class RequestHandler(socketserver.BaseRequestHandler):
    """
    Receive TCP requests and handle them
    """

    def handle(self):
        #print('Got connection from', self.client_address)
        engine = create_engine('postgresql://postgres:passw0rd@localhost:5432/EXCHANGEMACHINE')

        Session = sessionmaker(bind=engine)

        session = Session()




        while True:
            #print('entered loop')
            recv_message = self.request.recv(4096)
            #print('recv_message')

            if not recv_message:
                #print('break')
                break

            recv_message = recv_message.decode()
            #print(recv_message)
            recv_message = '\n'.join(recv_message.split("\r\n")[1:])
            root = et.fromstring(recv_message)

            if root.tag == 'transactions':
                res = transact(root, session)

                self.request.sendall(res.encode('utf-8'))

            if root.tag == 'create':
                res = create(root, session)
                self.request.sendall(res.encode('utf-8'))





if __name__ == '__main__':
    HOST = 'vcm-8940.vm.duke.edu'
    PORT = 12345
    # engine = create_engine('postgresql://postgres:passw0rd@localhost:5432/EXCHANGEMACHINE')
    #
    # Base.metadata.drop_all(engine)
    # Base.metadata.create_all(engine, checkfirst=True)


    print('session connnected')
    #server = TCPServer((HOST, PORT), RequestHandler)

    server = ThreadingTCPServer((HOST, PORT), RequestHandler)
    server.serve_forever()

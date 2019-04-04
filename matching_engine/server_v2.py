import socket
import socketserver
import threading
from threading import Thread
from socketserver import ThreadingTCPServer, TCPServer
from tables import Base
from concurrent.futures import ThreadPoolExecutor
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from transaction import transact
from creation import create
import xml.etree.ElementTree as et

def run(session, connection):
    # Wait for a connection

        print('session connnected')


        while 1:
            recv_message = connection.recv(4096)

            if recv_message:
                recv_message = recv_message.decode()

                recv_message = '\n'.join(recv_message.split("\r\n")[1:])
                root = et.fromstring(recv_message)

                if root.tag == 'transactions':
                    res = transact(root, session)

                    connection.send(res.encode('utf-8'))

                if root.tag == 'create':
                    res = create(root, session)
                    connection.send(res.encode('utf-8'))
            else:
                break
        connection.close()



if __name__ == '__main__':
    HOST = 'vcm-8940.vm.duke.edu'
    PORT = 12345
    # engine = create_engine('postgresql://postgres:passw0rd@localhost:5432/EXCHANGEMACHINE')
    #
    # Base.metadata.drop_all(engine)
    # Base.metadata.create_all(engine, checkfirst=True)

    server_address = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(server_address)
    sock.listen(1)

    engine = create_engine('postgresql://postgres:passw0rd@localhost:5432/EXCHANGEMACHINE')

    Session = sessionmaker(bind=engine)

    session = Session()

    thread_pool = ThreadPoolExecutor(max_workers=50)
    print('connection established')


    while 1:
        print('entering loop')
        connection, client_address = sock.accept()
        t = threading.Thread(target=run, args=(session, connection,))
        t.start()





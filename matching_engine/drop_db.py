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




if __name__ == '__main__':
    HOST = 'vcm-8940.vm.duke.edu'
    PORT = 12345
    engine = create_engine('postgresql://postgres:passw0rd@localhost:5432/EXCHANGEMACHINE')

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine, checkfirst=True)


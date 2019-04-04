from sqlalchemy import Column, String, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    userid = Column(Integer, primary_key=True) #pk
    balance = Column(Integer)

    def __init__(self, userid, balance):
        self.balance = balance
        self.userid = userid
class Position(Base):
    __tablename__ = 'position'
    pos_id = Column(Integer, primary_key=True)
    userid = Column(Integer) #fk
    symbol = Column(String)
    share = Column(Integer)

    def __init__(self, userid, symbol, share):
        self.userid = userid
        self.symbol = symbol
        self.share = share

class OrderList(Base):
    __tablename__='OrderList'
    orderid = Column(Integer, primary_key=True)  # pk
    userid = Column(Integer)
    symbol = Column(String)
    amount = Column(Integer)
    limit = Column(Float)
    status = Column(String) # open, cancanled or executed
    trade = Column(String) # sell or buy
    created_date = Column(DateTime)

    def __init__(self, userid, symbol, amount, limit, status, trade):

        self.userid = userid
        self.symbol = symbol
        self.amount = amount
        self.limit = limit
        self.status = status
        self.trade = trade
        self.created_date = datetime.datetime.utcnow()



'''
class SellList(Base):
    __tablename__ = 'SellList'
    orderid = Column(Integer, primary_key=True) #pk
    userid = Column(Integer)
    symbol = Column(String)
    amount = Column(Integer)
    limit = Column(Float)
    created_date = Column(DateTime)

    def __init__(self, orderid, userid, symbol, amount, limit):
        self.orderid = orderid
        self.userid = userid
        self.symbol = symbol
        self.amount = amount
        self.limit = limit
        self.created_date = datetime.datetime.utcnow()

class BuyList(Base):
    __tablename__ = 'BuyList'
    orderid = Column(Integer, primary_key=True)  # pk
    userid = Column(Integer)  # fk
    symbol = Column(String)
    amount = Column(Integer)
    limit = Column(Float)
    created_date = Column(DateTime)

    def __init__(self, orderid, userid, symbol, amount, limit):
        self.orderid = orderid
        self.userid = userid
        self.symbol = symbol
        self.amount = amount
        self.limit = limit
        self.created_date = datetime.datetime.utcnow()

class Executed(Base):
    __tablename__ = 'Executed'
    orderid = Column(Integer, primary_key=True)  # pk
    amount = Column(Integer)
    price = Column(Float)
    executed_date = Column(DateTime)
    def __init__(self, orderid, amount, price):
        self.orderid = orderid
        self.amount = amount
        self.price = price
        self.executed_date = datetime.datetime.utcnow()


class Canceled(Base):
    __tablename__ = 'Canceled'
    orderid = Column(Integer, primary_key=True)  # pk
    amount = Column(Integer)
    canceled_date = Column(DateTime)
    def __init__(self, orderid, amount):
        self.orderid = orderid
        self.amount = amount
        self.canceled_date = datetime.datetime.utcnow()

'''
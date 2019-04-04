import tables
import xml.etree.ElementTree as et
from sqlalchemy import asc, desc
from sqlalchemy import and_
from tables import User, Position, OrderList
from xml.etree.ElementTree import Element, SubElement
import datetime

def transact(root, session):

    transactions = Element('results')

    for order in root.findall('order'):
        sym = order.get('sym')
        amount = int(order.get('amount'))
        limit = float(order.get('limit'))
        # upper limit for buy, lower limit for sell
        if amount > 0:
            #buy
            buyer_id = int(root.get('account'))

            # put to order
            new_buy_list = OrderList(buyer_id, sym, amount, limit, 'open', 'buy')

            session.add(new_buy_list)
            session.commit()
            trans_id = new_buy_list.orderid
            # print('amount larget than 0 trans id is', trans_id)

            opened = SubElement(transactions, 'opened', {'sym': str(sym), 'amount': str(amount), 'limit': str(limit),
                                                         'id': str(new_buy_list.orderid)})

            to_sell = session.query(OrderList).filter(and_(OrderList.symbol == sym,
                                                           OrderList.limit <= limit,
                                                           OrderList.status == 'open',
                                                           OrderList.amount == amount,
                                                           OrderList.trade == 'sell')).order_by(OrderList.limit.asc()).first()
            to_buy = session.query(OrderList).filter_by(orderid = trans_id).first()

            if to_sell is None:
                pass
                #print('no selling order')
            else:
                #we have some match. But we need to check the amount. if
                seller_id = to_sell.userid


                #check balance
                buyer = session.query(User).filter_by(userid = buyer_id).first()
                seller = session.query(User).filter_by(userid = to_sell.userid).first()

                buyer_position = session.query(Position).filter_by(userid=buyer_id, symbol=sym).first()
                seller_position = session.query(Position).filter_by(userid=seller_id, symbol=sym).first()

                total_price = to_sell.limit*amount
                if buyer.balance >= total_price:

                    #balance for buyer and seller
                    buyer.balance -= total_price
                    seller.balance += total_price

                    # executed list

                    # print('add new_selled and new_bought to Executed list')


                    #update sell and buy list
                    to_sell.status = 'executed'
                    to_buy.status = 'executed'
                    # print('change both to executed')
                    #update position


                    if buyer_position is None:
                        new_pos = Position(buyer_id, sym, amount)
                        # print('add new pos to buyer position')
                        session.add(new_pos)

                    else:
                        # print('add the bought amount to buyer position')
                        buyer_position.share = buyer_position.share + amount

                    seller_position.share -= amount
                    if seller_position.share == 0:
                        seller_position.delete()

                    session.commit()

                else:
                    error = SubElement(transactions, 'error', {'sym': str(sym), 'amount': str(amount), 'limit': str(limit),
                                                                 'id': str(trans_id)})
                    error.text='Buyer balance not enough.'



        if amount < 0:
            # sell
            amount = -amount
            seller_id = int(root.get('account'))

            # put to order
            new_sell_list = OrderList(seller_id, sym, amount, limit, 'open', 'sell')

            session.add(new_sell_list)
            session.commit()

            trans_id = new_sell_list.orderid
            # print('amount smaller than trans id is', trans_id)

            opened = SubElement(transactions, 'opened', {'sym': str(sym), 'amount': str(amount), 'limit': str(limit),
                                                         'id': str(new_sell_list.orderid)})

            to_buy = session.query(OrderList).filter(and_(OrderList.symbol == sym,
                                                          OrderList.limit <= limit,
                                                          OrderList.status == 'open',
                                                          OrderList.amount == amount,
                                                          OrderList.trade == 'buy')).order_by(OrderList.limit.asc()).first()

            to_sell = session.query(OrderList).filter_by(orderid=trans_id).first()

            if to_buy is None:
                pass
                # print('no buyer order')

            else:
                # we have some match. But we need to check the amount. if
                seller_id = to_sell.userid


                # check balance
                buyer = session.query(User).filter_by(userid=buyer_id).first()
                seller = session.query(User).filter_by(userid=to_sell.userid).first()

                buyer_position = session.query(Position).filter_by(userid=buyer_id, symbol=sym).first()
                seller_position = session.query(Position).filter_by(userid=seller_id, symbol=sym).first()

                total_price = to_sell.limit * amount
                if buyer.balance >= total_price:

                    # balance for buyer and seller
                    buyer.balance -= total_price
                    seller.balance += total_price

                    # executed list

                    # print('add new_selled and new_bought to Executed list')

                    # update sell and buy list
                    to_sell.created_date = datetime.datetime.utcnow()
                    to_sell.status = 'executed'
                    to_buy.created_date = datetime.datetime.utcnow()
                    to_buy.status = 'executed'
                    # print('executed')
                    # update position

                    if buyer_position is None:
                        new_pos = Position(buyer_id, sym, amount)
                        # print('add new pos to buyer position')
                        session.add(new_pos)

                    else:
                        # print('add the bought amount to buyer position')
                        buyer_position.share = buyer_position.share + amount

                    seller_position.share -= amount
                    if seller_position.share == 0:
                        seller_position.delete()

                    session.commit()

                else:
                    error = SubElement(transactions, 'error',
                                       {'sym': str(sym), 'amount': str(amount), 'limit': str(limit),
                                        'id': str(trans_id)})
                    error.text = 'Buyer balance not enough.'






    for query in root.findall('query'):
        query_id = int(query.get('id'))
        status_tag = SubElement(transactions, 'status', {'id': str(query_id)})

        trans = session.query(OrderList).filter_by(orderid=query_id).first()

        if trans is not None:
            # print('Found query in OrderList')
            shares = trans.amount
            status = trans.status
            price = trans.limit
            time = trans.created_date

            if status == 'open':
                open = SubElement(status_tag, 'open', {'shares': str(shares)})
            elif status == 'canceled':
                canceled = SubElement(status_tag, 'canceled', {'shares': str(shares), 'time': str(time)})
            elif status == 'executed':
                executed = SubElement(status_tag, 'executed', {'shares': str(shares),
                                                               'price': str(price),
                                                               'time': str(time)})




    for cancel in root.findall('cancel'):
        cancel_id = int(cancel.get('id'))
        canceled = SubElement(transactions, 'canceled', {'id': str(cancel_id)})

        trans = session.query(OrderList).filter_by(orderid=cancel_id).first()
        if trans is not None:

            if trans.status == 'canceled':
                pass
            if trans.status == 'executed':
                executed = SubElement(canceled, 'executed', {'share': str(trans.amount),
                                                             'price': str(trans.limit),
                                                             'time': str(trans.created_date)})
            if trans.status == 'open':
                trans.status = 'canceled'
                trans.created_date = datetime.datetime.utcnow()
                canceled2 = SubElement(canceled, 'canceled', {'share': str(trans.amount),
                                                              'time': str(trans.created_date)})

                session.commit()

            continue



    res = str(et.tostring(transactions, encoding='utf8', method='xml'),'utf-8')
    return str(len(res))+'\r\n'+res
"""
<transactions id="ACCOUNT_ID"> #contains 1 or more of the below children
    <order sym="SYM" amount="AMT" limit="LMT"/>
    <query id="TRANS_ID">
    <cancel id="TRANS_ID">
</transactions>"""
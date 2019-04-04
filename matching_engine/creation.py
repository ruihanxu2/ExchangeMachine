from tables import User, Position
import xml.etree.ElementTree as et
from xml.etree.ElementTree import Element, SubElement, Comment
import tables
from xml.dom import minidom


def create(root, session):
    result = Element('result')

    for child in root:
        if child.tag == 'account':
            id = int(child.get('id'))
            balance = float(child.get('balance'))

            # search data base to see if there is this account, create or skip
            if session.query(User).filter_by(userid = id).first():
                # already exist, <error>
                # # print('acc already exist')
                error = SubElement(result, 'error', {'id': str(id)})
                error.text = 'This account already exist.'

            else:
                # print('creating acc')
                new_user = User(id, balance)
                session.add(new_user)
                session.commit()
                created = SubElement(result, 'created', {'id': str(id)})


        #add

        elif child.tag == 'symbol':
            sym = child.get('sym')
            for account in child.findall('account'):
                acc_id = int(account.get('id'))
                # print('account id is', acc_id)
                share = int(account.text)

                # if sym exist, add
                # else create

                position = session.query(Position).filter_by(userid = acc_id, symbol = sym).first()
                if position is None:
                    # print('create position')
                    new_pos = Position(acc_id, sym, share)
                    session.add(new_pos)
                    session.commit()
                else:
                    # print('update position')
                    position.share += share
                    session.commit()
                created = SubElement(result, 'created', {'sym': str(sym), 'id': str(acc_id)})


        else:
            error = SubElement(result, 'error')
            error.text = 'Invalid tag.'
    # print(result)
    res = str(et.tostring(result, encoding='utf8', method='xml'), 'utf-8')
    return str(len(res)) + '\r\n' + res
"""
from xml.etree.ElementTree import Element, SubElement, Comment, tostring

top = Element('top')

comment = Comment('Generated for PyMOTW')
top.append(comment)

child = SubElement(top, 'child')
child.text = 'This child contains text.'

child_with_tail = SubElement(top, 'child_with_tail')
child_with_tail.text = 'This child has regular text.'
child_with_tail.tail = 'And "tail" text.'

child_with_entity_ref = SubElement(top, 'child_with_entity_ref')
child_with_entity_ref.text = 'This & that'

# print tostring(top)




$ python ElementTree_create.py

<top><!--Generated for PyMOTW--><child>This child contains text.</ch
ild><child_with_tail>This child has regular text.</child_with_tail>A
nd "tail" text.<child_with_entity_ref>This &amp; that</child_with_en
tity_ref></top>

"""






"""<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>"""


"""<?xml version="1.0" encoding="UTF-8"?>
<create>
    <account id="123456" balance="1000"/>
    <symbol sym="SPY">
        <account id="123456">100000</account>
    </symbol>
</create>"""
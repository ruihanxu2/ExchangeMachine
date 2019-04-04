import socket
import threading
import random
from concurrent.futures import ThreadPoolExecutor


def runTest():
    for i in range(2):  # Modify parameter
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('vcm-8940.vm.duke.edu', 12345))


        send_option = 2
        print(send_option)

        if send_option == 0:
            print(send_option)

            test_message = '173\r\n' \
                           '<?xml version=\'1.0\' encoding=\'UTF-8\'?>\r\n' \
                           '<create>\r\n' \
                           '  <account id=\'1\' balance=\'11111\'/>\r\n' \
                           '  <account id=\'2\' balance=\'222\'/>\r\n' \
                           '  <account id=\'4\' balance=\'3333\'/>\r\n' \
                           '  <symbol sym=\'SPY\'>\r\n' \
                           '    <account id=\'1\'>100000</account>\r\n' \
                           '  </symbol>\r\n' \
                           '  <symbol sym=\'SPY\'>\r\n' \
                           '    <account id=\'1\'>979</account>\r\n' \
                           '    <account id=\'3\'>356</account>\r\n' \
                           '  </symbol>\r\n' \
                           '</create>\r\n\r\n'
        elif send_option == 1:
            print(send_option)

            test_message = '173\r\n' \
                           '<?xml version=\'1.0\' encoding=\'UTF-8\'?>\r\n' \
                           '<transactions account = \'1\'>\r\n' \
                           '<order sym =\'SPY\' amount=\'100\' limit=\'123.45\'/>\r\n' \
                           '<order sym =\'XYZ\' amount=\'89\' limit=\'37.00\'/>\r\n' \
                           '<order sym =\'ABC\' amount=\'-42\' limit=\'11.43\'/>\r\n' \
                           '</transactions>\r\n\r\n'
        elif send_option == 2:
            print(send_option)

            test_message = '173\r\n' \
                           '<?xml version=\'1.0\' encoding=\'UTF-8\'?>\r\n' \
                           '<transactions account = \'12345\'>\r\n' \
                           '<order sym =\'SPY\' amount=\'100\' limit=\'145.67\'/>\r\n' \
                           '<order sym =\'XYZ\' amount=\'99\' limit=\'42.00\'/>\r\n' \
                           '<order sym =\'ABC\' amount=\'-42\' limit=\'1.43\'/>\r\n' \
                           '<query id=\'1\'/>\r\n' \
                           '<query id=\'2\'/>\r\n'\
                           '<query id=\'3\'/>\r\n' \
                           '<cancel id=\'1\'/>\r\n' \
                           '<query id=\'1\'/>\r\n' \
                           '</transactions>\r\n\r\n'

        elif send_option == 3:
            print(send_option)

            test_message = '173\r\n' \
                           '<?xml version=\'1.0\' encoding=\'UTF-8\'?>\r\n' \
                           '<create>\r\n' \
                           '  <account id=\'10\' balance=\'1000\'/>\r\n' \
                           '  <symbol sym=\'EQGD\'>\r\n' \
                           '    <account id=\'10\'>100000</account>\r\n' \
                           '  </symbol>\r\n' \
                           '</create>\r\n\r\n'

        print(test_message)

        s.sendall(str.encode(test_message, 'utf-8'))


        '''
        timing here
        '''

        recv_message = s.recv(4096)

        print(recv_message.decode())



if __name__ == '__main__':
    thread_pool = ThreadPoolExecutor(max_workers=50)  # Modify

    for i in range(1):
        future = thread_pool.submit(runTest)

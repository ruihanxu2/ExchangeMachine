import socket
import threading
import random
from concurrent.futures import ThreadPoolExecutor
import time
import sys


if __name__ == '__main__':
    start_total = time.time()
    no_user = int(sys.argv[1])
    for i in range(no_user):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('vcm-8940.vm.duke.edu', 12345))

        set_up_user = '173\r\n' \
                      '<?xml version=\'1.0\' encoding=\'UTF-8\'?>\r\n' \
                      '<create>\r\n' \
                      '  <account id=\''+str(i)+'\' balance=\'11111\'/>\r\n' \
                      '  <symbol sym=\'SPY\'>\r\n' \
                      '    <account id=\''+str(i)+'\'>100000</account>\r\n' \
                      '  </symbol>\r\n' \
                      '  <symbol sym=\'XYZ\'>\r\n' \
                      '    <account id=\'' + str(i) + '\'>100000</account>\r\n' \
                      '  </symbol>\r\n' \
                      '  <symbol sym=\'ABC\'>\r\n' \
                      '    <account id=\'' + str(i) + '\'>100000</account>\r\n' \
                      '  </symbol>\r\n' \
                      '</create>\r\n\r\n'
        s.sendall(str.encode(set_up_user, 'utf-8'))
        recv_message = s.recv(4096)
        set_up_pos = '173\r\n' \
                     '<?xml version=\'1.0\' encoding=\'UTF-8\'?>\r\n' \
                     '<transactions account = \''+str(i)+'\'>\r\n' \
                     '<order sym =\'SPY\' amount=\'100\' limit=\'123.45\'/>\r\n' \
                     '<order sym =\'XYZ\' amount=\'89\' limit=\'37.00\'/>\r\n' \
                     '<order sym =\'ABC\' amount=\'-42\' limit=\'11.43\'/>\r\n' \
                     '</transactions>\r\n\r\n'
        s.sendall(str.encode(set_up_pos, 'utf-8'))
        recv_message = s.recv(4096)
        st.close()

    print('setting up finished')
    end_total = time.time()
    print ('total time:', end_total - start_total)

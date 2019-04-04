import socket
import threading
import random
from concurrent.futures import ThreadPoolExecutor
import time

def runTest(threadno):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('vcm-8940.vm.duke.edu', 12345))
    start = time.time()
    for i in range(250):  # Modify parameter

        test_message = '173\r\n<?xml version=\'1.0\' encoding=\'UTF-8\'?>\r\n\
        <transactions account = \''+str(i)+'\'>\r\n\
        <query id=\''+str(threadno*i)+'\'/>\r\n\
        <query id=\'' + str(threadno*i) + '\'/>\r\n\
        <query id=\'' + str(threadno*i) + '\'/>\r\n\
        <query id=\'' + str(threadno*i) + '\'/>\r\n\
        <query id=\'' + str(threadno*i) + '\'/>\r\n\
        <query id=\'' + str(threadno*i) + '\'/>\r\n\
        <query id=\'' + str(threadno*i) + '\'/>\r\n\
        <query id=\'' + str(threadno*i) + '\'/>\r\n\
        <query id=\'' + str(threadno*i) + '\'/>\r\n\
        <query id=\'' + str(threadno*i) + '\'/>\r\n\
        </transactions>\r\n\r\n'




        s.sendall(str.encode(test_message, 'utf-8'))

        recv_message = s.recv(4096)

        #print(recv_message.decode())

    end = time.time()
    print('The execution time for', threadno, 'is', end - start)



if __name__ == '__main__':
    start_total = time.time()

    t1 = threading.Thread(target=runTest, args=(1,))
    t2 = threading.Thread(target=runTest, args=(2,))
    t3 = threading.Thread(target=runTest, args=(3,))
    t4 = threading.Thread(target=runTest, args=(4,))
    t5 = threading.Thread(target=runTest, args=(5,))
    t6 = threading.Thread(target=runTest, args=(6,))
    t7 = threading.Thread(target=runTest, args=(7,))
    t8 = threading.Thread(target=runTest, args=(8,))
    t9 = threading.Thread(target=runTest, args=(1,))
    t10 = threading.Thread(target=runTest, args=(2,))
    t11= threading.Thread(target=runTest, args=(3,))
    t12= threading.Thread(target=runTest, args=(4,))
    t13= threading.Thread(target=runTest, args=(5,))
    t14= threading.Thread(target=runTest, args=(6,))
    t15= threading.Thread(target=runTest, args=(7,))
    t16= threading.Thread(target=runTest, args=(8,))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()
    t15.start()
    t16.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()
    t13.join()
    t14.join()
    t15.join()
    t16.join()

    end_total = time.time()

    print ('total time:', end_total - start_total)

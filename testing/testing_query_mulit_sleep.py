import socket
import threading
import random
from concurrent.futures import ThreadPoolExecutor
import time

def runTest(threadno):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('vcm-8940.vm.duke.edu', 12345))
    start = time.time()
    for i in range(100):  # Modify parameter

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


    t1.start()
    time.sleep(10)
    t2.start()
    time.sleep(10)
    t3.start()
    time.sleep(10)
    t4.start()
    time.sleep(10)


    t1.join()
    t2.join()
    t3.join()
    t4.join()


    end_total = time.time()

    print ('total time:', end_total - start_total)

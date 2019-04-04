import socket
import threading
import random
from concurrent.futures import ThreadPoolExecutor
import time

def runTest(threadno):
    start = time.time()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('vcm-8940.vm.duke.edu', 12345))

    for i in range(4000):  # Modify parameter

        test_message = '173\r\n<?xml version=\'1.0\' encoding=\'UTF-8\'?>\r\n\
        <transactions account = \''+str(i)+'\'>\r\n\
        <query id=\''+str(i)+'\'/>\r\n\
        <query id=\'' + str(i) + '\'/>\r\n\
        <query id=\'' + str(i) + '\'/>\r\n\
        <query id=\'' + str(i) + '\'/>\r\n\
        <query id=\'' + str(i) + '\'/>\r\n\
        <query id=\'' + str(i) + '\'/>\r\n\
        <query id=\'' + str(i) + '\'/>\r\n\
        <query id=\'' + str(i) + '\'/>\r\n\
        <query id=\'' + str(i) + '\'/>\r\n\
        <query id=\'' + str(i) + '\'/>\r\n\
        </transactions>\r\n\r\n'




        s.sendall(str.encode(test_message, 'utf-8'))

        recv_message = s.recv(4096)

        #print(recv_message.decode())
    end = time.time()
    print('The execution time for', threadno, 'is', end - start)



if __name__ == '__main__':
    start_total = time.time()
    thread_pool = ThreadPoolExecutor(max_workers=50)  # Modify


    for i in range(1):
        future = thread_pool.submit(runTest, (i))
    end_total = time.time()

    #print ('total time:', end_total - start_total)

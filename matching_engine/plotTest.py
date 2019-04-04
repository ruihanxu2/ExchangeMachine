from matplotlib import pyplot as plt
import numpy as np

# x = [1,10,100,1000,10000]
# y4 = [0.11,0.27,3.01,42.03,400.11]
# y2 = [0.17, 0.45, 4.95, 46.14, 579.78]
# y1 = [0.27, 0.70, 7.52, 50.059, 851.81]
# plt.figure()
#
# plt.plot(x, y4, label= '4core')
# plt.plot(x, y2, label= '2core')
# plt.plot(x, y1, label= '1core')
# plt.xlabel('created_user')
# plt.ylabel('time')
# plt.xscale('log')
# plt.legend()

# plt.plot(iter, accuracy_test)

# plt.show()


x = [1,10,20 ,30,40, 50, 100]
y4 = [0.09912896156311035, 0.4830820560455322,1.1172358989715576, 2.9572641849517822, 5.272462844848633, 2.8060879707336426 , 9.704121351242065]
y3 = [0.18659591674804688, 0.5013267993927002, 0.9464550018310547,  2.3011677265167236, 2.1853599548339844, 2.4664762020111084 , 5.037349462509155]
y2 = [0.10730838775634766, 0.7172501087188721,1.050100326538086, 1.559495210647583, 2.1013357639312744, 2.336958885192871 , 10.61022162437439]
y1 = [0.10529637336730957, 0.5601119995117188,1.2551164627075195,  1.5098791122436523, 2.057797908782959, 2.5038645267486572 , 9.484577655792236]
plt.plot(x, y4, label= 'TCPserver: 4 cores')
plt.plot(x, y3, label= 'threadingTCPserver: 4 cores')
plt.plot(x, y2, label= 'TCPserver: 2 cores')
plt.plot(x, y1, label= 'threadingTCPserver: 2 cores')
plt.xlabel('created_user')
plt.ylabel('time')
plt.title('Comparison of single thread vs multithread')
plt.xscale('log')
plt.legend()
plt.show()
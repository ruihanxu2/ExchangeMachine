# HW4 Exchange Matching Engine
We used python for this assignment. The overview of the assignment can be found in written up.

The project can run normally without Docker, that is to run ```python3 server.py``` and then run ```python3 testing.py```.

However, we can not make it work using Docker. The error message is:
```
matching_server_1  | Traceback (most recent call last):
matching_server_1  |   File "server.py", line 65, in <module>
matching_server_1  |     server = TCPServer((HOST, PORT), RequestHandler)
matching_server_1  |   File "/usr/local/lib/python3.7/socketserver.py", line 452, in __init__
matching_server_1  |     self.server_bind()
matching_server_1  |   File "/usr/local/lib/python3.7/socketserver.py", line 466, in server_bind
matching_server_1  |     self.socket.bind(self.server_address)
matching_server_1  | OSError: [Errno 99] Cannot assign requested address
```
It seems that with Docker, the program can not bind socket normally.

Our Dockerfile is under matching_engine folder.
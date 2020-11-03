#!/usr/bin/python3

import socket
import random
import sys

headers = [
    "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:82.0) Gecko/20100101 Firefox/82.0",
    "Accept-Language: en-US,en;q=0.5",
    "Connection: keep-alive"
]

tests = []

# Used in formating the requests
BASE_REQUEST = "GET /?{} HTTP/1.1\r\n"
PRECEDING_REQUEST = '{}\r\n'

# Exit codes
SUCCESS = 0
FAILURE = 1


def gen_socket(ip, https=True) -> socket:
    # This is the deafult web HTTPS port
    int: port = 443
    if https:
        # This is the deafult web HTTP port
        port = 80

    # Setting up the socket we're going to use to connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(4)
    s.connect((ip, port))

    int: rand_int = random.randint(0, 2000)
    request = BASE_REQUEST.format(rand_int).encode('UTF-8')
    s.send(request)

    for header in headers:
        r = PRECEDING_REQUEST.format(header).encode('UTF-8')
        s.send(r)

    return s


def check_and_assign_args(arg_ip, arg_port_type, arg_num_sockets, arg_time):

    # TODO: Work on assertions

    # if(type(int(arg_num_sockets)) is not (int)):
    #     print("Number of sockets:", arg_num_sockets, "is not an int")
    #     exit(FAILURE)

    # if(type((arg_time)) is not (int)):
    #     print("Time:", arg_time, "is not an int")
    #     exit(FAILURE)

    ip = arg_ip
    is_https = False

    if (str(arg_port_type) == "https"):
        is_https = True

    num_sockets = int(arg_num_sockets)
    time = int(arg_time)

    return ip, is_https, num_sockets, time


if __name__ == "__main__":

    if len(sys.argv) < 5:
        # Invalid use prints usage
        print(
            "Usage\t| python {} <website/ip> <http or https> <# of sockets> <timeout>\n".format(sys.argv[0]))
        print("Example\t| python {} floridapoly.edu http 100 10".format(
            sys.argv[0]))
        print("\t| python {} floridapoly.edu https 150 5".format(sys.argv[0]))
        exit(FAILURE)

    ip, is_https, num_sockets, time = check_and_assign_args(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
        sys.argv[4],
    )

    print(ip, is_https, num_sockets, time)

    exit(SUCCESS)

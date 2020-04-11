import socket, time

SERVER=None
CLIENT_CONNECTION = []

#class Server(self, scenario_name):

# target=foo(34)()

# closures
class Server:

    # Server('foo')
    def __init__(self, scenario_name):
        self.scenario_name = scenario_name

    def wait_for_client_connection(self):
        conn, addr = SERVER.accept()
        print("++++++++++ FOUND CLIENT")
        print("SENDING NAME OF THE SCENARIO")
        conn.send(bytes(self.scenario_name, "utf8"))
        CLIENT_CONNECTION.append(conn)
        print(get_connection())

def setup():
    global SERVER
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind(('127.0.0.1', 10423))
    SERVER.listen(1)
    print("Socket is ready.")

def get_connection():
    if len(CLIENT_CONNECTION) > 0:
        return CLIENT_CONNECTION[0]
    else:
        return None

def close_connection():
    global CLIENT_CONNECTION
    conn_check = get_connection()
    print('conn_check is ' + str(conn_check))
    if conn_check is not None:
        print('about to close')
        conn_check.send(bytes("OK", "utf8"))
        time.sleep(10)
        print('sent')
        conn_check.close()
        print('closed')
        CLIENT_CONNECTION = []
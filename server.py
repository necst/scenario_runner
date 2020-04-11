import socket

SERVER=None
CLIENT_CONNECTION = []

def setup():
    global SERVER
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind(('127.0.0.1', 10423))
    SERVER.listen(1)
    print("Socket is ready.")

def wait_for_client_connection():
    conn, addr = SERVER.accept()
    print("++++++++++ FOUND CLIENT")
    CLIENT_CONNECTION.append(conn)
    print(get_connection())

def get_connection():
    if len(CLIENT_CONNECTION) > 0:
        return CLIENT_CONNECTION[0]
    else:
        return None

def close_connection():
    global CLIENT_CONNECTION
    conn_check = get_connection()
    if conn_check is not None:
        conn_check.send(bytes("OK", "utf8"))
        conn_check.close()
        CLIENT_CONNECTION = []
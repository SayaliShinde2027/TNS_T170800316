import socket
import threading
from proxy.handler import handle_client

PROXY_HOST = "127.0.0.1"
PROXY_PORT = 9090


def start_proxy():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((PROXY_HOST, PROXY_PORT))
    server.listen(100)

    print(f"🔥 Proxy running on {PROXY_HOST}:{PROXY_PORT}")

    while True:
        client_socket, addr = server.accept()
        threading.Thread(target=handle_client, args=(client_socket,), daemon=True).start()


if __name__ == "__main__":
    start_proxy()
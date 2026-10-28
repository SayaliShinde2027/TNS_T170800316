from proxy.server import start_proxy
from database.db import init_db

if __name__ == "__main__":
    print("Starting Phish-Guard...")

    init_db()  # 🔥 NEW LINE

    start_proxy()
#!/bin/python3

from socket import *
import time
from threading import Thread, Lock

start_time = time.time()
print_lock = Lock()

def scan_port(target, port):
    """Function to scan a single port"""
    try:
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(0.5)  # Add timeout to avoid hanging
        conn = s.connect_ex((target, port))
        if conn == 0:
            with print_lock:  # Prevent print collisions in threads
                print(f'Port {port}: OPEN')
        s.close()
    except Exception:
        pass

def main():
    target = input('Enter host for scanning: ')
    t_IP = gethostbyname(target)   # Resolve the target to an IP address
    print('Starting scanning on host:', t_IP)

    threads = []
    for port in range(0, 65535):
        thread = Thread(target=scan_port, args=(t_IP, port))
        threads.append(thread)
        thread.start()

        # Limit the number of concurrent threads
        while len(threads) > 100:  # Maximum 100 threads
            for t in threads:
                if not t.is_alive():
                    threads.remove(t)

    # Ensure all threads finish before calculating the total time
    for t in threads:
        t.join()

    print('Time taken:', time.time() - start_time)

if __name__ == '__main__':
    main()

import socket
import threading

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"[+] Port {port} is OPEN")
        sock.close()
    except:
        pass

def threader(ip, ports):
    threads = []
    for port in ports:
        t = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()

def main():
    print("\n*** Simple Port Scanner ***")
    target = input("Enter Target IP/Hostname: ")
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("[!] Hostname could not be resolved.")
        return
    print(f"\nScanning Target: {ip}")
    start_port = int(input("Enter start port (e.g., 1): "))
    end_port = int(input("Enter end port (e.g., 1024): "))
    ports = range(start_port, end_port + 1)
    threader(ip, ports)

if __name__ == "__main__":
    main()

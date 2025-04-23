import socket
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import datetime

logs = "/logs/honeypot.log"

def logger(protocol, ip, port, data):
    log_entry = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "protocol": protocol,
        "ip": ip,
        "port": port,
        "data": data.decode(errors='ignore')[:200]
    }
    with open(logs, "a") as f:
        f.write(json.dumps(log_entry) + "\n")
    print(f"[{protocol}] {ip}:{port} logged.")

def rtspServer():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind(('0.0.0.0', 554))
    soc.listen(5)
    print("RTSP server listening on port 554...")
    while True:
        conn, addr = soc.accept()
        data = conn.recv(1024)
        if data:
            print(f"[RTSP] Connection from {addr[0]}:{addr[1]} - DATA: {data[:100]}")
            with open("/logs/rtsp.log", "a") as f:
                logger(f"{addr[0]}:{addr[1]} - {data.decode(errors='ignore')}\n")
        conn.close()

def onvifServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 8000))
    s.listen(5)
    print("ONVIF server listening on port 8000...")
    while True:
        conn, addr = s.accept()
        data = conn.recv(1024)
        if b"<SOAP" in data or b"Probe" in data:
            logger("ONVIF", addr[0], addr[1], data)
        conn.close()

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_body = self.rfile.read(content_length)
        logger("HTTP", self.client_address[0], self.client_address[1], post_body)
        self.send_response(403)
        self.end_headers()

    def log_message(self, format, *args):
        return 

def http():
    httpd = HTTPServer(('0.0.0.0', 8888), handler)
    print("HTTP server listening on port 8888...")
    httpd.serve_forever()

def cowrie():
    with open("/logs/cowrie.json", "r") as f:
        for line in f:
            print("[SSH-HONEYPOT]", line)

if __name__ == "__main__":
    threading.Thread(target=rtspServer, daemon=True).start()
    threading.Thread(target=onvifServer, daemon=True).start()
    threading.Thread(target=handler, daemon=True).start()

    while True:
        pass
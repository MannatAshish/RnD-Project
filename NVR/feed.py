import socket

HOST = '0.0.0.0'
PORT = 554

response = """RTSP/1.0 200 OK
CSeq: 1
Content-Base: rtsp://172.19.17.46/test/
Content-Type: application/sdp
Content-Length: 460

v=0
o=- 9 2 IN IP4 127.0.0.1
s=Stream 1
t=0 0
m=video 0 RTP/AVP 96
a=rtpmap:96 H264/90000
a=control:streamid=0
"""

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"RTSP Server running on rtsp://{HOST}:{PORT}...")
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected from {addr}")
                data = conn.recv(1024)
                if b"OPTIONS" in data or b"DESCRIBE" in data:
                    print("Received OPTIONS or DESCRIBE request")
                    conn.sendall(response.encode())
                conn.close()

if __name__ == "__main__":
    main()
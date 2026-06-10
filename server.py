import http.server
import socketserver
import os
import sys
import socket

if len(sys.argv) < 2:
    print("Usage: python3 server.py <dossier>")
    sys.exit(1)

dossier = sys.argv[1]
os.chdir(dossier)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
except Exception:
    ip = "127.0.0.1"
s.close()

PORT = 8000

print("\033[92mVotre adresse de serveur:\033[0m http://" + ip + ":" + str(PORT))
print("\033[94mVotre dossier partager:\033[0m " + dossier)

handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    httpd.serve_forever()


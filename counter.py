import http.server
import random
from prometheus_client import start_http_server

PORT = 8000
METRICS_PORT =8001

class HandleRequests(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes('{"message":"Hello World"}',"utf-8"))
        self.wfile.flush()
        self.wfile.close()

if __name__=="__main__":
    start_http_server(METRICS_PORT)
    server =http.server.HTTPServer(('localhost',PORT),HandleRequests)
    server.serve_forever()
import http.server
import random
from prometheus_client import start_http_server, Counter, Gauge
import time

no_of_requests=Counter('app_requests_count',' total no of requests',['app_name','endpoint'])
total_requests_now=Gauge('app_requests_now','number of requests currently processed')

PORT = 8000
METRICS_PORT =8001

class HandleRequests(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        no_of_requests.labels('rest_api',self.path).inc()
        total_requests_now.inc()
        time.sleep(5)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes('{"message":"Hello World"}',"utf-8"))
        total_requests_now.dec()
        self.wfile.close()

if __name__=="__main__":
    start_http_server(METRICS_PORT)
    server =http.server.HTTPServer(('localhost',PORT),HandleRequests)
    server.serve_forever()
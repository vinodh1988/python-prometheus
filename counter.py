import http.server
import random
from prometheus_client import Summary, start_http_server, Counter, Gauge, Histogram
import time

no_of_requests=Counter('app_requests_count',' total no of requests',['app_name','endpoint'])
total_requests_now=Gauge('app_requests_now','number of requests currently processed')
items_served= Histogram('items_served_in_one_request','number of items served in one request', buckets= [0,10,20,30,40,50,60,70,100])
items_served_summary =Summary('items_served_summary',"summary of items served")
PORT = 8000
METRICS_PORT =8001

class HandleRequests(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        no_of_requests.labels('rest_api',self.path).inc()
        #total_requests_now.inc()
        random_number=random.random()*100
        items_served.observe(random_number)
        items_served_summary.observe(random_number)
        #time.sleep(5)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(bytes('{"message":"Hello World "'+str(random_number)+"}","utf-8"))
        #total_requests_now.dec()
        self.wfile.close()

if __name__=="__main__":
    start_http_server(METRICS_PORT)
    server =http.server.HTTPServer(('localhost',PORT),HandleRequests)
    server.serve_forever()
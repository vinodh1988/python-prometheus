from prometheus_client import CollectorRegistry , Gauge, push_to_gateway
import random;
registry=CollectorRegistry()

gauge=Gauge('erros_now','errors in the system at this point',registry=registry)

while True:
    random_number=random.random()*1000
    print(random_number)
    if(random_number%2==0):
        gauge.inc()
    else:
        gauge.dec()

    if(int(random_number)==540):
        break
    push_to_gateway('http://13.233.126.246:9091/',job="Short Job",registry=registry)
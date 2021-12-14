import boto3
import json
import datetime  

import random

clientes = ['juliana','sara','danilo', 'wellington', 'bigode']
statusPossiveis = ['pedido feito','montando', 'no forno','saiu do forno', 'embalando','pronto']

peeker = random.SystemRandom()

eventBridge = boto3.client('events')

def put_events(eventBus, source, detailType, detail):
    response = eventBridge.put_events(
        Entries=[
            {
                'Time': datetime.datetime.now(),
                'Source': source,
                'DetailType': detailType,
                'Detail': json.dumps(detail),
                'EventBusName': eventBus,
            }
        ]
    )
    print("EventBridge Response: {}".format(json.dumps(response)))
    
def makeEvent(status, pedido, cliente):
    today = datetime.datetime.now()
    eventBus="pizzaria"
    source = "com.aws.pizzaria"
    detailType = "Alteracao Pizza"
    detail = {
      "pedido": str(pedido),
      "status": status,
      "cliente": cliente,
      "time": str(today)
    }
    put_events(eventBus, source, detailType, detail)

for i in range(20):
   cliente = peeker.choice(clientes)
   print(i)
   for status in statusPossiveis:
       makeEvent(status, i, cliente)
       



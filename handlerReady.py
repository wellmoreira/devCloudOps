import json
import random
from sqsHandler import SqsHandler
    
def readyHandler(event, context):
    
    sqs = SqsHandler("https://sqs.us-east-1.amazonaws.com/725606180892/espera-entrega")
    
    pedido = {
      "pedido_id": event['detail']['pedido'],
      "status": event['detail']['status'],
      "cliente": event['detail']['cliente']
    }
    
    sqs.send(json.dumps(pedido))
    
    return event
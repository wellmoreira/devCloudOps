import json
import boto3
from boto3.dynamodb.conditions import Key
from baseDAO import BaseDAO
import random
from datetime import datetime
from sqsHandler import SqsHandler

dao = BaseDAO('eventos-pizzaria')

def allHandler(event, context):
    #response = dao.put_item({'pedido_id':'111', 'name': 'wellington'})
    response = dao.put_item(eval(json.dumps(event['detail'])))
    
    return response
    
def prontoHandler(event, context):
    print("event: {}".format(json.dumps(event)))
    
    sqs = SqsHandler("https://sqs.us-east-1.amazonaws.com/725606180892/espera-entrega")
    
    for detail in eval(json.dumps(event['detail'])):
        #payload = detail['body']
        #print(json.dumps(payload))
        sqs.send(detail)
    
    return event
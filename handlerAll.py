import json
import boto3
from boto3.dynamodb.conditions import Key
from baseDAO import BaseDAO
import random
from datetime import datetime

dao = BaseDAO('eventos-pizzaria')

def allHandler(event, context):
    response = dao.put_item(eval(json.dumps(event['detail'])))
    
    return response
    
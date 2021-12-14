import json
import random
    
def endHandler(event, context):
    print("event: {}".format(json.dumps(event)))
    
    return event
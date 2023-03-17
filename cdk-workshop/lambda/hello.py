import json
import requests

def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    res=requests.get("https://www.google.com/")
    print(res.status_code)
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Hello, CDK! You have hit {}\n'.format(event['path'])
    }
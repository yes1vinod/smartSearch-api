import json
import boto3
import base64
from datetime import datetime
import uuid
# import requests
s3 = boto3.client('s3')
BUCKET_NAME = 'vin-smart-search'

def lambda_handler(event, context):
    fileName = event["queryStringParameters"]["fileName"]
    client=boto3.client('rekognition')
    response=client.detect_text(Image={'S3Object':{'Bucket':'sam-app-s3uploadbucket-7n3cd8ezfenv','Name':fileName}})
    print('File Name >> ' + fileName)
    # now = datetime.now()
  
    # # file_content = base64.b64decode(event['body']['content'])
    # event_body = json.loads(event['body'])
    # print('==============================================')
    # # print('event_body >>' +event_body)
    # print('==============================================')
    # print('event_body content >>' +event_body['content'])
    # print('==============================================')
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "fileName": fileName,
            "response": response
        }),
    }
 
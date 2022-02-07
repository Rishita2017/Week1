import boto3
import json
client_s3 = boto3.client('s3')

def my_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        response = client_s3.get_object(Bucket=bucket, Key=key)
    print("Author : " + response['Metadata']['author'])
    print("Description : " + response['Metadata']['description'])
import json

def my_handler(event, context):
    print("Hello world")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello for lambda')
    }

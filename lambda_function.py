import json

def my_handler(event, context):
     s3=boto3.client("s3")
     if event:
        print("Event : ",event)
        fil_obj=event["Record"][0]
        filename=str(fil_obj['s3']['object']['key'])
        print("ilename:",filename)
        fileobj=s3.get_object(Bucket=Sourcebucket,Key=filename)
        print("fileobj",fileobj)
        filecontent=fileobj["Body"].read().decode('utf-8')
        print(filecontent)
       
   
   return {
        'statusCode': 200,
        'body': json.dumps('Hello for lambda')
    }

import boto3
s3_client=boto3.client('s3')
s3_client.create_bucket(Bucket='data_bucket')
s3_client.Object('data_bucket','lambda_function.zip').upload_file(Filename='C:\Users\RISHITA JAIN\PycharmProjects\Week1\lambda_function.zip')
import logging
import boto3
import os
from botocore.exceptions import ClientError

class Function:

    def create_bucket(self, bucket_name, region='ap-south-1'):
        try:
            if region is None:
                s3_client = boto3.client('s3')
                s3_client.create_bucket(Bucket=bucket_name)
            else:
                s3_client = boto3.client('s3', region_name=region)
                location = {'LocationConstraint': region}
                s3_client.create_bucket(Bucket=bucket_name,
                                        CreateBucketConfiguration=location)
        except ClientError as e:
            logging.error(e)
            return False
        return True
      
zf = zipfile.ZipFile('lambda_function.zip', mode='w', compression=zipfile.ZIP_DEFLATED)
zf.write('lambda_function.py')
zf.close()


    def upload_file(self, file_name, bucket, object_name=None):

        if object_name is None:
            object_name = os.path.basename(file_name)

        # Upload the file
        s3_client = boto3.client('s3')
        try:
            response = s3_client.upload_file(file_name, bucket, object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True


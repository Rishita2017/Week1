
from shutil import make_archive
import boto3
import os
from botocore.exceptions import ClientError

class Function:

    def create_bucket(self, bucket_name, region='ap-south-1'):
        try:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                        CreateBucketConfiguration=location)
        except ClientError as e:
            print(e)


    def create_zipfile(self, lambda_function_directory):
        try:
            make_archive('python',
                         'zip',
                         lambda_function_directory)
            print("Zip compressed successfully")
        except:
            print("Zip not uploaded")

    def upload_file(self, file_name, bucket, object_name=None):

        if object_name is None:
            object_name = os.path.basename(file_name)

        # Upload the file
        s3_client = boto3.client('s3')
        try:
            response = s3_client.upload_file(file_name, bucket, object_name)
        except ClientError as e:
            print(e)

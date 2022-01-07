import boto3

class Stack:
    def __init__(self, stack_name, template_body, region, source_bucket, data_bucket):
        self.stack_name = stack_name
        self.template_body = template_body
        self.client_cloudformation = boto3.client('cloudformation', region_name=region)
        self.client_s3 = boto3.client('s3', region_name=region)
        self.source_bucket = source_bucket
        self.data_bucket = data_bucket

    def create_stack(self):
        print(self.source_bucket)
        print(self.data_bucket)
        self.client_cloudformation.create_stack(
            StackName=self.stack_name,
            TemplateBody=self.template_body,
            Capabilities=['CAPABILITY_IAM'],
            Parameters=[
                {
                    'ParameterKey': "SourceBucket",
                    'ParameterValue': self.source_bucket
                },
                {
                    'ParameterKey': "DataBucket",
                    'ParameterValue': self.data_bucket
                }

            ]
        )

    def update_stack(self):
       self.client_cloudformation.update_stack(
            StackName=self.stack_name,
            TemplateBody=self.template_body,
            Capabilities=['CAPABILITY_IAM'],
            Parameters=[
                {
                    'ParameterKey': "SourceBucket",
                    'ParameterValue': self.source_bucket
                },
                {
                    'ParameterKey': "DataBucket",
                    'ParameterValue': self.data_bucket
                }])

    def status_check(self):
        stack_status = self.client_cloudformation.describe_stacks(StackName=self.stack_name)
        status = stack_status['Stacks'][0]['StackStatus']
        return status



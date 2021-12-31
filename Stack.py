import boto3
client_cloud=boto3.client(‘cloudformation’)
class Stack:
    def __init__(self, stack_name, template_body,  source_bucket , data_bucket):
        self.stack_name = stack_name
        self.template_body = template_body
        self.source_bucket= source_bucket
        self.data_bucket = data_bucket


    def create_stack(self):
        response = self.client_cloud.create_stack(
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
        response1 = self.client_cloud.update_stack(
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
    def status_check(self):
        stack_status== self.client_cloud.describe_stacks(StackName=self.stack_name)
        status = stack_status['Stacks'][0]['StackStatus']
        return status



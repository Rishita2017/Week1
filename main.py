from stack import Stack
from function import Function
function = Function()
dataBucketName = "datas3botobucket"
result_create = function.create_bucket(dataBucketName)
if result_create:
    print("Bucket got created successfully")
else:
    print("Bucket got created Failed")
function.create_zipfile('Python')
result_upload = function.upload_file('lambda_function.zip', dataBucketName)
if result_upload:
    print("File  uploaded successfully")
else:
    print("File  uploaded Failed")

with open('template.yaml', 'r') as cf_file:
    cft_template = cf_file.read()

stack_obj = Stack("FirstStacks3lambda", cft_template, "ap-south-1", "rishita10", "datas3bucket")
stack_obj.create_stack()
stack_obj.update_stack()



import boto3
from account import clientes

for count in range(len(clientes)):
    profile = clientes[count]
    session = boto3.session.Session(profile_name=profile)
    ec2_re = session.resource(service_name='ec2', region_name='us-east-1')
    cloudwatch_cli = session.client(service_name='cloudwatch', region_name='us-east-1')
    ec2_cli = session.client(service_name='ec2', region_name='us-east-1')
    lambda_cliente = session.client(service_name='lambda', region_name='us-east-1')

    list_functions = lambda_cliente.list_functions(FunctionVersion='ALL')
    Functions = list_functions['Functions']
    for Function in Functions:
        FunctionName = Function['FunctionName']
        Runtime = Function['Runtime']
        if Runtime == 'python2.7':
            print(profile,FunctionName, Runtime)

import boto3
import sys

Correo_Electronico = sys.argv[1]

session = boto3.session.Session(profile_name='QXSSDDATLANTICOPROD')
ec2_re = session.resource(service_name='ec2', region_name='us-east-1')
cloudwatch_cli = session.client(service_name='appstream', region_name='us-east-1')
ec2_cli = session.client(service_name='ec2', region_name='us-east-1')

UserName = 'joneshys@gmail.com'
appstream_client = boto3.client('appstream')

Describe_Stack_AppStream = appstream_client.describe_stacks()
Stack_Name = Describe_Stack_AppStream['Stacks'][0]['Name']
print(Stack_Name)
Associate_User_Stack = appstream_client.batch_associate_user_stack(UserStackAssociations=[{'StackName': Stack_Name,'UserName': Correo_Electronico,'AuthenticationType': 'USERPOOL','SendEmailNotification': True}])
#print(Create_User)
print(Associate_User_Stack)
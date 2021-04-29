#!/usr/bin/env python3
import boto3
import sys
import time

#Correo_Electronico = sys.argv[1]
#Primer_Nombre = sys.argv[2]
#Primer_Apellido = sys.argv[3]

Correo_Electronico = 'cvoborny-ita@transitodelatlantico.gov.co'
Primer_Nombre = 'Carmen'
Primer_Apellido = 'Borny'

session = boto3.session.Session(profile_name='QXSSDDATLANTICOPROD')
ec2_re = session.resource(service_name='ec2', region_name='us-east-1')
cloudwatch_cli = session.client(service_name='appstream', region_name='us-east-1')
ec2_cli = session.client(service_name='ec2', region_name='us-east-1')
appstream_client = session.client(service_name='appstream', region_name='us-east-1')

Describe_Stack_AppStream = appstream_client.describe_stacks()
Stack_Name = Describe_Stack_AppStream['Stacks'][0]['Name']
#print(Stack_Name)
Create_User = appstream_client.create_user(UserName=Correo_Electronico, FirstName=Primer_Nombre, LastName=Primer_Apellido,AuthenticationType='USERPOOL')
#print(Create_User)
time.sleep(5)
Associate_User_Stack = appstream_client.batch_associate_user_stack(UserStackAssociations=[{'StackName': Stack_Name,'UserName': Correo_Electronico,'AuthenticationType': 'USERPOOL','SendEmailNotification': True}])
#print(Create_User)
Status_Create = Associate_User_Stack['ResponseMetadata']['HTTPStatusCode']
if 200 == Status_Create:
    print('El usuario con el siguiente correo electrónico '+Correo_Electronico+', fue creado exitosamente. Por favor verifique la bandeja de entrada del correo electrónico '+Correo_Electronico)
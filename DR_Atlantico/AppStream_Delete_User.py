#!/usr/bin/env python3
import boto3
import sys

#Correo_Electronico = sys.argv[1]

session = boto3.session.Session(profile_name='QXSSDDATLANTICOPROD')
ec2_re = session.resource(service_name='ec2', region_name='us-east-1')
cloudwatch_cli = session.client(service_name='appstream', region_name='us-east-1')
ec2_cli = session.client(service_name='ec2', region_name='us-east-1')

Correo_Electronico='lmercado@transitodelatlantico.gov.co'

appstream_client = session.client(service_name='appstream', region_name='us-east-1')

Delete_User_appStream = appstream_client.delete_user(UserName=Correo_Electronico, AuthenticationType='USERPOOL')
Delete_User_AppStream = Delete_User_appStream['ResponseMetadata']['HTTPStatusCode']
if 200 == Delete_User_AppStream:
    print('El usuario '+Correo_Electronico+' Fue eliminado correctamente.')
else:
    print('El usuario '+Correo_Electronico+' No existe.')
#!/usr/bin/env python3
import json
import boto3
import sys

#Correo_Electronico = sys.argv[1]
Correo_Electronico = 'ccaratt@transitodelatlantico.gov.co'

session = boto3.session.Session(profile_name='QXSSDDATLANTICOPROD')
ec2_re = session.resource(service_name='ec2', region_name='us-east-1')
cloudwatch_cli = session.client(service_name='appstream', region_name='us-east-1')
ec2_cli = session.client(service_name='ec2', region_name='us-east-1')

appstream_client = boto3.client('appstream')

responses = appstream_client.describe_sessions(StackName='Stack-QX-NO-CROND', FleetName='Fleet-QX-NO-CROND')

for respon in responses['Sessions']:
    Id_sesion = respon['Id']
    UserId = respon['UserId']
    ConnectionState = respon['ConnectionState']
    MaxExpirationTime = respon['MaxExpirationTime']
    EniPrivateIpAddress = respon['NetworkAccessConfiguration']['EniPrivateIpAddress']
    #print(Id_sesion, UserId, ConnectionState, MaxExpirationTime, EniPrivateIpAddress) # Punto de control
    if Correo_Electronico in UserId:
        #print(Id_sesion) #Punto de control
        print('La sesión del usuario '+UserId+', fue cerrada exitosamente. Inicie sesión nuevamente.')
        Force_Brute_Close_Session = appstream_client.expire_session(SessionId=Id_sesion)
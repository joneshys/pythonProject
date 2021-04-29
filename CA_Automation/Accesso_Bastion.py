#!/usr/bin/env python3
import json
import boto3
from datetime import datetime
import sys

user='sorrelly.jaramillo'
IP_Pub = '177.254.207.108'
clientes = ['QXSSDDITAGUITEST']

#clientes = [sys.argv[1]]
IP_PUB_House = IP_Pub+'/32'
#IP_PUB_House = sys.argv[2]+'/32'
Mail_User = user+'@quipux.com'
#Mail_User = sys.argv[3]+'@quipux.com'

Access_SG_Bastion = []
for count in range(len(clientes)):
    profile = clientes[count]
    session = boto3.session.Session(profile_name=profile)
    ec2_re = session.resource(service_name='ec2', region_name='us-east-1')
    ec2_cli = session.client(service_name='ec2', region_name='us-east-1')

    instances = ec2_cli.describe_instances()

    for instance in instances['Reservations']:
        for network in instance['Instances']:
            for idsg in network['NetworkInterfaces']:
                for GroupName in idsg['Groups']:
                    SGGroupName = GroupName['GroupName']
                    SGGroupId = GroupName['GroupId']
                    if 'QXBASTION' in SGGroupName:
                        GroupNameBastion = SGGroupName
                        SGGroupIdBastion = SGGroupId
                        Const_SG_Bastion = SGGroupIdBastion
                        Access_SG_Bastion.append(Const_SG_Bastion)
                        #print(SGGroupIdBastion)# Punto de control


Existing_User_CidrIp = []
Existing_User_Mail = []
for count in range(len(clientes)):
    profile = clientes[count]
    session = boto3.session.Session(profile_name=profile)
    ec2_re = session.resource(service_name='ec2', region_name='us-east-1')
    ec2_cli = session.client(service_name='ec2', region_name='us-east-1')

    instances = ec2_cli.describe_instances()

    ID_Security_Group_Bastion = Access_SG_Bastion[0]
    security_group = ec2_re.SecurityGroup(ID_Security_Group_Bastion)

    response = ec2_cli.describe_security_groups(GroupIds=[ID_Security_Group_Bastion])
    sg = response['SecurityGroups']
    for IpPermissions in sg:
        #print(IpPermissions)#Punto de control
        NombreGrupoSeguridad = IpPermissions['GroupName']
        PermisosIps = IpPermissions['IpPermissions']
        #print(NombreGrupoSeguridad, PermisosIps)#Punto de control
        for PermisosIp in PermisosIps:
            IpRanges = PermisosIp['IpRanges']
            for IpRange in IpRanges:
                #print(IpRange)#Punto de control
                CidrIp = IpRange['CidrIp']
                Description = IpRange['Description']
                Existing_User_Mail.append(Description)
                if Mail_User in Description:
                    print('Regla del usuario '+Mail_User+' con IP Publica '+IP_PUB_House+' fue actualizada '+'en la cuenta '+profile)
                    security_group = ec2_re.SecurityGroup(ID_Security_Group_Bastion)
                    revoke = security_group.revoke_ingress(CidrIp=CidrIp, FromPort=3389, ToPort=3389,IpProtocol='tcp')
                    autorize = security_group.authorize_ingress(IpPermissions=[{ 'FromPort':3389,'IpProtocol':'tcp','IpRanges':[{'CidrIp': IP_PUB_House,'Description': Mail_User}], 'ToPort':3389}])
#print(Existing_User_Mail)# Punto de control

if Mail_User not in Existing_User_Mail:
    print('Se crea regla para el usuario'+' '+Mail_User+' '+'hacia la Ip Publica'+' '+IP_PUB_House+' en la cuenta '+profile)
    autorize_Test = security_group.authorize_ingress(IpPermissions=[{'FromPort': 3389, 'IpProtocol': 'tcp', 'IpRanges': [{'CidrIp': IP_PUB_House, 'Description': Mail_User}],'ToPort': 3389}])
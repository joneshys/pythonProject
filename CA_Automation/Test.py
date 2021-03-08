#!/usr/bin/env python3
import json
import boto3
from datetime import datetime
import sys

clientes = ['QXSSDDATLANTICOTEST']
#clientes = [sys.argv[1]]
IP_PUB_House = '192.168.3.25'+'/32'
#IP_PUB_House = sys.argv[2]+'/32'
Mail_User = 'andrea.benitez@quipux.com'
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
                print(IpRange)#Punto de control
                #CidrIp = IpRange['CidrIp']
                Description = IpRange['Description']
                #Existing_User_Mail.append(Description)
                print(Description)
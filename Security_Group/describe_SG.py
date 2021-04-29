import json
import boto3
from datetime import datetime
import sys
from account import clientes
for count in range(len(clientes)):
    profile = clientes[count]
    session = boto3.session.Session(profile_name=profile)
    ec2_re = session.resource(service_name='ec2', region_name='us-east-1')
    ec2_cli = session.client(service_name='ec2', region_name='us-east-1')

    GroupIds=["sg-00416c03c838991cf","sg-00e43693bd1174416","sg-00fbd087ca45dff73","sg-013a9e7cd3d64a23b","sg-02b8f92f5a8acee64","sg-0320b921d1777827d","sg-0355e8eb21090d51e","sg-040379b9698e1e15f",
    "sg-04fd9807d8d407c19","sg-054ecf9a2303892a8","sg-0562eaead856e5866","sg-058e1a4bd2fbb65c9","sg-05e40e0a0648b7151","sg-05f30de823556988f","sg-0665a8fa36fb86ba9","sg-06aad5b8afb8300fa",
    "sg-06e2bd8c7eb0b5b84","sg-072e1bafd3dc7182f","sg-074193a8840b745dd","sg-07ca682b044aad32e","sg-07d1a5b43edc67b89","sg-07fbca985ccb5a48c","sg-080925df840f9e79b","sg-08896163e0a79e9fb",
    "sg-08d556441dc7d33ce","sg-096701dce3af5d6c1","sg-09c8c4dbf41e55a50","sg-0a8a1defc2fd4722c","sg-0b6ecac87f5bee4cb","sg-0cb265650e41d22ce","sg-0cf9a85feebc9182f","sg-0da044a15ba9662b1",
    "sg-0e3641094f0a1a260","sg-0eb9cae33953e1c5a","sg-0f2579e15b69ee62c","sg-0fc84677fc53e7cad"]

    response = ec2_cli.describe_security_groups(GroupIds=GroupIds)
    #print(response['SecurityGroups'])
    for IpPermissions in response['SecurityGroups']:
        GroupName= IpPermissions['GroupName']
        for ports in IpPermissions['IpPermissions']:
            f = open("Port_SG_Prod.txt", "a")
            print(GroupName,ports)
            SG_Ports_Prod = GroupName,ports
            f.write(str(SG_Ports_Prod)+'\n')
            f.close()

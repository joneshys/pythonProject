import json
import boto3

def lambda_handler(event, context):
    IP_ResourceRecords = []

    # Obtener el DNS Name y su IP
    client_route53 = boto3.client('route53')
    list_hosted_zones = client_route53.list_hosted_zones()
    ID_HostedZones = list_hosted_zones['HostedZones'][0]['Id'].split('/')[2]
    # print(ID_HostedZones) #Punto de control
    list_resource_record_sets = client_route53.list_resource_record_sets(HostedZoneId=ID_HostedZones)
    ResourceRecordSets = list_resource_record_sets['ResourceRecordSets']
    # print(ResourceRecordSets) #Punto de control
    for RecordSet in ResourceRecordSets:
        if 'NS' == RecordSet['Type']:
            Name = RecordSet['Name']
            ResourceRecords = RecordSet['ResourceRecords'][0]['Value']
            # print(Name, ResourceRecords) #Punto de control
            IP_ResourceRecords.append(Name)
    # return IP_ResourceRecords #Punto de control

    client_route53 = boto3.client('route53')
    list_hosted_zones = client_route53.list_hosted_zones()
    ID_HostedZones = list_hosted_zones['HostedZones'][0]['Id'].split('/')[2]
    # Obtener la IP actual de la instancia
    client_ec2 = boto3.client('ec2')
    Instances = client_ec2.describe_instances()
    for instance in (Instances['Reservations']):
        for ec2 in instance['Instances']:
            PrivateIpAddress = ec2['PrivateIpAddress']
            Tags = ec2['Tags']
            for tag in Tags:
                if tag["Key"] == 'Name':
                    InstanceName = tag["Value"]
                    # print(InstanceName, PrivateIpAddress) #Punto de control
                    if 'QXBASTION' not in InstanceName:
                        # print(InstanceName, PrivateIpAddress) #Punto de control
                        Name_Resource_Records = InstanceName.lower() + '.' + IP_ResourceRecords[0]
                        # print(Name_Resource_Records)
                        response = client_route53.change_resource_record_sets(
                            HostedZoneId=ID_HostedZones,
                            ChangeBatch={
                                'Comment': 'Upgrade Name Resource in ' + Name_Resource_Records + ' with IP ' + PrivateIpAddress,
                                'Changes': [{
                                    'Action': 'UPSERT',
                                    'ResourceRecordSet': {
                                        'Name': Name_Resource_Records,
                                        'Type': "A",
                                        'TTL': 300,
                                        'ResourceRecords': [{'Value': PrivateIpAddress}]}}]})
                        print(
                            'The server ' + InstanceName + ' in resource route53 ' + Name_Resource_Records + ' Updated with IP ' + PrivateIpAddress)
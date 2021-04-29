#!/usr/bin/env python3

#Importacion de las librerias necesarias
import boto3
#from account import clientes
clientes = ['QXSSDDATLANTICOTEST']
#Se crea la conexión a AWS, y se crea una lista por medio del for y del append
const_1 = []
for count in range(len(clientes)):
    profile = clientes[count]
    session = boto3.session.Session(profile_name=profile)
    ec2_re = session.resource(service_name='ec2', region_name='us-east-1')
    cloudwatch_cli = session.client(service_name='cloudwatch', region_name='us-east-1')
    ec2_cli = session.client(service_name='ec2', region_name='us-east-1')
    rds = session.client(service_name='rds', region_name='us-east-1')
    Names_RDS = rds.describe_db_instances()
    RDSs = Names_RDS['DBInstances']
    for Instances_RDS in RDSs:
        #print(Instances_RDS)
        DBInstanceIdentifier = Instances_RDS['DBInstanceIdentifier']
        Family_Instances_RDS = Instances_RDS['DBInstanceClass']
        Engine = Instances_RDS['Engine']
        EngineVersion = Instances_RDS['EngineVersion']
        DBInstanceStatus = Instances_RDS['DBInstanceStatus']
        MasterUsername = Instances_RDS['MasterUsername']
        T_InstanceCreateTime = Instances_RDS['InstanceCreateTime']
        InstanceCreateTime = T_InstanceCreateTime.strftime('%Y-%m-%d')
        BackupRetentionPeriod = str(Instances_RDS['BackupRetentionPeriod'])
        AvailabilityZone = Instances_RDS['AvailabilityZone']
        VpcId_Instance_RDS = Instances_RDS['DBSubnetGroup']['VpcId']
        MultiAZ = str(Instances_RDS['MultiAZ'])
        LicenseModel = Instances_RDS['LicenseModel']
        StorageEncrypted = str(Instances_RDS['StorageEncrypted'])
        SubnetIdentifier_A = Instances_RDS['DBSubnetGroup']['Subnets'][0]['SubnetIdentifier']
        SubnetAvailabilityZone_A = Instances_RDS['DBSubnetGroup']['Subnets'][0]['SubnetAvailabilityZone']['Name']
        SubnetIdentifier_B = Instances_RDS['DBSubnetGroup']['Subnets'][1]['SubnetIdentifier']
        SubnetAvailabilityZone_B = Instances_RDS['DBSubnetGroup']['Subnets'][1]['SubnetAvailabilityZone']['Name']
        print(profile, DBInstanceIdentifier, MultiAZ, Family_Instances_RDS)
        const1 = profile + ',' + DBInstanceIdentifier + ',' + Family_Instances_RDS + ',' + Engine + ',' + EngineVersion + ',' + DBInstanceStatus + ',' + MasterUsername + ',' + InstanceCreateTime + ',' + BackupRetentionPeriod + ',' + AvailabilityZone + ',' + VpcId_Instance_RDS + ',' + MultiAZ + ',' + LicenseModel + ',' + StorageEncrypted + ',' + SubnetIdentifier_A + ',' + SubnetAvailabilityZone_A + ',' + SubnetIdentifier_B + ',' + SubnetAvailabilityZone_B
        const_1.append(const1)
#print(const_1) # punto de evaluación

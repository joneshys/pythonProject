import boto3
import csv
from datetime import datetime
#clientes = ['QXSSDDATLANTICOPROD', 'QXSSDDBELLOPROD', 'QXSSDDCALIPROD', 'QXHUNITIPROD', 'QXIMPTOSVALLEPROD', 'QXSSDDITAGUIPROD', 'QXSSDDPEREIRAPROD', 'QXINTRUNTPROD', 'QXBIPROD','QXPROD', 'QXCOMPARENDERASSOMOSPROD', 'QXSSDDSABANETAPROD']
clientes = ['TEST']
for count in range(len(clientes)):
    profile = clientes[count]
    session = boto3.session.Session(region_name="us-east-1", profile_name=profile)
    ec2_re = session.resource(service_name="cloudwatch", region_name="us-east-1")
    ec2_cli = session.client("cloudwatch", region_name="us-east-1")
    kms = session.client(service_name="kms",region_name="us-east-1")

    List_KMS = kms.list_aliases()
    for Alias in List_KMS['Aliases']:
       print(Alias)
       response = kms.schedule_key_deletion(KeyId=Alias['TargetKeyId'],PendingWindowInDays=7)

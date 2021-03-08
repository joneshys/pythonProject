import boto3
import csv
import collections
import pandas as pd
import os
import time
#os.remove("Count_Snapshot_EC2.csv")

#clientes = ['QXSSDDATLANTICOTEST', 'QXSSDDATLANTICOPROD', 'QXSSDDBELLOTEST', 'QXSSDDBELLOPROD', 'QXSSDDCALITEST','QXSSDDCALIPROD', 'QXHUNITIPROD', 'QXIMPTOSVALLETEST', 'QXIMPTOSVALLEPROD', 'QXSSDDITAGUITEST','QXSSDDITAGUIPROD', 'QXSSDDPEREIRATEST', 'QXSSDDPEREIRAPROD', 'QXINTRUNTTEST', 'QXINTRUNTPROD', 'QXBIPROD','QXPROD', 'QXCOMPARENDERASSOMOSPROD', 'QXSSDDSABANETATEST', 'QXSSDDSABANETAPROD']
clientes = ['QXSSDDATLANTICOPROD', 'QXSSDDBELLOPROD', 'QXSSDDCALIPROD', 'QXHUNITIPROD', 'QXIMPTOSVALLEPROD', 'QXSSDDITAGUIPROD', 'QXSSDDPEREIRAPROD', 'QXINTRUNTPROD', 'QXBIPROD','QXPROD', 'QXCOMPARENDERASSOMOSPROD', 'QXSSDDSABANETAPROD']

# clientes = ['QXSSDDBELLOPROD']
#f4 = open("Count_Snapshot_EC2.csv", "w", newline='')
#header_CSV = ['Cliente', 'Id_Snapshot']
#cvs_w = csv.writer(f4)
#cvs_w.writerow(header_CSV)
#f4.close()

for count in range(len(clientes)):
    profile = clientes[count]
    session = boto3.session.Session(profile_name=profile)
    ec2_cli = session.client(service_name='ec2', region_name='us-east-1')
    Instances = ec2_cli.describe_instances()

    #f4 = open("Count_Snapshot_EC2.csv", "a", newline='')
    #cvs_w = csv.writer(f4)

    Id_Owner_Account = []
    for instance in (Instances['Reservations']):
        for ec2 in instance['Instances']:
            Id_Owner = ec2['NetworkInterfaces'][0]['OwnerId']
            if Id_Owner not in Id_Owner_Account:
                Id_Owner_Account.append(Id_Owner)
    # print(Id_Owner_Account[0])

    List_Count_AMI = []
    amis = ec2_cli.describe_images(Owners=Id_Owner_Account)
    for ami in amis['Images']:
        List_Count_AMI.append(profile)
    print(collections.Counter(List_Count_AMI))
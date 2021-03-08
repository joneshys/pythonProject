import boto3
import csv
import collections
import pandas as pd
import os
from datetime import datetime
import time

#clientes = ['QXSSDDATLANTICOTEST','QXSSDDATLANTICOPROD','QXSSDDBELLOTEST','QXSSDDBELLOPROD','QXSSDDCALITEST','QXSSDDCALIPROD','QXHUNITIPROD','QXIMPTOSVALLETEST','QXIMPTOSVALLEPROD','QXSSDDITAGUITEST','QXSSDDITAGUIPROD','QXSSDDPEREIRATEST','QXSSDDPEREIRAPROD','QXINTRUNTTEST','QXINTRUNTPROD','QXBIPROD','QXPROD','QXCOMPARENDERASSOMOSPROD','QXSSDDSABANETATEST','QXSSDDSABANETAPROD']
clientes = ['QXSSDDPEREIRATEST']

for count in range(len(clientes)):
    profile = clientes[count]
    session = boto3.session.Session(profile_name=profile)
    ec2_cli = session.client(service_name='ec2', region_name='us-east-1')
    Instances = ec2_cli.describe_instances()
    RDS_Client = boto3.client('rds')
    snapshots = RDS_Client.describe_db_snapshots(SnapshotType='manual')
    #print(snapshots)

    List_Count_Snapshot_RDS = []
    for Snapshot_RDS in snapshots['DBSnapshots']:
        DBSnapshotIdentifier = Snapshot_RDS['DBSnapshotIdentifier']
        SnapshotCreateTime = Snapshot_RDS['SnapshotCreateTime'].date()
        Ahora = datetime.now().date()
        Resta_Dias = Ahora - SnapshotCreateTime
        List_Count_Snapshot_RDS.append(profile)
        print(DBSnapshotIdentifier, Resta_Dias, profile)
    #print(collections.Counter(List_Count_Snapshot_RDS))
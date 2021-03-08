import boto3
import csv
import os
import pandas as pd
from datetime import datetime
os.remove("Count_Snapshot_RDS.csv")

clientes = ['QXSSDDATLANTICOTEST','QXSSDDATLANTICOPROD','QXSSDDBELLOTEST','QXSSDDBELLOPROD','QXSSDDCALITEST','QXSSDDCALIPROD','QXHUNITIPROD','QXIMPTOSVALLETEST','QXIMPTOSVALLEPROD','QXSSDDITAGUITEST','QXSSDDITAGUIPROD','QXSSDDPEREIRATEST','QXSSDDPEREIRAPROD','QXINTRUNTTEST','QXINTRUNTPROD','QXBIPROD','QXPROD','QXCOMPARENDERASSOMOSPROD','QXSSDDSABANETATEST','QXSSDDSABANETAPROD']

f3 = open("Count_Snapshot_RDS.csv","w",newline='')
header_CSV = ['Client', 'Snapshot']
cvs_w = csv.writer(f3)
cvs_w.writerow(header_CSV)
f3.close()
for count in range(len(clientes)):
    profile = clientes[count]
    session = boto3.session.Session(profile_name=profile)
    ec2_re = session.resource(service_name='ec2', region_name='us-east-1')
    ec2_cli = session.client(service_name="ec2", region_name="us-east-1")
    rds = session.client(service_name="rds", region_name="us-east-1")
    efs = session.client(service_name="efs", region_name="us-east-1")
    backup = session.client(service_name="backup", region_name="us-east-1")

    f3 = open("Count_Snapshot_RDS.csv","a",newline='')
    cvs_w = csv.writer(f3)
    RDS_Snapshot = rds.describe_db_snapshots()
    RDS_Snapshots = RDS_Snapshot['DBSnapshots']
    Cantidad_Snapshots = len(profile)
    for Snapshot in RDS_Snapshots:
        SnapshotCount = Snapshot['DBSnapshotIdentifier']
        cvs_w.writerow([profile, SnapshotCount])
    f3.close()
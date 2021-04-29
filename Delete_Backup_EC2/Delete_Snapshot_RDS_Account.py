import boto3
import collections
import time
import datetime
from datetime import datetime

#clientes = ['QXSSDDATLANTICOTEST', 'QXSSDDATLANTICOPROD', 'QXSSDDBELLOTEST', 'QXSSDDBELLOPROD', 'QXSSDDCALITEST','QXSSDDCALIPROD', 'QXHUNITIPROD', 'QXIMPTOSVALLETEST', 'QXIMPTOSVALLEPROD', 'QXSSDDITAGUITEST','QXSSDDITAGUIPROD', 'QXSSDDPEREIRATEST', 'QXSSDDPEREIRAPROD', 'QXINTRUNTTEST', 'QXINTRUNTPROD', 'QXBIPROD','QXPROD', 'QXCOMPARENDERASSOMOSPROD', 'QXSSDDSABANETATEST', 'QXSSDDSABANETAPROD']
#clientes = ['QXSSDDATLANTICOPROD', 'QXSSDDBELLOPROD', 'QXSSDDCALIPROD', 'QXHUNITIPROD', 'QXIMPTOSVALLEPROD', 'QXSSDDITAGUIPROD', 'QXSSDDPEREIRAPROD', 'QXINTRUNTPROD', 'QXBIPROD','QXPROD', 'QXCOMPARENDERASSOMOSPROD', 'QXSSDDSABANETAPROD']
clientes = ['QXSSDDBELLOPROD']

for count in range(len(clientes)):
    profile = clientes[count]
    session = boto3.session.Session(profile_name=profile)
    ec2_cli = session.client(service_name='ec2', region_name='us-east-1')
    RDS_Client = session.client(service_name='rds', region_name='us-east-1')

    Describe_RDS = RDS_Client.describe_db_snapshots()

    for RDSs in Describe_RDS['DBSnapshots']:
        DBSnapshotIdentifier = RDSs['DBSnapshotIdentifier']
        SnapshotCreateTime = RDSs['SnapshotCreateTime'].date()
        Hoy = datetime.now().date()
        Old_Days = Hoy - SnapshotCreateTime
        #print(profile,DBSnapshotIdentifier, SnapshotCreateTime, Old_Days.days)
        if Old_Days.days > 15:
            print(profile, DBSnapshotIdentifier, SnapshotCreateTime, Old_Days.days)
            Delete_Snapshot_GreaterThan_30_Days = RDS_Client.delete_db_snapshot(DBSnapshotIdentifier=DBSnapshotIdentifier)
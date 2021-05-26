import boto3
import collections
import time
import datetime
from datetime import datetime

#clientes = ['QXSSDDATLANTICOTEST', 'QXSSDDATLANTICOPROD', 'QXSSDDBELLOTEST', 'QXSSDDBELLOPROD', 'QXSSDDCALITEST','QXSSDDCALIPROD', 'QXHUNITIPROD', 'QXIMPTOSVALLETEST', 'QXIMPTOSVALLEPROD', 'QXSSDDITAGUITEST','QXSSDDITAGUIPROD', 'QXSSDDPEREIRATEST', 'QXSSDDPEREIRAPROD', 'QXINTRUNTTEST', 'QXINTRUNTPROD', 'QXBIPROD','QXPROD', 'QXCOMPARENDERASSOMOSPROD', 'QXSSDDSABANETATEST', 'QXSSDDSABANETAPROD']
#clientes = ['QXSSDDATLANTICOPROD', 'QXSSDDBELLOPROD', 'QXSSDDCALIPROD', 'QXHUNITIPROD', 'QXIMPTOSVALLEPROD', 'QXSSDDITAGUIPROD', 'QXSSDDPEREIRAPROD', 'QXINTRUNTPROD', 'QXBIPROD','QXPROD', 'QXCOMPARENDERASSOMOSPROD', 'QXSSDDSABANETAPROD']
clientes = ['QXSSDDATLANTICOPROD']

for count in range(len(clientes)):
    profile = clientes[count]
    session = boto3.session.Session(profile_name=profile)
    ec2_cli = session.client(service_name='ec2', region_name='us-east-1')
    RDS_Client = session.client(service_name='rds', region_name='us-east-1')

    Describe_RDS_Manual = RDS_Client.describe_db_snapshots(SnapshotType='manual')
    Describe_RDS_Automatico = RDS_Client.describe_db_snapshots()

    for RDSs_Manual in Describe_RDS_Manual['DBSnapshots']:
        DBSnapshotIdentifier_Manual = RDSs_Manual['DBSnapshotIdentifier']
        SnapshotCreateTime_Manual = RDSs_Manual['SnapshotCreateTime'].date()
        Hoy_Manual = datetime.now().date()
        Old_Days_Manual = Hoy_Manual - SnapshotCreateTime_Manual
        print(profile,'Manual', DBSnapshotIdentifier_Manual, SnapshotCreateTime_Manual, str(Old_Days_Manual.days)+' días de vejez')
        if Old_Days_Manual.days > 7:
            print(profile, 'Manual', DBSnapshotIdentifier_Manual, SnapshotCreateTime_Manual, str(Old_Days_Manual.days)+' días de vejez')
            Delete_Snapshot_GreaterThan_7_Days_Manual = RDS_Client.delete_db_snapshot(DBSnapshotIdentifier=DBSnapshotIdentifier_Manual)

    for RDSs_Automatico in Describe_RDS_Automatico['DBSnapshots']:
        DBSnapshotIdentifier_Automatico = RDSs_Automatico['DBSnapshotIdentifier']
        SnapshotCreateTime_Automatico = RDSs_Automatico['SnapshotCreateTime'].date()
        Hoy_Automatico = datetime.now().date()
        Old_Days_Automatico = Hoy_Automatico - SnapshotCreateTime_Automatico
        print(profile,'Automatico',DBSnapshotIdentifier_Automatico, SnapshotCreateTime_Automatico, str(Old_Days_Automatico.days)+' días de vejez')
        if Old_Days_Automatico.days > 7:
            print(profile, 'Automatico', DBSnapshotIdentifier_Automatico, SnapshotCreateTime_Automatico, str(Old_Days_Automatico.days)+' días de vejez')
            Delete_Snapshot_GreaterThan_7_Days_Automatico = RDS_Client.delete_db_snapshot(DBSnapshotIdentifier=DBSnapshotIdentifier_Automatico)
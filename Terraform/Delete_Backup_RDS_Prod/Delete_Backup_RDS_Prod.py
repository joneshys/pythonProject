import boto3
import datetime
from datetime import datetime

def lambda_handler(event, context):
    ec2_cli = boto3.client('ec2')
    RDS_Client = boto3.client('rds')
    Describe_RDS_Manual = RDS_Client.describe_db_snapshots(SnapshotType='manual')
    Describe_RDS_Automatico = RDS_Client.describe_db_snapshots()

    for RDSs_Manual in Describe_RDS_Manual['DBSnapshots']:
        DBSnapshotIdentifier_Manual = RDSs_Manual['DBSnapshotIdentifier']
        SnapshotCreateTime_Manual = RDSs_Manual['SnapshotCreateTime'].date()
        Hoy_Manual = datetime.now().date()
        Old_Days_Manual = Hoy_Manual - SnapshotCreateTime_Manual
        print(DBSnapshotIdentifier_Manual, 'Manual',SnapshotCreateTime_Manual, str(Old_Days_Manual.days)+' días de Antiguedad')
        if Old_Days_Manual.days > 7:
            print(DBSnapshotIdentifier_Manual, 'Manual', SnapshotCreateTime_Manual,str(Old_Days_Manual.days)+' días de Antiguedad')
            Delete_Snapshot_GreaterThan_7_Days = RDS_Client.delete_db_snapshot(DBSnapshotIdentifier=DBSnapshotIdentifier_Manual)

    for RDSs_Automatico in Describe_RDS_Automatico['DBSnapshots']:
        DBSnapshotIdentifier_Automatico = RDSs_Automatico['DBSnapshotIdentifier']
        SnapshotCreateTime_Automatico = RDSs_Automatico['SnapshotCreateTime'].date()
        Hoy_Automatico = datetime.now().date()
        Old_Days_Automatico = Hoy_Automatico - SnapshotCreateTime_Automatico
        print(DBSnapshotIdentifier_Automatico,'Automatico', SnapshotCreateTime_Automatico, str(Old_Days_Automatico.days)+' días de Antiguedad')
        if Old_Days_Automatico.days > 7:
            print(DBSnapshotIdentifier_Automatico,'Automatico', SnapshotCreateTime_Automatico, str(Old_Days_Automatico.days)+' días de Antiguedad')
            Delete_Snapshot_GreaterThan_7_Days = RDS_Client.delete_db_snapshot(DBSnapshotIdentifier=DBSnapshotIdentifier_Automatico)
import boto3
import collections
import time
import datetime

clientes = ['QXCOMPARENDERASSOMOSPROD']

for count in range(len(clientes)):
    profile = clientes[count]
    session = boto3.session.Session(profile_name=profile)
    ec2_cli = session.client(service_name='ec2', region_name='us-east-1')
    Instances = ec2_cli.describe_instances()

    Id_Owner_Account = []
    for instance in (Instances['Reservations']):
        for ec2 in instance['Instances']:
            Id_Owner = ec2['NetworkInterfaces'][0]['OwnerId']
            if Id_Owner not in Id_Owner_Account:
                Id_Owner_Account.append(Id_Owner)

    Snapshots_Id = ec2_cli.describe_snapshots(OwnerIds=Id_Owner_Account)
    for snapshot in Snapshots_Id['Snapshots']:
        SnapshotId = snapshot['SnapshotId']
        StartTime = snapshot['StartTime'].date()
        Ahora = datetime.datetime.now().date()
        Resta_Dias = Ahora - StartTime
        #print(Resta_Dias.days)
        if Resta_Dias.days > 30:
            Delete_Snapshot_EC2 = ec2_cli.delete_snapshot(SnapshotId=SnapshotId)['ResponseMetadata']['HTTPStatusCode']
            if Delete_Snapshot_EC2 == 200:
                print('El siguiente Id de Snapshot EC2 fue eliminado correctamente: '+SnapshotId+', del cliente: '+profile)
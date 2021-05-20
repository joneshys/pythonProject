import boto3
import collections
import time
import datetime
from datetime import datetime

#clientes = ['QXSSDDATLANTICOTEST', 'QXSSDDBELLOTEST', 'QXSSDDCALITEST', 'QXIMPTOSVALLETEST', 'QXSSDDITAGUITEST', 'QXSSDDPEREIRATEST', 'QXINTRUNTTEST', 'QXSSDDSABANETATEST']
clientes = ['QXHUNITIPROD','QXSSDDATLANTICOPROD', 'QXSSDDBELLOPROD', 'QXSSDDCALIPROD', 'QXIMPTOSVALLEPROD', 'QXSSDDITAGUIPROD', 'QXSSDDPEREIRAPROD', 'QXINTRUNTPROD', 'QXBIPROD','QXPROD', 'QXCOMPARENDERASSOMOSPROD', 'QXSSDDSABANETAPROD']
#'QXHUNITIPROD',
#clientes = ['QXHUNITIPROD']
for count in range(len(clientes)):
    profile = clientes[count]
    session = boto3.session.Session(profile_name=profile)
    ec2_cli = session.client(service_name='ec2', region_name='us-east-1')
    Instances = ec2_cli.describe_instances()
    ec2_resource = boto3.resource('ec2')

    Id_Owner_Account = []
    for instance in (Instances['Reservations']):
        for ec2 in instance['Instances']:
            Id_Owner = ec2['NetworkInterfaces'][0]['OwnerId']
            if Id_Owner not in Id_Owner_Account:
                Id_Owner_Account.append(Id_Owner)

            # Eliminación de AMI´s EC2
            amis = ec2_cli.describe_images(Owners=Id_Owner_Account)
            for ami in amis['Images']:
                create_date = ami['CreationDate'].split('T')
                Create_Date = datetime.strptime(create_date[0], '%Y-%m-%d').date()
                Noe = datetime.now().date()
                Resta = Noe - Create_Date
                ami_id = ami['ImageId']
                # print(Resta.days, ami_id, profile)
                if Resta.days > 15:
                    Delete_AMI_EC2 = ec2_cli.deregister_image(ImageId=ami_id)['ResponseMetadata']['HTTPStatusCode']
                    if Delete_AMI_EC2 == 200:
                        print(
                            'El siguiente Id de AMI EC2 fue eliminado correctamente: ' + ami_id + ', del cliente: ' + profile)

    # Eliminación Snapshot´s EC2
    Snapshots_Id = ec2_cli.describe_snapshots(OwnerIds=Id_Owner_Account)
    for snapshot in Snapshots_Id['Snapshots']:
        SnapshotId = snapshot['SnapshotId']
        StartTime = snapshot['StartTime'].date()
        Ahora = datetime.now().date()
        Resta_Dias = Ahora - StartTime
        # print(Resta_Dias.days)
        if Resta_Dias.days > 15:
            Delete_Snapshot_EC2 = ec2_cli.delete_snapshot(SnapshotId=SnapshotId)['ResponseMetadata']['HTTPStatusCode']
            if Delete_Snapshot_EC2 == 200:
                print('El siguiente Id de Snapshot EC2 fue eliminado correctamente: ' + SnapshotId + ', del cliente: ' + profile)



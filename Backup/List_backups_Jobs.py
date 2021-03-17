import boto3

session = boto3.session.Session(profile_name='QXIMPTOSVALLEPROD')
ec2_re = session.resource(service_name='ec2', region_name='us-east-1')
cloudwatch_cli = session.client(service_name='appstream', region_name='us-east-1')
ec2_cli = session.client(service_name='ec2', region_name='us-east-1')
Backup=session.client(service_name='backup', region_name='us-east-1')

List_Bakup_Jobs=Backup.list_backup_jobs(ByState='FAILED')
BackupJobs = List_Bakup_Jobs['BackupJobs']
#print(BackupJobs)
for backup in BackupJobs:
    print(backup)
import boto3
import csv
from datetime import datetime
clientes = ['QXSSDDATLANTICOPROD', 'QXSSDDBELLOPROD', 'QXSSDDCALIPROD', 'QXHUNITIPROD', 'QXIMPTOSVALLEPROD', 'QXSSDDITAGUIPROD', 'QXSSDDPEREIRAPROD', 'QXINTRUNTPROD', 'QXBIPROD','QXPROD', 'QXCOMPARENDERASSOMOSPROD', 'QXSSDDSABANETAPROD']
#clientes = ['QXPROD']
Ahora = datetime.now().date()

f4 = open("List_Alarm.csv", "a",newline='')
cvs_w = csv.writer(f4)
f4.close()


for count in range(len(clientes)):
    profile = clientes[count]
    session = boto3.session.Session(region_name="us-east-1", profile_name=profile)
    ec2_re = session.resource(service_name="cloudwatch", region_name="us-east-1")
    ec2_cli = session.client("cloudwatch", region_name="us-east-1")

    f4 = open("List_Alarm.csv", "a", newline='')
    cvs_w = csv.writer(f4)

    paginator = ec2_cli.get_paginator('describe_alarms')
    #for response1 in paginator.paginate(StateValue='ALARM'):
    for response in paginator.paginate(StateValue='INSUFFICIENT_DATA'):
        if response['MetricAlarms'] != []:
            Alarm_Metrics =response['MetricAlarms']
            for Alarm_Metric in Alarm_Metrics:
                AlarmName = Alarm_Metric['AlarmName']
                print(profile, AlarmName, 'INSUFFICIENT_DATA', Ahora)
                cvs_w.writerow([profile, AlarmName, 'INSUFFICIENT_DATA', Ahora])

    for response1 in paginator.paginate(StateValue='ALARM'):
        if response1['MetricAlarms'] != []:
            Alarm_Metrics =response1['MetricAlarms']
            for Alarm_Metric in Alarm_Metrics:
                AlarmName = Alarm_Metric['AlarmName']
                print(profile, AlarmName, 'ALARM', Ahora)
                cvs_w.writerow([profile, AlarmName, 'ALARM', Ahora])

    f4.close()
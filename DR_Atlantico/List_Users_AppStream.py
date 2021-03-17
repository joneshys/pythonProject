import boto3
import csv

clientes = ['QXSSDDATLANTICOPROD']  # ,'QXSSDDATLANTICOTEST']

f4 = open("List_Users_AppStream", "w",newline='')
header_CSV = ['Cliente','Id_Snapshot']
cvs_w = csv.writer(f4)
cvs_w.writerow(header_CSV)
f4.close()

for count in range(len(clientes)):
    profile = clientes[count]
    session = boto3.session.Session(profile_name=profile)
    ec2_re = session.resource(service_name='ec2', region_name='us-east-1')
    cloudwatch_cli = session.client(service_name='cloudwatch', region_name='us-east-1')
    ec2_cli = session.client(service_name='ec2', region_name='us-east-1')
    appstream = session.client(service_name='appstream', region_name='us-east-1')

    UserAppstream = appstream.describe_users(AuthenticationType='USERPOOL',MaxResults=61)
    Users_AppsStream = UserAppstream['Users']

    f4 = open("List_Users_AppStream.csv", "a", newline='')
    cvs_w = csv.writer(f4)

    # print(Users_AppsStream)

    for users in Users_AppsStream:
        print(users)
        UserName = users['UserName']
        Enabled = users['Enabled']
        Status = users['Status']
        FirstName = users['FirstName']
        LastName = users['LastName']
        print(profile, UserName, Enabled, Status, FirstName, LastName)
        cvs_w.writerow([profile, UserName, Enabled, Status, FirstName, LastName])
    f4.close()
        # if 'CONFIRMED' == Status:
            # print(profile, UserName, Enabled, Status, FirstName, LastName)
        # if 'oscar.gomez@quipux.com' in UserName:
            # print(profile, UserName, Enabled, Status, FirstName, LastName)
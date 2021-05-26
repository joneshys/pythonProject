import boto3
import os
os.remove("WorkspaceId_User.txt")
clientes = ['QXVALTIX']

for count in range(len(clientes)):
    profile = clientes[count]
    session = boto3.session.Session(profile_name=profile)
    ec2_cli = session.client(service_name='ec2', region_name='us-east-1')
    Workspaces_Client = session.client(service_name='workspaces', region_name='us-east-1')

    WorkSpaces = Workspaces_Client.describe_workspaces_connection_status()
    #print(WorkSpaces["WorkspacesConnectionStatus"])

    for WorkSpace in WorkSpaces["WorkspacesConnectionStatus"]:
        WorkspaceId = WorkSpace['WorkspaceId']
        ConnectionState = WorkSpace['ConnectionState']
        #print(WorkspaceId, ConnectionState)
        response = Workspaces_Client.describe_workspaces(WorkspaceIds=[WorkspaceId])
        UserName = response['Workspaces'][0]['UserName']
        f = open("WorkspaceId_User.txt", "a")
        print(WorkspaceId, UserName)
        WorkspaceId_UserTxt = WorkspaceId+" "+UserName+"\n"
        f.write(WorkspaceId_UserTxt)
        f.close()
        WorkspaceId_User = 'ws-5dcbksmd8'
        #reboot_workspaces = Workspaces_Client.reboot_workspaces(RebootWorkspaceRequests=[{'WorkspaceId': WorkspaceId_User}])
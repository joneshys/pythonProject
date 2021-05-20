import boto3
import mmap
clientes = ['QXSSDDBELLOPROD']
for count in range(len(clientes)):
    profile = clientes[count]
    session = boto3.session.Session(profile_name=profile)
    elbv2_cli = session.client(service_name='elbv2', region_name='us-east-1')
    ec2_cli = session.client(service_name='ec2', region_name='us-east-1')
    ec2_resource = session.resource(service_name='ec2', region_name='us-east-1')

    List_ELBV2 = response = elbv2_cli.describe_load_balancers()
    #print(List_ELBV2['LoadBalancers'])

    response = ec2_cli.describe_network_interfaces()
    for List_NI in response['NetworkInterfaces']:
        if 'ELB' in List_NI['Description']:
           print(List_NI['PrivateIpAddress'], List_NI['Description'])

           with open('hosts') as f:
               s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
               if s.find(b'digital') != -1:
                   print('True')
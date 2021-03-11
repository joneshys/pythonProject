import boto3

clientes = ['QXIMPTOSVALLETEST']

for count in range(len(clientes)):
    profile = clientes[count]
    session = boto3.session.Session(profile_name=profile)
    IAM = session.client(service_name='iam', region_name='us-east-1')

    user = IAM.create_user(UserName='jose_test',Tags=[{'Key':'Owner','Value':'QUIPUX'}])

    print(user)

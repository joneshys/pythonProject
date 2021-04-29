import boto3
#from account import clientes
from datetime import datetime
import sys

#clientes = ['default']
clientes = ['QXPROD']

now = datetime.now().date()
Hoy = str(now)

#New_Reposoroties = sys.argv[1]
New_Reposoroties = 'eliminar-este-repo-test'

for count in range(len(clientes)):
    profile = clientes[count]
    session = boto3.session.Session(profile_name=profile)
    ec2_re = session.resource(service_name='ec2', region_name='us-east-1')
    cloudwatch_cli = session.client(service_name='cloudwatch', region_name='us-east-1')
    ec2_cli = session.client(service_name='ec2', region_name='us-east-1')
    ecr = session.client(service_name='ecr', region_name='us-east-1')

    Describe_ECR = ecr.describe_repositories()

    #print(response['repositories'])
    repositoriesName = []
    if Describe_ECR['repositories'] != []:
        for repositoryName in Describe_ECR['repositories']:
            Name_Repository = repositoryName['repositoryName']
            repositoriesName.append(Name_Repository)
            #print(Name_Repository)
    #print(repositoriesName)
    if New_Reposoroties in repositoriesName:
        f = open('Log_ECR_Repositories.txt', "a")
        print('El repo de nombre '+New_Reposoroties+', ya se encuentra creado, por favor cambiar el nombre. A continuación se relaciona los repos creados')
        Logs_01 = 'El repo de nombre '+New_Reposoroties+', ya se encuentra creado, por favor cambiar el nombre.'
        Log_Create_Repo_01 = Hoy+' '+Logs_01 + '\n'
        f.write(Log_Create_Repo_01)
        f.close()
        if Describe_ECR['repositories'] != []:
            for i, repositoryName in enumerate(Describe_ECR['repositories'], 1):
                Name_Repository = repositoryName['repositoryName']
                print(i, Name_Repository, 'Fecha de consula')
    else:
        f = open('Log_ECR_Repositories.txt', "a")
        print('Se procede a la creación del repo '+New_Reposoroties)
        Logs = 'Se procede a la creación del repo '+New_Reposoroties
        Log_Create_Repo = Hoy+' '+Logs+'\n'
        f.write(Log_Create_Repo)
        f.close()
        Create_Repository = ecr.create_repository(repositoryName=New_Reposoroties)
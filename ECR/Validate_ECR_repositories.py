import boto3
from datetime import datetime
#from account import clientes
import sys

clientes = ['QXPROD']
#clientes = ['default']

now = datetime.now().date()
Hoy = str(now)

for count in range(len(clientes)):
    profile = clientes[count]
    session = boto3.session.Session(profile_name=profile)
    ec2_re = session.resource(service_name='ec2', region_name='us-east-1')
    cloudwatch_cli = session.client(service_name='cloudwatch', region_name='us-east-1')
    ec2_cli = session.client(service_name='ec2', region_name='us-east-1')
    ecr = session.client(service_name='ecr', region_name='us-east-1')

    Describe_ECR = ecr.describe_repositories()

    #print(response['repositories'])
    if Describe_ECR['repositories'] != []:
        for repositoryName in Describe_ECR['repositories']:
            Name_Repository = repositoryName['repositoryName']
            #print(Name_Repository) # Punto de control
            List_Images = ecr.list_images(repositoryName = Name_Repository)
            #print(Name_Repository,List_Images['imageIds']) # Punto de control
            if List_Images['imageIds'] != []:
                #print(Name_Repository, List_Images['imageIds'])
                f = open('Log_Delete_ECR_repositories_Empty.txt', "a")
                print('Este repo continen imagenes por lo cual no se borra '+Name_Repository)
                Logs_01 = 'Este repo continen imagenes por lo cual no se borra '+Name_Repository
                Logs_Delete_Repo_01 = Hoy+' '+Logs_01+'\n'
                f.write(Logs_Delete_Repo_01)
                f.close()
            if List_Images['imageIds'] == []:
                Delete_Repo_Empty = ecr.delete_repository(repositoryName = Name_Repository)
                f = open('Log_Delete_ECR_repositories_Empty.txt', "a")
                print('Se procedio con el borrado del repo vacío de nombre '+Name_Repository)
                Logs_02 = 'Se procedio con el borrado del repo vacío de nombre '+Name_Repository
                Logs_Delete_Repo_02 = Hoy+' '+Logs_02+'\n'
                f.write(Logs_Delete_Repo_02)
                f.close()
import boto3
import csv
from datetime import datetime
import collections
import pandas as pd
import os
import time
#os.remove("Count_Snapshot_EC2.csv")

clientes = ['QXSSDDATLANTICOTEST', 'QXSSDDATLANTICOPROD', 'QXSSDDBELLOTEST', 'QXSSDDBELLOPROD', 'QXSSDDCALITEST','QXSSDDCALIPROD', 'QXHUNITIPROD', 'QXIMPTOSVALLETEST', 'QXIMPTOSVALLEPROD', 'QXSSDDITAGUITEST','QXSSDDITAGUIPROD', 'QXSSDDPEREIRATEST', 'QXSSDDPEREIRAPROD', 'QXINTRUNTTEST', 'QXINTRUNTPROD', 'QXBIPROD','QXPROD', 'QXCOMPARENDERASSOMOSPROD', 'QXSSDDSABANETATEST', 'QXSSDDSABANETAPROD']
# clientes = ['QXSSDDBELLOPROD']
for count in range(len(clientes)):
    profile = clientes[count]
    session = boto3.session.Session(profile_name=profile)
    Certication_ACM = session.client(service_name='acm', region_name='us-east-1')


    response = Certication_ACM.list_certificates()
    CertificateSummaryList = response['CertificateSummaryList']

    for CertificateList in CertificateSummaryList:
        CertificateArn = CertificateList['CertificateArn']
        Describe_Certificate_ACM = Certication_ACM.describe_certificate(CertificateArn = CertificateArn)
        #print(Describe_Certificate_ACM)# Punto de control
        DomainName = Describe_Certificate_ACM['Certificate']['DomainName']
        SubjectAlternativeNames = Describe_Certificate_ACM['Certificate']['SubjectAlternativeNames']
        Subject = Describe_Certificate_ACM['Certificate']['Subject']
        Issuer = Describe_Certificate_ACM['Certificate']['Issuer']
        Status = Describe_Certificate_ACM['Certificate']['Status']
        NotBefore = datetime.now().date()
        NotAfter = Describe_Certificate_ACM['Certificate']['NotAfter'].date()
        Dias_restantes = NotAfter - NotBefore
        print(profile,Dias_restantes.days,DomainName, SubjectAlternativeNames, Subject, Issuer, Status, NotBefore, NotAfter)
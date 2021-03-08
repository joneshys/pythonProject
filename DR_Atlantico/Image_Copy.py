#!/usr/bin/env python3
import json
import boto3
from datetime import datetime

clientes = ['QXSSDDATLANTICOPROD']
for count in range(len(clientes)):
    profile = clientes[count]
    session = boto3.session.Session(profile_name=profile)
    appstream_client = session.client(service_name='appstream', region_name='us-east-1')
    Images_Appstream = appstream_client.describe_images(Type='PRIVATE')

    List_Days_Images_Appstream = []
    for images_appstream in Images_Appstream['Images']:
        #Name = images_appstream['Name']
        CreatedTime = images_appstream['CreatedTime'].replace(tzinfo=None).date()
        hoy = datetime.today().date()
        resta = hoy - CreatedTime
        List_Days_Images_Appstream.append(resta.days)
        #print(Name,resta.days) # Punto de control

    #print(List_Days_Images_Appstream) # Punto de control
    Min_Days_Images_Appstream = min(List_Days_Images_Appstream)
    #print(Min_Days_Images_Appstream)
    for images_appstream in Images_Appstream['Images']:
        Name = images_appstream['Name']
        CreatedTime = images_appstream['CreatedTime'].replace(tzinfo=None).date()
        hoy = datetime.today().date()
        resta = hoy - CreatedTime
        if resta.days == Min_Days_Images_Appstream:
            print(Name, resta.days)  # Punto de control
            response = appstream_client.copy_image(SourceImageName=Name,DestinationImageName= Name,DestinationRegion= 'us-west-2',DestinationImageDescription= 'Copia realizada para DR de la cuenta de Atlantico')
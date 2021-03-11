#!/usr/bin/env python3
import json
import boto3
from datetime import datetime
import sys

clientes = ['QXSSDDATLANTICOTEST']
#clientes = [sys.argv[1]]

for count in range(len(clientes)):
    profile = clientes[count]
    session = boto3.session.Session(profile_name=profile)
    Step_Functions = session.client(service_name='stepfunctions', region_name='us-east-1')

    List_Step_Functions = Step_Functions.list_state_machines()

    ListStepFunctions = List_Step_Functions['stateMachines']

    for List_Step_Function in ListStepFunctions:
        #print(List_Step_Function)# Punto de control
        stateMachineArn = List_Step_Function['stateMachineArn']
        Name_State_Machine = List_Step_Function['name']
        if 'create' in Name_State_Machine:
            Create_Environments = Step_Functions.start_execution(stateMachineArn=stateMachineArn)
            ResponseMetadata = Create_Environments['ResponseMetadata']['HTTPStatusCode']
            if 200 == ResponseMetadata:
                print("El ambiente "+profile+", estará activo dentro de 20 minutos.")
            else:
                print("El ambiente " + profile + ", está presentado problemas, por favor comuniquese al área de IT.")
                #print(ResponseMetadata) # Punto de control

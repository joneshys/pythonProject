import boto3

StackName='Stack-QX-NO-CROND'
FleetName='Fleet-QX-NO-CROND'

session = boto3.session.Session(profile_name='QXSSDDATLANTICOPROD')
ec2_re = session.resource(service_name='ec2', region_name='us-east-1')
cloudwatch_cli = session.client(service_name='appstream', region_name='us-east-1')
ec2_cli = session.client(service_name='ec2', region_name='us-east-1')
appstream_client = session.client(service_name='appstream', region_name='us-east-1')
#responses = appstream_client.describe_sessions(StackName='Stack-QX-NO-CROND', FleetName='Fleet-QX-NO-CROND')
responses = appstream_client.describe_sessions(StackName=StackName, FleetName=FleetName)

for respon in responses['Sessions']:
    Id_sesion = respon['Id']
    UserId = respon['UserId']
    ConnectionState = respon['ConnectionState']
    MaxExpirationTime = respon['MaxExpirationTime']
    EniPrivateIpAddress = respon['NetworkAccessConfiguration']['EniPrivateIpAddress']
    #Force_Brute_Close_Session = appstream_client.expire_session(SessionId=Id_sesion)
    # print(Id_sesion, UserId, ConnectionState, MaxExpirationTime, EniPrivateIpAddress) # Punto de control

    if 'NOT_CONNECTED' == ConnectionState:
        appstream_client.expire_session(SessionId=Id_sesion)
        # print('El ID de conexión ',Id_sesion,' del usuario ',UserId, ConnectionState, MaxExpirationTime, EniPrivateIpAddress) #Punto de control
        print('El ID de conexión ' +Id_sesion+' del usuario ' +UserId +' fue cerrado por completo, ya que presenta un estado ' +ConnectionState +'.')
    else:
        print('El ID de conexión ' +Id_sesion +' del usuario ' +UserId +', presenta un estado ' +ConnectionState +', por lo cual no sera cerrada la sesion.')

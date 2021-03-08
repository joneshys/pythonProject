import boto3
import sys

session = boto3.session.Session(profile_name='QXSSDDATLANTICOPROD')
ec2_re = session.resource(service_name='ec2', region_name='us-west-2')
cloudwatch_cli = session.client(service_name='appstream', region_name='us-east-1')
ec2_cli = session.client(service_name='ec2', region_name='us-west-2')
vpc = ec2_re.Vpc()








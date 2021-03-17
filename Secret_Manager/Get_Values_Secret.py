import boto3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

session = boto3.session.Session(profile_name='QXIMPTOSVALLEPROD')
ec2_re = session.resource(service_name='ec2', region_name='us-east-1')
cloudwatch_cli = session.client(service_name='appstream', region_name='us-east-1')
ec2_cli = session.client(service_name='ec2', region_name='us-east-1')
Secret = session.client(service_name='secretsmanager', region_name='us-east-1')
IAMClient = session.client(service_name='iam', region_name='us-east-1')

AccountAlias = IAMClient.list_account_aliases()['AccountAliases'][0].upper()
print(AccountAlias)
Get_Secret_Values = []
client = boto3.client('secretsmanager')
Secrte_Value = Secret.list_secrets()
SecretLists = Secrte_Value['SecretList']
for SecretList in SecretLists:
    Name = SecretList['Name']
    #print(Name)
    SecretString = Secret.get_secret_value(SecretId=Name)['SecretString']
    Get_Secret_Values.append(SecretString)
    #print(SecretString)

print(Get_Secret_Values[0])

mail_content = AccountAlias+' '+Get_Secret_Values[0]
sender_address = 'jose.benitez@quipux.com'
sender_pass = 'Neruda87$'
receiver_address = 'jose.benitez@quipux.com'

message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Sending of secret values from database RDS of the account'+' '+AccountAlias

#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))

session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')
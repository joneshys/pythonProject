import boto3
import smtplib
import ast
import email, smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

clientes = ['QXSSDDBELLOPROD', 'QXIMPTOSVALLEPROD']

for count in range(len(clientes)):
    profile = clientes[count]
    session = boto3.session.Session(profile_name=profile)
    ec2_re = session.resource(service_name='ec2', region_name='us-east-1')
    cloudwatch_cli = session.client(service_name='appstream', region_name='us-east-1')
    ec2_cli = session.client(service_name='ec2', region_name='us-east-1')
    Secret = session.client(service_name='secretsmanager', region_name='us-east-1')
    IAMClient = session.client(service_name='iam', region_name='us-east-1')

    Secrte_Value_Rotate = Secret.list_secrets()
    SecretLists = Secrte_Value_Rotate['SecretList']
    # print(SecretLists[0])

    ## Rotation passwd RDS
    RotationLambdaARN = SecretLists[0]['RotationLambdaARN']
    # print(RotationLambdaARN)
    for SecretList in SecretLists:
        Name = SecretList['Name']
        SecretString = Secret.get_secret_value(SecretId=Name)
        SecretString_ARN = SecretString['ARN']
        SecretString_Name = SecretString['Name']
        # print(SecretString)
        rotate_secret = Secret.rotate_secret(SecretId=Name, RotationLambdaARN=RotationLambdaARN,
                                         RotationRules={'AutomaticallyAfterDays': 25})

    ## Get value secret passwd EDS
    AccountAlias = IAMClient.list_account_aliases()['AccountAliases'][0].upper()
    # print(AccountAlias)
    Get_Secret_Values = []
    client = boto3.client('secretsmanager')
    Secrte_Value = Secret.list_secrets()
    SecretLists = Secrte_Value['SecretList']
    for SecretList in SecretLists:
        Name = SecretList['Name']
        # print(Name)
        SecretString = Secret.get_secret_value(SecretId=Name)['SecretString']
        Get_Secret_Values.append(SecretString)
        # print(SecretString)

    ## Create file .txt for add values secret
    List_Format_Secret_Values = []
    my_dict = ast.literal_eval(Get_Secret_Values[0])
    for k,v in my_dict.items():
        list_1 = '%s -> %s'%(k,v)
        print(list_1)
        List_Format_Secret_Values.append(list_1)
    f = open("test.txt", "a")
    mail_content_1 = AccountAlias+'\n'+List_Format_Secret_Values[0]+'\n'+List_Format_Secret_Values[1]+'\n'+List_Format_Secret_Values[2]+'\n'+List_Format_Secret_Values[3]+'\n'+List_Format_Secret_Values[4]+'\n'+List_Format_Secret_Values[5]+'\n'+List_Format_Secret_Values[6]+'\n'+'--------------------------'+'\n'
    f.write(mail_content_1)
    f.close()

## Send mail with the file attach .txt
sender_address = 'jose.benitez@quipux.com'
sender_pass = 'Neruda87$'
receiver_address = "jose.benitez@quipux.com,juan.villa@quipux.com"

message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Sending of secret values from database RDS of the account'+' '+AccountAlias
mail_content = 'Sending of secret values from database RDS of the account AWS'
# message.attach(MIMEText(mail_content, 'plain'))
message.attach(MIMEText(mail_content,'plain'))
filename = 'test.txt'
with open(filename, 'rb') as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header("Content-Disposition",f"attachment; filename= {filename}")
message.attach(part)
text = message.as_string()

session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(sender_address, sender_pass)
text = message.as_string()
session.sendmail(sender_address, receiver_address.split(','), text)
session.quit()
print('Mail Sent')
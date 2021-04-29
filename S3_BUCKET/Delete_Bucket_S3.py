import boto3
#from account import clientes
#clientes = ['QXSSDDATLANTICOTEST']#,'QXSSDDATLANTICOPROD']#,'QXSSDDBELLOTEST','QXSSDDBELLOPROD','QXSSDDCALITEST','QXSSDDCALIPROD','QXHUNITIPROD','QXSSDDPEREIRATEST','QXSSDDPEREIRAPROD','QXINTRUNTTEST','QXINTRUNTPROD','QXBIPROD','QXPROD','QXCOMPARENDERASSOMOSPROD','QXSSDDSABANETATEST','QXSSDDSABANETAPROD']
clientes = ['QXSSDDCALIPROD']
for count in range(len(clientes)):
    profile = clientes[count]
    session = boto3.session.Session(profile_name=profile)
    Client_S3= session.client(service_name='s3', region_name='us-east-1')
    List_S3= Client_S3.list_buckets()

    for Bucket_S3 in List_S3['Buckets']:
        #print(Bucket_S3)
        Name_S3 = Bucket_S3['Name']
        if 'cloudtrailbucket' in Name_S3:
            List_Object_Bucket = Client_S3.list_objects_v2(Bucket=Name_S3)
            #print(List_Object_Bucket)
            if 'Contents' in List_Object_Bucket:
                for item in List_Object_Bucket['Contents']:
                    print('deleting file', item['Key'])
                    #Client_S3.delete_object(Bucket=Name_S3, Key=item['Key'])
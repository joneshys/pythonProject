from urllib.request import urlopen
import json
import pandas as pd
import requests

#df = pd.read_json('pricing.us-east-1.amazonaws.com/offers/v1.0/aws/index.json')
url_aws_presing = requests.get('https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/index.json')

data = json.loads(url_aws_presing.content)


resp = requests.get('http://ip-api.com/json/208.80.152.201')
#data = json.loads(resp.content)

print(data['offers']['AmazonEC2'])
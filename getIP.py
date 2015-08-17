"""Powered By Jack---http://renjikai.com/
   Based On http://v2ex.com/t/200342 GPU"""

import urllib,time,json,hashlib,requests
from time import gmtime

"""Get Correct IP"""
params = urllib.urlencode({'ip': 'myip'})
f = urllib.urlopen("http://ip.taobao.com/service/getIpInfo2.php", params)
ddata=json.loads(f.read())
wan_ip = ddata['data']['ip']

"""Some Settings You Need To Set"""
api_url = "https://www.cloudxns.net/api2/record/RECORD_ID"
api_key = "API_KEY"
api_secret = "API_SECRET"
Domain_ID = DOMAIN_ID
ttl = 120
line_id = 1
host = "HOST"
Domain_type = "A"

request_data = {
"domain_id": Domain_ID,
"host": host,
"value": wan_ip,
"type": Domain_type,
"ttl": ttl,
"line_id": line_id
}

request_time = time.strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime())
hmac = hashlib.md5(api_key+api_url+str(json.dumps(request_data))+request_time+api_secret).hexdigest()
headers = {
'API-KEY' : api_key,
'API-REQUEST-DATE' : request_time,
'API-HMAC' : hmac,
'API-FORMAT' : 'json'
}
""" ignore urlib3 warnings """
requests.packages.urllib3.disable_warnings()
r = requests.put(url=api_url,headers=headers,data=json.dumps(request_data),verify=False)
response = r.json()
response_data = response[u'data']
print response_data
exit()

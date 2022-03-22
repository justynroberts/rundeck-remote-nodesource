import http.client
import yaml
import json
import sys

file = sys.argv[1] 
host = sys.argv[2] 
apitoken = sys.argv[3] 
index = sys.argv[4] 
project = sys.argv[5] 

with open(file, 'r') as yaml_in:
    yaml_object = yaml.safe_load(yaml_in) # yaml_object will be a list or a dict
    json_payload = json.dumps(yaml_object)

conn = http.client.HTTPSConnection(host)
payload = json_payload
headers = {
    'X-Rundeck-Auth-Token':apitoken,
    'Content-Type': "application/json",
    }
conn.request("POST", "/api/41/project/"+project+"/source/"+index+"/resources?=", payload, headers)
res = conn.getresponse()
data = res.read()

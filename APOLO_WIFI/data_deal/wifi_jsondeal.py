import json
import re

with open('wifispot.json' , 'r') as reader:
    json_file = json.loads(reader.read())
out = []
count = 0
for i in json_file:
    out.append([])
    jfile=re.split(',',str(i))
    out[count].append(jfile[1].replace("\'熱點名稱","{\'hot_spot_name"))
    out[count].append(jfile[6].replace("緯度","longitude"))
    out[count].append(jfile[7].replace("經度","latitude"))
    count+=1
json_out="["
for i in range(0,count):
    json_out+=out[i][0]+","+out[i][1]+","+out[i][2]+","

json_out = json_out[:json_out.__len__()-1]
json_out=json_out+"]"
json_out=json_out.replace("\'","\"")
json_out =json_out.replace(" ","")
fp = open("wifispot_clear.json", "a")
fp.write(json_out)
fp.close()

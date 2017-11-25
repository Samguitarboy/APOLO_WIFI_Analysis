import json
import re
import urllib
from urllib.request import urlopen
import json


def getGeoForAddress(address):
    addressUrl = "http://maps.googleapis.com/maps/api/geocode/json?address=" + address
    addressUrlQuote = urllib.parse.quote(addressUrl, ':?=/')
    response = urlopen(addressUrlQuote).read().decode('utf-8')
    responseJson = json.loads(response)
    lat = responseJson.get('results')[0]['geometry']['location']['lat']
    lng = responseJson.get('results')[0]['geometry']['location']['lng']
    print(address + '的經緯度是: %f, %f'  %(lat, lng))
    return [lat, lng]


with open('20170818084255321.json', "r", errors='ignore') as reader:
    json_file = json.loads(reader.read())
out = []
count = 0
for i in json_file:
    out.append([])
    jfile = re.split(',', str(i))
    if (jfile[5].find("餐") != -1):
        out[count].append(jfile[2])
        out[count].append(jfile[3])
        out[count].append(jfile[5])
        count += 1


lat_lng=[]
for i in range(0,count):
    temp=str(out[i][1]).replace(" \'商業地址\': \'","")
    temp = temp.replace("\'","")
    lat_lng.append(getGeoForAddress(temp))
   # print(lat_lng)
print (lat_lng)

'''for i in range(0, count):
    print(out[i])'''
json_out = "["
for i in range(0, count):
    json_out += out[i][0] + "," + out[i][1] + "," + out[i][2] + ","
json_out = json_out[:json_out.__len__() - 1]
json_out = json_out + "]"
json_out = json_out.replace("\'", "\"")
json_out = json_out.replace(" ", "")
#print(json_out)

'''fp = open("restaurant_clear.json", "a")
fp.write(json_out)
fp.close()'''

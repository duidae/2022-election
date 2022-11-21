from urllib.request import urlopen
import json
import pandas as pd
import schedule

def update_excel():
    print("loading json...")
    url = "https://api.github.com"
    #url = "https://download.2022dl.nat.gov.tw/test/running_P.json"
    response = urlopen(url)
    data_json = json.loads(response.read())
    df = pd.read_json()
    df.to_csv(r'Path where the new CSV file will be stored\New File Name.csv', index = None)

"""
import urllib
import urllib2
username = "username"
password = "password"
url = 'http://url.com/'
values = { 'username': username,'password': password }
data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
result = response.read()
print result
"""

schedule.every(5).seconds.do(update_excel)
#schedule.every(10).minutes.do(update_excel)

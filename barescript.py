import requests
import sys
import json

headers = {
  'authority': 'app.publer.io',
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/json;',
  'origin': 'https://publer.io',
  'referer': 'https://publer.io/',
  'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'sec-gpc': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
url = "https://app.publer.io/hooks/media"
url1 = input('url - ')
original_payload = "{\"url\":\"https://youtu.be/vjhKzvhW-fc?si=J6sSwdaKu_uYu20d\",\"iphone\":false}"
payload = original_payload.replace("https://youtu.be/vjhKzvhW-fc?si=J6sSwdaKu_uYu20d", url1)
response = requests.post(url, headers=headers, data=payload)
req1 = json.loads(response.text)
jobid = req1['job_id']
while True:

    data1 = requests.get('https://app.publer.io/api/v1/job_status/' + jobid, headers=headers)
    getdata = json.loads(data1.text)
    print(getdata['status'])
    try:
        
        print(getdata['payload'][0]['path'])
        print(getdata['payload'][0]['path'])
        
    except:
        pass

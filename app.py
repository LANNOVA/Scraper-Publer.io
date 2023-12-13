import requests
import sys
import json
from tkinter import Tk, Label, Entry, Button

def submit_callback():
   
    data1 = requests.get('https://app.publer.io/api/v1/job_status/' + jobid, headers=headers)
    getdata = json.loads(data1.text)
    print(getdata['status'])
    try:
        
        print(getdata['payload'][0]['path'])
        open_in_browser(getdata['payload'][0]['path'])
        
    except:
        pass


def open_in_browser(url):
    import webbrowser
    webbrowser.open(url)
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

root = Tk()
root.title("Online Video Downloader")


def submit_url():
    global jobid
    url = "https://app.publer.io/hooks/media"
    url1 = url_entry.get()
    original_payload = "{\"url\":\"https://youtu.be/vjhKzvhW-fc?si=J6sSwdaKu_uYu20d\",\"iphone\":false}"
    payload = original_payload.replace("https://youtu.be/vjhKzvhW-fc?si=J6sSwdaKu_uYu20d", url1)
    response = requests.post(url, headers=headers, data=payload)
    req1 = json.loads(response.text)
    jobid = req1['job_id']
    while True:
        submit_callback()

Label(root, text="Enter URL:").pack(pady=10)
url_entry = Entry(root, width=40)
url_entry.pack(pady=10)
submit_button = Button(root, text="Submit", command=submit_url)
submit_button.pack(pady=10)

root.mainloop()

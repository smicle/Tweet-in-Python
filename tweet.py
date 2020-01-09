import os
import sys
import json
import yaml
import config
from requests_oauthlib import OAuth1Session

with open(f"{os.path.dirname(sys.argv[0])}/api.yaml") as file:
    y = yaml.safe_load(file)
    CLIENT_KEY = y["CLIENT_KEY"]
    CLIENT_SECRET = y["CLIENT_SECRET"]
    RESOURCE_OWNER_KEY = y["RESOURCE_OWNER_KEY"]
    RESOURCE_OWNER_SECRET = y["RESOURCE_OWNER_SECRET"]

def tweet(text):
    session = OAuth1Session(client_key=CLIENT_KEY, client_secret=CLIENT_SECRET, resource_owner_key=RESOURCE_OWNER_KEY, resource_owner_secret=RESOURCE_OWNER_SECRET)
    res = session.post("https://api.twitter.com/1.1/statuses/update.json", params={"status": text})
    if res.status_code != 200:
        return res.status_code
    else:
        r = json.loads(res.text)
        time = r["created_at"]
        text = r["text"].replace("\n", "\\n")
        return "Time: {}\nText: {}".format(time, text)

def main():
    text = sys.argv[1].replace("\\n", "\n")
    res = tweet(text)
    print(res)

if __name__ == "__main__":
    main()

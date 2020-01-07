import sys
import yaml
import config
import json
from requests_oauthlib import OAuth1Session

with open("api.yaml") as file:
    data = yaml.safe_load(file)
    CLIENT_KEY = data["CLIENT_KEY"]
    CLIENT_SECRET = data["CLIENT_SECRET"]
    RESOURCE_OWNER_KEY = data["RESOURCE_OWNER_KEY"]
    RESOURCE_OWNER_SECRET = data["RESOURCE_OWNER_SECRET"]

def tweet(text):
    twitter = OAuth1Session(client_key=CLIENT_KEY, client_secret=CLIENT_SECRET, resource_owner_key=RESOURCE_OWNER_KEY, resource_owner_secret=RESOURCE_OWNER_SECRET)
    url = "https://api.twitter.com/1.1/statuses/update.json"
    params = {"status": text}

    res = twitter.post(url, params=params)

    if res.status_code != 200:
        return res.status_code
    else:
        res = json.loads(res.text)
        time = res["created_at"]
        text = res["text"].replace("\n", "\\n")
        return "Time: {}\nText: {}".format(time, text)

def main():
    args = sys.argv
    text = args[1].replace("\\n", "\n")
    res = tweet(text)
    print(res)

if __name__ == "__main__":
    main()

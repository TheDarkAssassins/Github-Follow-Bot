import requests
import json
import argparse
import tqdm
import time
from base64 import b64encode
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--token', help="Your GitHub Personal Access Token", required=True)
parser.add_argument('-m', '--my-username', help="Your GitHub Username", required=True)
parser.add_argument('-f', '--file', help="Followers File to Unfollow", required=True)
args = parser.parse_args()

HEADERS = {"Authorization": "Basic " + b64encode(str(args.my_username + ":" + args.token).encode('utf-8')).decode('utf-8')}
sesh = requests.session()
sesh.headers.update(HEADERS)
with open(args.file, 'r+') as f:
    obj = json.load(f)
    print("Unfollowing Users... This WILL take a while!")
    for user in tqdm.tqdm(obj, ncols=35, smoothing=True, bar_format='[PROGRESS] {n_fmt}/{total_fmt} | {bar}'):
        while True:
            time.sleep(5)
            res = sesh.delete('https://api.github.com/user/following/' + user)
            if res.status_code != 204:
                print(res.status_code)
                print("We may have been rate-limited, waiting until it stops!")
                time.sleep(60)
            else:
                break
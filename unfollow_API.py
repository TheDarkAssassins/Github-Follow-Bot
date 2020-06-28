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
parser.add_argument('-u', '--user-target', help="User to grab followers from")
parser.add_argument('-f', '--file', help="unfollow users from a File pre-generated")
parser.add_argument('-a', '--all', help="Unfollow all your followers", action="store_true")
parser.add_argument('-mf', '--max-followers', help="Max Number of Followers to unfollow")
args = parser.parse_args()

HEADERS = {"Authorization": "Basic " + b64encode(str(args.my_username + ":" + args.token).encode('utf-8')).decode('utf-8')}

res = requests.get("https://api.github.com/user", headers=HEADERS)

if res.status_code != 200:
    print("Failure to Authenticate, please check Personal Access Token and Username!")
    exit(1)
else:
    print("Authentication Succeeded!")
sesh = requests.session()
sesh.headers.update(HEADERS)
if not args.file:

    target = args.my_username
    res = sesh.get("https://api.github.com/users/" + target + "/following")


    links_array = requests.utils.parse_header_links(res.headers['Link'].rstrip('>').replace('>,<', ',<'))
    last_link = links_array[1]['url']
    last_page = last_link.split('=')[-1]
    users_to_follow = []
    mnof = args.max_followers
    print('Grabbing People to unfollow\nThis may take a while... there are ' + str(last_page) + ' pages to go through.')
    for page in tqdm.tqdm(range(1, int(last_page)), ncols=35, smoothing=True, bar_format='[PROGRESS] {n_fmt}/{total_fmt} | {bar}'):
        res = sesh.get('https://api.github.com/users/' + target + "/following?limit=100&page=" + str(page)).json()
        for user in res:
            users_to_follow.append(user['login'])
        if mnof != None:
            if len(users_to_follow) >= int(mnof):
                break
    filename = str(datetime.now().strftime('%m-%d-%YT%H-%M-%S')) + "-" + str(len(users_to_follow)) + "_FOLLOWING.json"
    with open(filename, 'w+') as f:
        json.dump(users_to_follow, f, indent=4)
else:
    filename = args.file

with open(filename, 'r+') as f:
    obj = json.load(f)
    print("Starting to unfollow Users... This WILL Take a while, we must avoid being rate-limited!")
    for user in tqdm.tqdm(obj, ncols=35, smoothing=True, bar_format='[PROGRESS] {n_fmt}/{total_fmt} | {bar}'):
        while True:
            time.sleep(2)
            res = sesh.delete('https://api.github.com/user/following/' + user)
            if res.status_code != 204:
                print(res.status_code)
                print("We may have been rate-limited, waiting until it stops!")
                time.sleep(60)
            else:
                break

# GitHub Follow Bot

Started as a fork, completely changed around code. **I do not recommend you use this a lot, you may get banned from GitHub but I'm not sure! This was just a PoC**

## Installing

```
pip install -r requirements.txt
```

## How to Use

### Get PAT:

https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line **READ HERE**

Make sure to enable the `user` scope and all subscopes inside of that permission!

#### To Follow:

```
python follow_bot.py -t <PERSONAL_ACCESS_TOKEN> -m <YOUR_USERNAME> -u <TARGET_TO_GRAB_FOLLOWERS_FROM> # To follow and generate a new followers file

python follow_bot.py -t <PERSONAL_ACCESS_TOKEN> -m <YOUR_USERNAME> -f <FILENAME> # Follow users from a pre-generated file

python follow_bot.py -t <PERSONAL_ACCESS_TOKEN> -m <YOUR_USERNAME> -mf 1000 # Cap followers to 1000
```

#### To Unfollow:

```
python unfollow_bot.py -t <PERSONAL_ACCESS_TOKEN> -m <YOUR_USERNAME> -f <FILENAME> # Unfollow users from file

python unfollow_bot.py -t <PERSONAL_ACCESS_TOKEN> -m <YOUR_USERNAME> -f <FILENAME> -mu 100 # Unfollow users from file but cap at 100

python unfollow_bot.py -t <PERSONAL_ACCESS_TOKEN> -m <YOUR_USERNAME> -a # Unfollow Everybody

python unfollow_bot.py -t <PERSONAL_ACCESS_TOKEN> -m <YOUR_USERNAME> -a -mu 40# Unfollow Everybody Cap at 40
```

## Why I did this?

Selenium is slow and ugly, APIs are nice to use and we can let this run in the background. Also allows for less resources to be used + storing files of who you followed so you don't lose people you really do want to follow!

Somewhere, I read:
- One in ten people you follow will follow you back.
- One in hundred people you follow will star your repos.
- One in thousand people you follow will fork your repos.

Might be true, might be not 🤷‍.

Rewritten to use GitHub API from Selenium by [M4cs](https://github.com/M4cs)

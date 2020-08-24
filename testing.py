from time import sleep
from selenium import webdriver

import os
import sys
import csv
import ssl
import time
import json
import random

# Load json file for credentials
with open("config.json") as f:
    credentials = json.load(f)

    cred_login = credentials["login"]
    cred_password = credentials["password"]

from instapy import InstaPy
session = InstaPy(username=cred_login,password=cred_password,page_delay=2)
session.login()

hashtag_main_list = [
    "worldcode",
    "programmerrepublic",
    "coding",
    "code",
    "programmerslife",
    "webdev",
    "developerslife",
    "devlife",
    "codinglife",
    "100daysofcode",
    "programming",
    "machinelearning",
    "deeplearning",
    "datascientist",
    "workhardanywhere",
    "webdevelopment",
    "desksetup",
    "workstation",
    "pcsetup",
    "roominspiration",
    "dreamsetup",
    "deskinspiration",
    "deskspace",
    "deskinspo",
    "workspacegoals",
    "officegoals",
    "officeinspiration",
    "minimalsetups"
]

hashtag_test_list = [
    "minimalsetups"
]

session.set_quota_supervisor(enabled=True,
                             peak_likes_daily=95654,
                             peak_likes_hourly=1263
                            )

session.like_by_tags(hashtag_test_list,amount=169,sleep_delay=random.randint(1,3))
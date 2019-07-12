import subprocess
import os
import json

RSYNC = '/usr/bin/rsync'
RSYNC_SOURCE = "rsync://rsync.macports.org/macports//trunk/dports/PortIndex_darwin_18_i386/PortIndex.json"
BASE_DIR = os.path.abspath(os.path.dirname(__name__))
JSON_FILE = os.path.join(BASE_DIR, 'portindex.json')


def sync():
    subprocess.call([RSYNC, RSYNC_SOURCE, JSON_FILE])
    return


def open_file():
    with open(JSON_FILE, "r", encoding='utf-8') as file:
        data = json.load(file)
    return data


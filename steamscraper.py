#! /usr/bin/env python2

import argparse
import urllib
import os
from steamapiwrapper.SteamGames import Games

appid = -1

def main():
    steamapi = Games()
    _parse_args()
    for game in steamapi.get_info_for(appid, "us"):
        if not os.path.exists(game.name):
            os.makedirs(game.name)
        for screenshot in game.raw_json['screenshots']:
            _download_image(screenshot['path_full'], os.path.join(game.name, str(screenshot['id'])))
        _download_image(game.header_image, game.name)

def _download_image(url, name):
    urllib.urlretrieve(url, name + ".jpg")

def _parse_args():
    global appid
    parser = argparse.ArgumentParser(description="Grabs Steam screenshots for a specific game")
    parser.add_argument("appid", type=int, nargs=1, help="Steam appid to grab default screenshots for")
    args = parser.parse_args()
    appid = args.appid

if __name__ == "__main__":
    main()

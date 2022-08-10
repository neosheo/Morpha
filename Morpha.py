#!/usr/bin/env python3

import subprocess
from lib.selenium_functions import start_torrent, rd_login, kill_chrome, start_i2p_torrent
import json
import time

# post magnet link to real debrid
print('Posting link...')
subprocess.run(['./scripts/post_links.sh'])

# press the start torrent button
print('\nPressing start button...')
rd_login()
start_torrent()

# get name of torrent
with open('.torrent_name', 'r') as f:
	filename = f.readlines()[0]
	filename = filename.replace('+', ' ').replace('%3A', '_')

torrents = []

def get_current_list():
	# get list of torrents from real debrid
	subprocess.run(['./scripts/get_torrents_list.sh'])
	# convert list to json
	with open('.torrents_list', 'r') as f:
		# if torrents is not empty, clear it
		if torrents:
			del torrents[0]
		torrents.append(json.load(f))

print('\nFetching list of torrents...')
get_current_list()

# find requested torrent in list (torrents is a list in a list)
print('\nFinding requested torrent...')
for torrent in torrents[0]:
	if filename in torrent['filename']:
		if torrent['status'] == 'downloaded':
			link = torrent['links'][0]
			with open('.download_link', 'w') as f:
				f.write(link)
			break
		else:
			while True:
				time.sleep(900)
				get_current_list()
				if torrent['status'] == 'downloaded':
					link = torrent['links'][0]
					with open('.download_link', 'w') as f:
						f.write(link)
					break
	else:
		continue

# download file and upload to i2p
print('\nUnrestricting link...')
subprocess.run(['./scripts/unrestrict_link.sh'])
with open('.unrestricted_info', 'r') as f:
	unrestricted = json.load(f)
with open('.unrestricted_link', 'w') as f:
	f.write(unrestricted['download'])
print('\nDownloading file...')
subprocess.run(['./scripts/download_file.sh'])
print('\nCreating torrent...')
subprocess.run(['./scripts/make_torrent.sh'])
start_i2p_torrent()
kill_chrome()

#!/bin/bash

# post scraped magnet link to real debrid
magnet=`cat .magnet_link`

token=`cat .access_token`

curl -X POST \
    -H "Authorization: Bearer $token" \
    "https://api.real-debrid.com/rest/1.0/torrents/addMagnet?" -d "magnet=$magnet"

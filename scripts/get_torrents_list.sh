#!/bin/bash

token=`cat .access_token`

curl -X GET \
    -H "Authorization: Bearer $token" \
    "https://api.real-debrid.com/rest/1.0/torrents/" > .torrents_list

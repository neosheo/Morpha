#!/bin/bash

link=`cat .download_link`

token=`cat .access_token`

# get unrestricted download link
curl -X POST \
	-H "Authorization: Bearer $token" \
	"https://api.real-debrid.com/rest/1.0/unrestrict/link?" -d "link=$link" > .unrestricted_info

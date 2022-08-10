#!/bin/bash

name=`cat .torrent_name`
link=`cat .unrestricted_link`
mkdir downloads/$name
curl $link > downloads/$name/$name

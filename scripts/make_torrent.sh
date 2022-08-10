#!/bin/bash

cd downloads

# get name of torrent and tracker info to make torrent
torrent_name=`cat ../.torrent_name`
tracker=`cat ../.tracker`

# move to i2p and create torrent
cp -r $torrent_name ~/.i2p/i2psnark && rm -r $torrent_name
cd ~/.i2p/i2psnark
mktorrent -a $tracker -o $torrent_name.torrent $torrent_name

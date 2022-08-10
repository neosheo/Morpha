#!/usr/bin/env python3

from lib.selenium_functions import x1337x, kill_chrome

# let user choose the site they want to scrape
print('Which site do you want to use?\n')
site = input('[0] 1337x, [1] rarbg, [2] torrent galaxy ')

# run chosen scraper function
if site == '0':
    x1337x()
else:
    print('site not supported yet.')
    exit()
kill_chrome()

# get name of torrent from magnet link
with open('.magnet_link', 'r') as f:
    magnet = f.readlines()[0]
    magnet_sub = magnet.partition('&dn=')[2]
    title = magnet_sub.partition('&')[0]
    with open('.torrent_name', 'w') as f2:
        f2.write(title)
print(title)

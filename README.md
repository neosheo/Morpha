![Morpha](https://user-images.githubusercontent.com/100803853/183967036-29efd3ed-85c8-4d87-8a67-494146c319e6.png)

# Morpha
This project allows a user to add a magnet link to their Real Debrid account, download that link, and then add it as a torrent to I2P to seed.

# Dependencies
Users will need to have the following:
- a premium Real Debrid account (https://real-debrid.com/)
- I2P (https://geti2p.net/en/download)
- Google Chrome (https://www.google.com/chrome/)
- Chromedriver (https://chromedriver.chromium.org/downloads)
- Selenium Python bindings (https://pypi.org/project/selenium/)
- curl (https://curl.se/download.html)
- mktorrent (https://guix.gnu.org/packages/mktorrent-1.1/)

# Installation & Use
- clone the repository
- install dependencies
- run scripts/set_credentials (input your real debrid username, password, access token, and a torrent tracker url)
- run Scraper.py to find a magnet link (currently only supports https://1337x.to)
- run Morpha.py to download the torrent and upload to I2P

# Future Implementations
- install script
- additional site scrapers

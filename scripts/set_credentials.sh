#/bin/bash

# set real debird account details
echo 'Enter your Real Debrid credentials'
read -p 'username: ' user
read -p 'password: ' pass
read -p 'access token: ' token

echo 'Enter the I2P tracker you wish to use'
read -p 'tracker: ' tracker

echo RD_USER=$user > ../.env
echo RD_PASS=$pass >> ../.env
echo $token > ../.access_token
echo $tacker > ../.tracker

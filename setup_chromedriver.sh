#!/bin/sh

CHROME_DRIVER_VERSION=`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE_80`
echo 'Downloading...'
wget -N http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip -P ~/
echo 'Unziping...'
unzip ~/chromedriver_linux64.zip -d ~/
echo 'Cleaning...'
rm ~/chromedriver_linux64.zip
echo 'Setuping...'
mv -f ~/chromedriver $(pwd)/venv/bin
#sudo chown root:root /usr/local/bin/chromedriver
#sudo chmod 0755 /usr/local/bin/chromedriver
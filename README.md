# mtgscan
## install
1. after installing rabsberrypi os, enable SSH on rpi
2. remove rabsberrypi.local from win known_hosts (cause key wont match)
3. add new connection with pi@raspberrypi.local
4. connect

## setup
1. `sudo apt-get update`
2. `sudo apt dist-upgrade`
3. `sudo apt install git`
4. `sudo raspi-config` enable camera at interface options and reboot
5. `git config --global user.email "<email>"`
6. `git config --global user.name "Martan"`

## update & upgrade rpi
1. `sh update.sh`
2. `sudo reboot`

## connect to mysql
1. `sudo mysql -u root -p`


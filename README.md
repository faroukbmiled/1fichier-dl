**Note:**
- This a fork of the original project 
- Maintained for now
- Fixed it to work with Python >= 3.10.x
- Changed Proxy provider to proxyscrape since Proxyscan is dead
- You can edit proxy api from settings.json

## Usage
- Make sure Python3 is installed properly, do `pip install -r requirements.txt` and then you can use `download.sh` to launch the program
- Create $HOME/1fichier-dl.conf config file or windows directory instead of $HOME

Example config file:
```
[aria2]
host = HOST
port = PORT_NUMBER
token = YOUR_TOKEN
```

Change according to your configuration

## Fork Features
- paulo27ms fixed looping bug when proxy works but download fails
- Add aria2 integration from oureveryday
- Add token authentication
- Use config file instead of hardcoded values
- Blacklist failing proxies

## Todo
- Integrate gui with aria2

# 1fichier-dl
<p align="center">
  <b>1Fichier Download Manager.</b>
</p>



## Features
⭐ Manage your downloads

⭐ Bypass time limits

## Credits
* All icons, including the app icon, were provided by [Feather](https://feathericons.com/).
* Proxies provided by [Proxyscan](https://www./).
* paulo27ms for proxy stuff
* oureveryday for aria2 stuff

## Notes
if gui not working on LXDE or any other desktop environments, try these commands:
- pip install pyqt6
- sudo apt-get install '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev
- sudo apt install libxcb-xinerama0 

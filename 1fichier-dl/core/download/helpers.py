import requests
import math
import os
import time
import lxml.html
import json



Defaultapi = {"PorxyAPI": "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"}
Path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
if not os.path.exists(os.path.join(Path, 'settings.json')):
  with open(os.path.join(Path, 'settings.json'), 'w') as f:
    json.dump(Defaultapi, f, indent=4)
try:
    with open(os.path.join(Path, 'settings.json')) as f:
        load = json.load(f)
        settings = load["PorxyAPI"]
except:
    settings = Defaultapi['PorxyAPI']


FIRST_RUN = True
PROXY_TXT_API = settings
PLATFORM = os.name




def get_proxies(settings: str) -> list:
    '''
    Get proxies (str) from API.
    '''
    global FIRST_RUN

    if FIRST_RUN:
        FIRST_RUN = False
        return [None]

    r_proxies = requests.get(f'{settings if settings else PROXY_TXT_API}').text.splitlines()
    proxies = []
    for p in r_proxies:
        proxies.append({'https': f'{p}'} if PLATFORM == 'nt' else {'https': f'http://{p}'})
    print(proxies)
    return proxies

def convert_size(size_bytes: int) -> str:
    '''
    Convert from bytes to human readable sizes (str).
    '''
    # https://stackoverflow.com/a/14822210
    if size_bytes == 0:
        return '0 B'
    size_name = ('B', 'KB', 'MB', 'GB', 'TB')
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return '%s %s' % (s, size_name[i])

def download_speed(bytes_read: int, start_time: float) -> str:
    '''
    Convert speed to human readable speed (str).
    '''
    if bytes_read == 0:
        return '0 B/s'
    elif time.time()-start_time == 0:
        return '- B/s'
    size_name = ('B/s', 'KB/s', 'MB/s', 'GB/s', 'TB/s')
    bps = bytes_read/(time.time()-start_time)
    i = int(math.floor(math.log(bps, 1024)))
    p = math.pow(1024, i)
    s = round(bps / p, 2)
    return '%s %s' % (s, size_name[i])

def get_link_info(url: str) -> list:
    '''
    Get file name and size.
    '''
    try:
        r = requests.get(url)
        html = lxml.html.fromstring(r.content)
        if html.xpath('//*[@id="pass"]'):
            return ['Private File', '- MB']
        name = html.xpath('//td[@class=\'normal\']')[0].text
        size = html.xpath('//td[@class=\'normal\']')[2].text
        return [name, size]
    except:
        return None

def is_valid_link(url: str) -> bool:
    '''
    Returns whether `url` is a valid 1fichier domain.
    '''
    domains = [
        '1fichier.com/',
        'afterupload.com/',
        'cjoint.net/',
        'desfichiers.com/',
        'megadl.fr/',
        'mesfichiers.org/',
        'piecejointe.net/',
        'pjointe.com/',
        'tenvoi.com/',
        'dl4free.com/'
    ]

    return any([x in url.lower() for x in domains])

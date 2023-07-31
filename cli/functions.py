import json
import sys
from pathlib import Path
sys.path.append(str(Path.home() / ".kip/lib"))
import const

def __set_config(args):
    try:
        with open(const.KIP_CONFIGURATIONS_FILE, 'r+') as reader:
            configurations = json.loads(reader.read())
            n_configurations = {
                **configurations,
                **args
            }
        return True
    except Exception as e:
        print(str(e))
        return False

def set_registry_url(url):
    if url[-1] == '/':
        url = url[0:-1]
    return __set_config({
        'registry.url': url
    })
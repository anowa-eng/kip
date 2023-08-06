import json
import sys
import os
import requests
from zipfile import ZipFile
from pathlib import Path
sys.path.append(str(Path.home() / ".kip/lib"))
import const

def set_config(args: dict):
    try:
        file = const.KIP_CONFIGURATIONS_FILE
        try:
            json.loads(file.read_text())
        except Exception:
            file.write_text('{}')
        configurations = json.loads(file.read_text())
        n_configurations = {
            **configurations,
            **args
        }
        for k in n_configurations:
            if k not in const.KIP_CONFIGURATIONS_ARGUMENTS:
                print(f'Warning: "{k}" will not be used by the program.')
                del n_configurations[k]
        file.write_text(json.dumps(n_configurations))
        return True
    except Exception as e:
        print(f"{str(e)}\n -- Failed --")
        return False

def get_conf():
    with open(const.KIP_CONFIGURATIONS_FILE) as file:
        return json.load(file)

def get_registry_url_conf():
    registry_url = get_conf()['registry.url']
    if not (
        registry_url.startswith('https://')
        or registry_url.startswith('http://')
    ):
        registry_url = 'https://' + registry_url
    if registry_url.endswith('/'):
        registry_url = registry_url[0:-1]
    return registry_url

def install(package_name):
    # Validate package name
    if len(package_name.split('/')) != 2:
        raise Exception('Malformed dependency name - dependency name must be in the format "author/repository"')
    else:
        registry_url = get_registry_url_conf()
        resource_download_url = registry_url + '/download/' + package_name
        file = requests.get(resource_download_url)
        print(file)

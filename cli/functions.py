import json
import sys
import os
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
    return const.KIP_CONFIGURATIONS_FILE.read_text()

def install(package_name):
    # Validate package name
    if len(package_name.split('/')) != 2:
        raise Exception('Malformed dependency name - dependency name must be in the format "author/repository"')

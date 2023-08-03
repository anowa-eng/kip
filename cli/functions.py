import json
import sys
import os
import zipfile
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

def __list_dir(folder):
    def recursive_path_map_function(path):
        path_dict = {}
        path_dict['dirname'] = os.path.dirname(path)
        if os.path.isdir(path):
            path_dict['contents'] = __list_dir(path)
    paths = os.listdir(folder)
    return list(map(
        lambda path: recursive_path_map_function(folder),
        paths
    ))

def list_dir(p_folder: Path):
    folder = str(p_folder)
    paths = {}
    paths['dirpath'] = folder
    paths['dirname'] = os.path.dirname(folder)
    if os.path.isdir(folder):
        paths['content'] = list_dir(folder)
    return paths

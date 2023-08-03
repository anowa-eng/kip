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

def __list_dir(p_folder: Path, root_folder: Path = None):
    folder = os.path.normpath(str(p_folder))
    paths = {}
    paths['path'] = p_folder
    paths['relative_path'] = p_folder.relative_to(root_folder or p_folder)
    paths['name'] = os.path.basename(folder)
    if os.path.isdir(folder):
        paths['content'] = list(map(
            lambda directory: __list_dir(Path(p_folder / directory), root_folder or p_folder),
            os.listdir(str(folder))
        ))
    return paths

print(__list_dir(Path("C:\\Users\\lanie\\.kip\\lib\\")))
import json
import sys
from pathlib import Path
sys.path.append(str(Path.home() / ".kip/lib"))
import const

def set_config(args):
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

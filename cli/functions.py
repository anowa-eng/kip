import json
import sys
from pathlib import Path
sys.path.append(str(Path.home() / ".kip/lib"))
import const

def __kebab_case_to_camel_case(string):
    n_string = [*string]
    while '-' in n_string:
        i = n_string.index('-')
        if i == len(string) - 1:
            del n_string[i]
        else:
            n_string[i] = str.upper(n_string[i + 1])
            del n_string[i + 1]
    n_string = ''.join(n_string)
    return n_string

def __set_config(**kwargs):
    try:
        with open(const.KIP_CONFIGURATIONS_FILE, 'r+') as reader:
            configurations = json.loads(reader.read())
            n_configurations = {
                **configurations,
                **kwargs
            }
        return True
    except Exception as e:
        print(str(e))
        return False

def set_registry_url(url):
    if url[-1] == '/':
        url = url[0:-1]
    return __set_config(defaultRegistry=url)
import json
from pathlib import Path
import sys
sys.path.append(str(Path.home() / ".kip/lib"))
import const

print(f"Creating s\u001b[1m{str(const.KIP_HOME_DIRECTORY)}\u001b[0m...")
const.KIP_HOME_DIRECTORY.mkdir()
print(f"Creating s\u001b[1m{str(const.KIP_VAR_DIRECTORY)}\u001b[0m...")
const.KIP_VAR_DIRECTORY.mkdir()
print(f"Creating s\u001b[1m{str(const.KIP_DEPENDENCIES_DIRECTORY)}\u001b[0m...")
const.KIP_DEPENDENCIES_DIRECTORY.mkdir()
print("Creating configuration file...")
const.KIP_CONFIGURATIONS_FILE.touch()
const.KIP_CONFIGURATIONS_FILE.write_text(json.dumps(const.KIP_DEFAULT_CONFIGURATIONS))

print("Setup complete.")
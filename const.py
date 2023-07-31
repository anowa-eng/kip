from pathlib import Path

KIP_HOME_DIRECTORY = Path.home() / ".kip"
KIP_VAR_DIRECTORY = Path.home() / ".kip/var"
KIP_CONFIGURATIONS_FILE = KIP_HOME_DIRECTORY / "config.json"

KIP_CONFIGURATIONS_KEYS = ['defaultRegistry']
CLI_KIP_CONFIGURATIONS_ARGUMENTS = ['default-registry']

KIP_DEFAULT_CONFIGURATIONS = {
    "registry.url": "https://127.0.0.1"
}

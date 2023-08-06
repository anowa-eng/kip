import argparse
from pathlib import Path
import sys
sys.path.append(str(Path.home() / ".kip/lib"))
from cli import functions

commandline_parser = argparse.ArgumentParser()

subparsers = commandline_parser.add_subparsers()

config_command = subparsers.add_parser(name="config")
config_command.add_argument('k')
config_command.add_argument('v')

install_command = subparsers.add_parser(name="install")
install_command.add_argument("package")
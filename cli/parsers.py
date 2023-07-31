import argparse
from pathlib import Path
import sys
sys.path.append(str(Path.home() / ".kip/lib"))
from cli import functions

commandline_parser = argparse.ArgumentParser()

subparsers = commandline_parser.add_subparsers()

config_command = subparsers.add_parser('config-set')
config_item = config_command.add_argument()
config_value = config_command.add_argument()
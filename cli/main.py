from pathlib import Path
import sys
sys.path.append(str(Path.home() / ".kip/lib"))
from cli import functions, parsers

argv = parsers.commandline_parser.parse_args(sys.argv[1:])
cmd = sys.argv[1]

if cmd == 'config':
    functions.set_config({
        argv.k: argv.v
    })
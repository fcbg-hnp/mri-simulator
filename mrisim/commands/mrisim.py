import argparse
from importlib.resources import files

from .. import set_log_level, simulate
from ..config import read_config


def run():
    """Run mrisim() command."""
    parser = argparse.ArgumentParser(
        prog=f"{__package__.split('.')[0]}-mrisim", description="mrisim"
    )
    parser.add_argument(
        "-f",
        "--fname",
        type=str,
        metavar="str",
        help=".ini configuration file.",
        default=files("mrisim.config") / "config.ini",
    )
    parser.add_argument(
        "--verbose",
        help="set the log level.",
        type=str,
        metavar="str",
        default="INFO",
    )
    args = parser.parse_args()
    verbose = args.verbose.strip().upper()
    set_log_level(verbose)

    key, repetition, period, wait = read_config(args.fname)
    simulate(key, repetition, period, wait, verbose=None)

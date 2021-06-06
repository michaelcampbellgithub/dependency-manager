"""
Main script to run

Args:
    --config:   Name of config file (if not in config directory, include relative path from there)
"""
from argparse import ArgumentParser
from distutils.util import strtobool


# Constants
AP = ArgumentParser()


if __name__ == '__main__':
    # Add args
    AP.add_argument(
        "--config",
        required=True,
        type=str,
        help="Name of config file (if not in config directory, include relative path from there)"
    )
    AP.add_argument(
        "--log",
        required=False,
        type=lambda x: bool(strtobool(x)),
        help="If True, logs to the ./logs directory. If False (default), prints to stdout",
        default=False
    )
    AP.add_argument(
        "--username",
        required=False,
        type=str,
        help="Username for accessing SCM"
    )
    AP.add_argument(
        "--password",
        required=False,
        type=str,
        help="Password for accessing SCM"
    )
    AP.add_argument(
        "--scm_key",
        required=False,
        type=str,
        help="SSH key for accessing SCM"
    )

    # Parse args
    args = vars(AP.parse_args())

    # Validate args

    # Parse config


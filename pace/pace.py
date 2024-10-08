#!/usr/bin/env python3
"""
pace - Easy pace conversion from the command line.

When stdin is 'pace' (H:M:S or M:S or S), considered mile pace, and paces
(400m, distance) at other distances are put to stdout.  'pace -a distance -t
distance' for, example, 59 at 400m to 1600m to get stdout 3:56 min/1600.
"""

import argparse

import pace_math as pm
import pace_gui as pg

def main():

    version = "0.1"  # major.minor.patch (huge change)(minor addition)(if patching bug fixes)
    parser = argparse.ArgumentParser(description=(__doc__ or "").strip())

    # add options to the CLI tool
    parser.add_argument("--version", action="version", version=version)

    # run from command line for command
    parser.parse_args()

if __name__ == "__main__":
    main()
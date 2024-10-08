#!/usr/bin/env python3
"""
pace - Easy pace conversion from the command line.

When stdin is 'pace', considered mile pace and paces (400m, distance) at other
distances are put to stdout.  'pace -a distance -t distance' for, example, 59
at 400m to 1600m to get stdout 3:56 min/1600.
"""

# ideas as we go
 #options
    # -a : converts the given pace (considered mile first) to mile pace at distance given
    # -t : converts a pace given, instead of printed out full list, to just the pace at wanted distance
 #command-line
    # need to put file in path directory and change name to 'pace' to use as pace in command line

import argparse
import pace_gui

def main():

    version = "0.1"  # major.minor.patch (huge change)(minor addition)(if patching bug fixes)
    parser = argparse.ArgumentParser(usage=(__doc__ or "").strip())

    # add options to the CLI tool
    parser.add_argument("--version", action="version", version=version)

    # run from command line for command
    parser.parse_args()

if __name__ == "__main__":
    main()
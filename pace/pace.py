#!/usr/bin/env python3
"""
Easy pace conversion from the command line.

When stdin is 'pace' (H:M:S or M:S or S), considered mile pace, and paces
(400m, distance) at other distances are put to stdout.  'pace -a distance -t
distance' for, example, 59 at 400m to 1600m to get stdout 3:56 min/1600.
Shorthand is 'pace 59 400 1600' for above example.
"""

import argparse

import pace_math as pm
import pace_gui as pg


# class for cleaner help statements, metavar not after each option format, just end
class CustomHelpFormatter(argparse.HelpFormatter):
    def _format_action_invocation(self, action):
        parts = []
        parts.append(', '.join(action.option_strings))
        if action.metavar:
            parts.append(action.metavar)
        try:
            return ' '.join(parts)
        except Exception:
            return super()._format_action_invocation(action)

def main():

    version = "0.1"  # major.minor.patch (huge change)(minor addition)(if patching bug fixes)
    parser = argparse.ArgumentParser(description=(__doc__ or "").strip(), prog='pace', formatter_class=CustomHelpFormatter)

    # add options to the CLI tool
    parser.add_argument(
        "-v", "--version",
        action="version", version=version
        )
    
    parser.add_argument(
        "-a", "--at",
        metavar="DISTANCE",
        help="specify the distance pace is at"
        )
    parser.add_argument(
        "-t", "--to",
        metavar="DISTANCE",
        help="specify to what distance you are converting to"
    )
    parser.add_argument(
        "-k", "--km",
        help="Switch distances and paces to be in terms of kilometers",
        action="store_true"
    )

    # run from command line for command
    parser.parse_args()

if __name__ == "__main__":
    main()
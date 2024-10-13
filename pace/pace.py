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
import pace_formatter as pf
import pace_gui as pg


# formatter_class declaration for cleaner help statements (e.g. '-a, --at DISTANCE')
class CleanerHelpFormat(argparse.HelpFormatter):
    def _format_action_invocation(self, action):
        try:
            parts = []
            parts.append(', '.join(action.option_strings))
            if action.metavar:
                parts.append(action.metavar)
                return ' '.join(parts)
            raise
        except:  # fallback to default formatting if error
            return super()._format_action_invocation(action)

def main():

    version = "0.2"  # major.minor.patch (huge change)(minor addition)(if patching bug fixes)
    parser = argparse.ArgumentParser(
        description=(__doc__ or "").strip(), prog='pace', 
        formatter_class=CleanerHelpFormat
    )

    # add options to the CLI tool
        # returns value
    parser.add_argument(
        "-v", "--version",
        action="version", version=version
        )
    
        # positional
    parser.add_argument(
        "pace",
        help="The initial pace at distance, so 0:6:12 is 6:12 min/mile",
        nargs="+"
    )
    
        # changes value
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

        # boolean
    conversion_group = parser.add_argument_group("conversion")
    conversion_group.add_argument(
        "-k", "--km",
        help="Set distances and paces to be in terms of kilometers",
        action="store_true"
    )

    # get the values and what was passed in command line
    args = parser.parse_args()

    # Set choices and print if shorthand used
    if not (args.at or args.to):
        try:
            args.at = args.pace[1]
            args.to = args.pace[2:]
        except:
            pass
    
    pf.output(args.pace, args.km, args.at, args.to)


if __name__ == "__main__":
    main()
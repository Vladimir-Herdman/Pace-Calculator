#!/usr/bin/env python3
"""
Easy pace conversion from the command line.

When stdin is 'pace' (H:M:S or M:S or S), considered mile pace, and paces
(400m, distance) at other distances are put to stdout.  'pace -a distance -t
distance' for, example, 59 at 400m to 1600m to get stdout 3:56 min/1600.
Shorthand is 'pace 59 400m 1600m' for above example.
"""

import argparse
from subprocess import run

import paces_calc.pace_formatter as pf
import paces_calc.pace_gui as pg


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

    version = "0.8.0"  # major.minor.patch (huge change)(minor addition)(if patching bug fixes)
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
        help="The initial pace, so 0:6:12 is 0 hourse, 6 minutes, and 12 seconds",
        nargs="*"
    )

        # see window application of pace tool
    parser.add_argument(
        "-g", "--gui",
        action="store_true",
        help="open window application for pace distance conversions outside of command line"
    )

        # changes value
    parser.add_argument(
        "-a", "--at",
        metavar="DISTANCE",
        help="specify the distance pace is at (i.e. 1600m)"
        )
    parser.add_argument(
        "-t", "--to",
        metavar="DISTANCE",
        help="specify to what distance(s) you are converting to (i.e. 200m 400m 1mi)",
        nargs="*"
    )

    # get the values and what was passed in command line
    args = parser.parse_args()

    if (args.gui):
        pg.window_main()

    if (not args.pace):  # if no pace value given
        raise ValueError("usage: pace [-h] [-v] [-g] [-a DISTANCE] [-t DISTANCE] pace [pace ...]\n"
                         "    pace: error: expected at least one argument for pace value")

    if (args.pace[0] == "man"):  # if request for man page (pace man)
        man_path = __file__.replace("pace.py", "pace.1", 1)
        run(["man", man_path], check=True)
        exit(0)

    # Set choices and print if shorthand used
    if not (args.at or args.to):
        try:
            args.at = args.pace[1]
            args.to = args.pace[2:]
            args.pace = [args.pace[0]]
        except:
            args.pace = [args.pace[0]]

    pf.output(args.pace, args.at, args.to)


if __name__ == "__main__":
    main()

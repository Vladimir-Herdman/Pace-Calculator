"""To use this package as an import, such as `import paces_calc` in a
python file, after importing paces_calc, simply write `paces_calc.main()` 
below the import, and then the file can be run as if it were the command 
line tool `pace`.  Of course, this is after pip3 installing `paces_calc`

For example, what to wrint in file (named `pace_cli.py` for example):
```
import paces_calc
paces_calc.main()
```

And then, how to use the file in the command line (from same directory
as file):
```
python3 pace_cli.py 4:12 -a 1600m -t 200m 400m 800m
```
"""
# The below import makes it so that when users pip3 install paces_calc and then
# say import paces_calc, they can run paces_calc.main(), as the __init__ files
# purpose is to be the API of the the package created
from paces_calc.pace import main
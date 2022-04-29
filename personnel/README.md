# Personnel (web)

## Challenge

`` 
A challenge that was never discovered during the 2021 Constellations mission... now ungated :) 
`` 

Files:
* [app.py](personell.py)

## Solution 

The flag can be retrieved by running a regular expression egainst the system.
RegExp `.*` anly shows the values from file `users.txt`.
The flag from file `flag.txt` is appended after these values.

Running a RegEx, explicitly filtering including a new line `.*\nflag.*` results in an output `Vulpecula flag{f0e659b45b507d8633065bbd2832c627}`
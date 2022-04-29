# Read the Rules

## Challenge
``` 
Please follow the rules for this CTF! 
``` 
Link to  https://ctf.nahamcon.com/rules


## Solution 

The Flag is hidden in a comment of the sites HTML code
```
curl https://ctf.nahamcon.com/rules | grep flag{
```

Flag: `flag{90bc54705794a62015369fd8e86e557b}`
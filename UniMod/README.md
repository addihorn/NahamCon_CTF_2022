# UniMod (Cryptography)

## Challenge

```
I was trying to implement ROT-13, but got carried away. 
```

Files:
* [out](out)
* [unimod.py](unimod.py)

## Solution

ROT-13 is a cesar-cypher that is reversable with it's own key (due to having 26 letters in the alphabet)
But the output of the cyphertext looks like chinese characters.
Running it in Goggle-Translate did not result in anything meaningfull.

The code in `unimod.py` reveals the used key to do the calculation, some randum number between 0 and 0xFFFD (65533).   
The cyphertext is calculated by adding the plaintext + key and dividing(modulo) this number by 0xFFFD.  
Having a key near 0xFFFD would result in a overflow and in a cyphertext with ascii-numbers in the small numbers (i would assume roman alphabet) for at least a few characters.  
But since all cyphertext-characters are in the high ascii-numbers (chinese alphabet) a key significantly smaller than 0xFFFD was used.

This renders the modulo operation meaningless and we can calculate the key by checking teh difference of the first characters. (we know the first few characters of our plaintext to be `flag{`)

```python
>>> ord('饇')-ord('f')
39137
>>> ord('饍')-ord('l')
39137
>>> ord('饂')-ord('a')
39137
```

The key used, seems to be 39137.
Fixing the key, and altering the paython-script to `unimod-decode.py` results in the flag `flag{4e68d16a61bc2ea72d5f971344e84f11}`


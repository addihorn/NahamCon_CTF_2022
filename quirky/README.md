# Quirky (Warmup)

## Challenge 

```
This file is seems to have some strange pattern... 
```

Files:
* [quirky](quirky)
## Solution

The file `quirky` is a long ASCII-Text.  
The character-pattern looks like a Hex-String, so it needs to be converted to ASCII.

Running a [Hex-to-Ascii-Conversions](https://www.rapidtables.com/convert/number/hex-to-ascii.html) we can see, that the file has a lot of binary-characters and starts with "PNG"

Saving the content as `quirky.png`and opening the file reveals a QC-Code.
Reading this QR-Code (https://webqr.com/) reveals the flag

Flag: `flag{b7e2a32f5ae629dcfb1ac210d1f0c032}`


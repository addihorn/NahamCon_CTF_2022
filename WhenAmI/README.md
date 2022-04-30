# WhenAmI (Misc)

## Challenge 

```
I know where I am, but... when am I?

Download the file below.

NOTE: Flag submission format is flag{[number of seconds goes here]}, such as flag{600}.
```

Files:
* [challenge.txt](challenge.txt)

## Solution

Locate -13.582075733990298, -172.5084838587106  
=> Samoa, Pacific Ocean.  
=> Time Zone: Apia (UCT +14)  


Locate -14.327595989244111, -170.71287979386747  
=> Tualauta, Western District, American Samoa  
=> Time Zone: Samoa Standard Time (UCT -11)  


Let Dec 28th 11:59AM be 0  
Time Diff to Dec 31st 1:00AM ... 219.660 sec  

One hour (3600 sec) flight would, landing on  
Dec 31st 2:00AM Apia Standard Time  
Dec **30st** 1:00AM Samoa Standard Time

Waiting until 12:00PM Samoa Standard Time (11h, 39.600 sec)

One hour flight (3600 sec), landing on  
Dec 31st 01:00PM Samoa Standard Time  
Dec **31st* 2:00PM Apia Standard Time  

+10 hours (36.000)

calculate  
```
  219660
+   3600
+  39600
+   3600
+  36000
---------
  302460
-  86400 (Samoa lost a day on Dec 29th 2011)
---------
  216060
```
https://earthsky.org/human-world/friday-december-30-2011-struck-from-samoan-calendar/

### Alternative

First time looking on the watch
```
$ date --date="Dec 28 11:59:00 UTC+14 2011" +%s
1325023140
```

Final time
```
$ date --date="Jan 01 00:00:00 UTC+14 2012" +%s
1325325600 
```

Since it is calculating from UTC, the second timestamp is off by one day, because the missing Dec 29th 2011.

1325325600 - 86400 - 1325023140 = 216060

So the flag is `flag{216060}`

Shoutout to [@Sayan-404](https://github.com/Sayan-404) for the discussion and final piece of information.

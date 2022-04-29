# Steam Locomotive

## Challenge

```
I keep accidentally mistyping the ls command! 
```

## Solution

Running ssh to connect to the server.
The server input is blocked by the `sl` Programm https://www.cyberciti.biz/tips/displays-animations-when-accidentally-you-type-sl-instead-of-ls.html
and terminates the ssh-session after execution.

Checking with `ssh --help` we can see, that we can give a optional command to the connection

running 
```
$ ssh -p 31203 user@challenge.nahamcon.com ls -l
user@challenge.nahamcon.com's password: 
total 4
-r--------    1 user     user            39 Apr 24 16:44 flag.txt
```

We can see that flag-file, so we can run 
```
$ ssh -p 31203 user@challenge.nahamcon.com cat flag.txt
user@challenge.nahamcon.com's password: 
flag{4f9b10a81141c7a07a494c28bd91d05b}
```
to retrive the flag.
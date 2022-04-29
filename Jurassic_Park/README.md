# Jurassic Park (web)

## Challenge
```
Dr. John Hammond has put together a small portfolio about himself for his new theme park, Jurassic Park. Check it out here! 
```

## Solution

The source code does not give any hints where the flag could be.
Accessing folders `assets` and `css` did not result in anything.

In assets was an image tought, that wasn't used in the website `backup.jpg`
Checking for stenographic informations with `strings backup.jpg` did not result anything.
Neither did checking for metadata with `file backup.jpg`

Following https://superuser.com/questions/642555/how-can-i-view-all-files-in-a-websites-directory I was able to see, that there is a publicly available `robots.txt`-file, which resulted in

```
User-agent: *
Disallow: /ingen/
```

Following this path navigating to directory `/ingen/` revealed the flag
`flag{c2145f65df7f5895822eb249e25028fa}`
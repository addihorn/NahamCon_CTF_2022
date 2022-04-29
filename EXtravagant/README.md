# EXtravagant (Web)

## Challenge

```
I've been working on a XML parsing service. It's not finished but there should be enough for you to try out.

The flag is in /var/www
```

## Solution

XML parster points to some kind of XML-injection
OWASP.org points to a vector called XEE (XML External Entity)

https://owasp.org/www-community/vulnerabilities/XML_External_Entity_(XXE)_Processing

Updating file `attack.xml` and reading it out, results in flag `flag{639b72f2dd0017f454c44c3863c4e195}`
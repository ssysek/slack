# slack

### Database
To get into database (from root):
```
su postgres
psql postgres://ziewdlrk:2TnhYeeQs3W-ZCJh5oZgTlj6Q1EXFO0x@kandula.db.elephantsql.com:5432/ziewdlrk
```
or:
```
sudo -u postgres psql postgres://ziewdlrk:2TnhYeeQs3W-ZCJh5oZgTlj6Q1EXFO0x@kandula.db.elephantsql.com:5432/ziewdlrk
```
And run desired requests, like:
```
select * from users;
select * from posts;
```

### REST
Example requests(GET):
```
http://localhost:86/all_users
```

POST with added parameter:
```
http://localhost:86/user_id?user_id=1
```

If you can't run server (getting error like: [Errno 48] Address already in use):
```
ps -fA | grep python
root      8072  7133  0 02:33 pts/0    00:00:01 ~/slack/slack_server.py
kill 8072
```
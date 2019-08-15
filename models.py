from google.appengine.ext import ndb

class Note(ndb.Model):
    user_id = ndb.StringProperty()
    content = ndb.StringProperty()
    timestamp = ndb.DateTimeProperty(auto_now_add=True)

class User(ndb.Model):
    nickname = ndb.StringProperty()
    email = ndb.StringProperty()
    description = ndb.StringProperty()

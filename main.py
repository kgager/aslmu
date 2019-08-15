import os
import json
import webapp2
import jinja2
import urllib
from random import randint
from urllib import urlencode
from google.appengine.api import urlfetch
from google.appengine.api import users
from models import *

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def create_user(nickname, email):
    user = User(nickname=nickname, email=email)
    user.put()

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        form_template = jinja_env.get_template('templates/mainpage.html')
        self.response.write(form_template.render())
    def post(self):
        form_template = jinja_env.get_template('templates/mainpage.html')
        self.response.write(form_template.render())

class LoginPageHandler(webapp2.RequestHandler):
    def get(self):
        form_template = jinja_env.get_template('templates/loginpage.html')
        googleUser = users.get_current_user()
        if googleUser:
            log_url=users.create_logout_url("/")
        else:
            log_url=users.create_login_url("/main")
        self.response.write(form_template.render({
        "log": log_url
        }))

class MyProfilePageHandler(webapp2.RequestHandler):
    def get(self):
        form_template = jinja_env.get_template('templates/myprofile.html')
        self.response.write(form_template.render())

class RandomPageHandler(webapp2.RequestHandler):
    def get(self):
        form_template = jinja_env.get_template('templates/random.html')
        self.response.write(form_template.render())
class CulturePageHandler(webapp2.RequestHandler):
    def get(self):
        form_template = jinja_env.get_template('templates/culture.html')
        self.response.write(form_template.render())
class GetConnectPageHandler(webapp2.RequestHandler):
    def get(self):
        form_template = jinja_env.get_template('templates/getconnect.html')
        self.response.write(form_template.render())

class TranslatorPageHandler(webapp2.RequestHandler):
    def get(self):
        form_template = jinja_env.get_template('templates/translatorpage.html')
        self.response.write(form_template.render())
    def post(self):
        Query = str(self.request.get("Query")).split(" ")
        print(Query)
        result = []
        for word in Query:
            if word in lexicon:
                giphyP = {
                "q": lexicon.get(word),
                "api_key": "BWkKadSlz5EiOcSh3R61iPb5WPKb50Ha",
                "limit": 5,
                "rating": "g",
                "lang": "en"
                }
                giphyBaseURL = "http://api.giphy.com/v1/gifs/search?"
                giphyURL = giphyBaseURL + urlencode(giphyP)
                giphyR = json.loads(urlfetch.fetch(giphyURL).content)
                print(giphyR['data'])
                gif_url = giphyR['data'][0]['images']['original']['url']
                result.append(gif_url)
            else:
                result.append(word)
        form_template = jinja_env.get_template('templates/translatorpage.html')
        self.response.write(form_template.render({
        "result": result
        }))

class EventsPageHandler(webapp2.RequestHandler):
    def get(self):
        form_template = jinja_env.get_template('templates/eventpage.html')
        self.response.write(form_template.render())

class IndexPageHandler(webapp2.RequestHandler):
    def get(self):
        form_template = jinja_env.get_template('templates/index.html')
        self.response.write(form_template.render())

class MapsPageHandler(webapp2.RequestHandler):
    def get(self):
        form_template = jinja_env.get_template('templates/mappage.html')
        self.response.write(form_template.render())
    def post(self):
        latitude = int(self.request.get("lat"))
        longitude = int(self.request.get("lng"))
        form_template = jinja_env.get_template('templates/mappage.html')
        self.response.write(form_template.render({
        "latitude" : latitude,
        "longitude" : longitude
        }))


class ManualHandler(webapp2.RequestHandler):
    def get(self):
        form_template = jinja_env.get_template('templates/manual.html')
        self.response.write(form_template.render())

class ChatRoomHandler(webapp2.RequestHandler):
    def get(self):
        notes = Note.query().order(-Note.timestamp).fetch(limit=20)
        user = users.get_current_user()
        logout_url = users.create_logout_url('/') if user else None
        template = jinja_env.get_template('templates/main.html')
        self.response.write(template.render({
            'notes': notes,
            'nickname' : user.nickname() if user else None,
            'logout_url': logout_url }))

class NoteHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        template = jinja_env.get_template('templates/note_entry.html')
        self.response.write(template.render({
            'nickname' : user.nickname(),
            'logout_url': users.create_logout_url('/')}))
    def post(self):
        note = self.request.get('note')
        if len(note) > 1500:
            note = note[:1500]
        user = users.get_current_user()
        Note(user_id=user.user_id(), content=note).put()
        self.redirect('/chatroom')

class MostRecentNoteHandler(webapp2.RequestHandler):
    def get(self):
        note = Note.query().order(-Note.timestamp).get()
        self.response.headers['Content-Type'] = 'text-plain'
        self.response.write(str(note.timestamp if note else ''))

lexicon = {
    "hello": "asl hello",
    "car": "asl car",
    "dog": "asl dog sign with robert",
    "cat": "asl cat",
    "house": "asl house",
    "table": "asl car",
    "chair": "asl chair",
    "drink": "asl drink",
    "hat": "asl hat",
    "tv": "asl tv",
    "shirt": "asl shirt",
    "shoes": "asl shoes",
    "water": "asl water",
    "allergic": "asl allergic",
    "pants": "asl pants"
}



app = webapp2.WSGIApplication([
    ('/chatroom', ChatRoomHandler),
    ('/notes', NoteHandler),
    ('/most-recent-note', MostRecentNoteHandler),
    ('/main', MainPageHandler),
    ('/', LoginPageHandler),
    ('/translator', TranslatorPageHandler),
    ('/events', EventsPageHandler),
    ('/maps', MapsPageHandler),
    ('/myprofile', MyProfilePageHandler),
    ('/manual', ManualHandler),
    ('/index', IndexPageHandler),
    ('/culture', CulturePageHandler),
    ('/getconnect', GetConnectPageHandler),
    ('/random', RandomPageHandler),
], debug=True)

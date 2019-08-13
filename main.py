import os
import json
import webapp2
import jinja2
import urllib
from random import randint
from urllib import urlencode
from google.appengine.api import urlfetch

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

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
        self.response.write(form_template.render())

class MyProfilePageHandler(webapp2.RequestHandler):
    def get(self):
        form_template = jinja_env.get_template('templates/myprofile.html')
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
                "limit": 1,
                "rating": "g",
                "lang": "en"
                }
                giphyBaseURL = "http://api.giphy.com/v1/gifs/search?"
                giphyURL = giphyBaseURL + urlencode(giphyP)
                giphyR = json.loads(urlfetch.fetch(giphyURL).content)
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

class ManualHandler(webapp2.RequestHandler):
    def get(self):
        form_template = jinja_env.get_template('templates/manual.html')
        self.response.write(form_template.render())

class ChatroomPageHandler(webapp2.RequestHandler):
    def get(self):
        form_template = jinja_env.get_template('templates/chatroom.html')
        self.response.write(form_template.render())

lexicon = {
    "hello": "asl hello",
    "car": "asl car",
    "dog": "asl dog",
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
    ('/main', MainPageHandler),
    ('/', LoginPageHandler),
    ('/translator', TranslatorPageHandler),
    ('/events', EventsPageHandler),
    ('/maps', MapsPageHandler),
    ('/myprofile', MyProfilePageHandler),
    ('/chatroom', ChatroomPageHandler),
    ('/manual', ManualHandler),
    ('/index', IndexPageHandler)
], debug=True)

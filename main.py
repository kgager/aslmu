import os
import json
import webapp2
import jinja2
from urllib import urlencode
from google.appengine.api import urlfetch

jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# the handler section
#class MainPage(webapp2.RequestHandler):
    #def get(self):
        #welcome_template = jinja_env.get_template('templates/welcome.html')
        #self.response.write(welcome_template.render())  # the response

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        form_template = jinja_env.get_template('templates/mainpage.html')
        self.response.write(form_template.render())  # the response
    def post(self):
        form_template = jinja_env.get_template('templates/mainpage.html')
        self.response.write(form_template.render())

class LoginPageHandler(webapp2.RequestHandler):
    def get(self):
        form_template = jinja_env.get_template('templates/loginpage.html')
        self.response.write(form_template.render())  # the response

class MyProfilePageHandler(webapp2.RequestHandler):
    def get(self):
        form_template = jinja_env.get_template('templates/myprofile.html')
        self.response.write(form_template.render())

class TranslatorPageHandler(webapp2.RequestHandler):
    def get(self):
        form_template = jinja_env.get_template('templates/translatorpage.html')
        self.response.write(form_template.render())  # the response
    def post(self):
        english = self.request.get("english")
        form_template = jinja_env.get_template('templates/translatorpage.html')
        self.response.write(form_template.render({
        "english": english
        }))  # the response

class EventsPageHandler(webapp2.RequestHandler):
    def get(self):
        form_template = jinja_env.get_template('templates/eventpage.html')
        self.response.write(form_template.render())  # the response

class MapsPageHandler(webapp2.RequestHandler):
    def get(self):
        form_template = jinja_env.get_template('templates/mappage.html')
        self.response.write(form_template.render())  # the response

# class RecipeDisplayHandler(webapp2.RequestHandler):
#     def post(self):
#         query=self.request.get('query')
#         base_url = 'http://www.recipepuppy.com/api/?'
#         params = { 'q': query }
#         response = urlfetch.fetch(base_url + urlencode(params)).content
#         results = json.loads(response)
#         # bottom=self.request.get('bottom')
#         # memetype=self.request.get('memetype')
#         result_template = jinja_env.get_template('templates/recipe.html')
#         self.response.write(result_template.render({
#             'results': results
#             # 'query': query
#             # 'bottom': bottom,
#             # 'image_file': memetype
#
#         }))

# the app configuration section
app = webapp2.WSGIApplication([
    ('/main', MainPageHandler), #this maps the root url to the Main Page Handler
    ('/', LoginPageHandler),
    ('/translator', TranslatorPageHandler),
    ('/events', EventsPageHandler),
    ('/maps', MapsPageHandler),
    ('/myprofile', MyProfilePageHandler)
    #('/recipe', RecipeDisplayHandler)
], debug=True)

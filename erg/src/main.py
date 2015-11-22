import os
import dotenv
dotenv.load_dotenv("../.env")

from bottle import route, run
from typeform import Typeform



form_uid = os.environ['TYPEFORM_ID']

@route('/')
def index():
    f = Typeform()
    return f.get()

@route('/erg/user/')
def users():
    "List all users in JSON: {UID: {name: <USERNAME>, email: <EMAIL>} ... } "
    pass


@route('/erg/user/<uid>', method = 'GET')
def user_erg(uid):
    "Return JSON-encoded ERG for user with UID"
    pass


@route('/erg/form/', method = 'GET')
def erg_forms():
    "Returns all available forms"
    pass

@route('/erg/form/<fid>', method = 'GET')
def erg_form(fid):
    "Return a JSON-encoded Typeform form with id fid"
    f = Typeform.form(form_uid)
    pass


run(host='localhost', port=8080)

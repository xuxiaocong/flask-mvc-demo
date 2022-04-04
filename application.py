from flask import Flask

app = Flask(__name__)

from interceptors.all import *
from interceptors.error_handler import *
from controllers.index import index_page
from controllers.api.user_api import user_api

app.register_blueprint(index_page, url_prefix="/")
app.register_blueprint(user_api, url_prefix="/api/user")
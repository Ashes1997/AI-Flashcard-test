from flask import Flask
import os
def create_app():
  app = Flask(__name__)
  app.config['SECRET KEY'] = 'blahblahblah'
  return app
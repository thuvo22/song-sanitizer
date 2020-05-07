from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
from sanitizer import *


# Flask utils
from flask import jsonify 
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/join', methods=['GET','POST'])
def my_form_post():
    song = request.form['text1']
    word = request.args.get('text1')
    artist = request.form['text2']
    combine = vet(song,artist)
    result = {
        "output": combine
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)

if __name__ == '__main__':
    # app.run(port=5002, debug=True)

    # Serve the app with gevent
    #http_server = WSGIServer(('', 5000), app)
    #http_server.serve_forever()
    app.run()

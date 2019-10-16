from flask import Flask, render_template, request, url_for
import requests
import os
from random import random

app = Flask(__name__)

@app.route('/')
def test():
    return render_template('index.html', msg='Hiiiii')


if __name__ == "__main__":
    app.run(Debug=True)
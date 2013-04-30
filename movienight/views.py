from flask import redirect
from movienight import app


@app.route('/')
def index():
    return redirect('/admin/')

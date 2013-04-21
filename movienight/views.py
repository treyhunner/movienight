from movienight import app


@app.route('/')
def index():
    return '<a href="/admin/">Admin</a>'

from flask import Flask
from views import views


app = Flask(__name__) #init app
app.register_blueprint(views, url_prefix = "/views")

if __name__ == '__main__':
    app.run(debug=True) #debug = true so that changed files will refresh app automatically
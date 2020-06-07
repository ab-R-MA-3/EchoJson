from flask import Flask
import views

app = Flask(__name__)

app.register_blueprint(views.app)
app.config['JSON_AS_ASCII'] = False

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
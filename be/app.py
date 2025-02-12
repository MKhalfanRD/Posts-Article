from flask import Flask
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from models import db
from routes import api
from flask_cors import CORS
from flask_migrate import Migrate

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)

app.register_blueprint(api, url_prefix="/api")
migrate = Migrate(app, db)  

if __name__ == "__main__":
    app.run(debug=True)
